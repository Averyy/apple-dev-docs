# TN3133: Packaging a Metal renderer

**Framework**: Technotes

Distribute a Metal renderer in a Swift package.

#### Overview

Several individual pieces make up a Metal renderer: The CPU-side app code, the GPU-side shaders, and the structures that the app code and the shaders share. Bundling these pieces together in a single Swift package is an excellent way to modularize a renderer for use in multiple projects. Read this technote to discover a Swift package structure that shares C structs between Swift and Metal code, and to learn how to access the compiled Metal source as a `MTLLibrary`.

#### Configure the Package Manifest

The package structure that enables you to package Swift, Metal, and shared C sources in a single Swift package requires two [`Target`](https://developer.apple.com/documentation/PackageDescription/Target) declarations, as shown in the following example package manifest:

```swift
// swift-tools-version:5.5

import PackageDescription

let package = Package(
    name: "MyRenderer",
    products: [
        .library(
            name: "MyRenderer",
            targets: ["MyRenderer"]),
    ],
    targets: [
        // MyRenderer contains .swift and .metal files.
        .target(
            name: "MyRenderer",
            dependencies: ["MySharedTypes"]),

        // MySharedTypes contains a .h file nested inside of a folder named "include", and an empty .m file, specifying that the target should be compiled as an Obj-C target.
        .target(name: "MySharedTypes")
    ]
)
```

The `MyRenderer` target contains the Swift source files, as well as the Metal source files.

The `MySharedTypes` target contains the shared C structs within a header file. Store this header in the directory specified as the [`publicHeadersPath`](https://developer.apple.com/documentation/PackageDescription/Target/publicHeadersPath) for this target, so that the header is accessible from the `MyRenderer` target. It’s also important to have at least one Obj-C, C, or C++ implementation file in this target.

> **Note**: A target cannot have source files from both Swift and C-family languages, but it’s OK to have Swift and Metal sources in the same target because SwiftPM treats Metal files as resource files.

Add the `MySharedTypes` target as a dependency of the `MyRenderer` target to access the shared C structs in the `MyRenderer` target.

Here is a visual representation of the file structure described in the example above:

```None
.
└── MyRenderer
    ├── Package.swift
    ├── README.md
    └── Sources
        ├── MyRenderer
        │   ├── Renderer.swift
        │   └── Shaders.metal
        └── MySharedTypes
            ├── SharedTypes.m
            └── include
                └── SharedTypes.h
```

#### Accessing the Shared C Structs in Swift

Swift Package Manager creates a module that contains the C structs found in the [`publicHeadersPath`](https://developer.apple.com/documentation/PackageDescription/Target/publicHeadersPath), and because the Swift target is dependent on the C target, the C structs are directly accessible from Swift.

Continuing with the same naming from the example above, consider the following header located at `MyRenderer/Sources/MySharedTypes/include/SharedTypes.h`:

```Obj-C
#ifndef SharedTypes_h
#define SharedTypes_h

#import <simd/simd.h>

typedef struct {
    vector_float2 position;
    vector_float4 color;
} AAPLVertex;

#endif /* SharedTypes_h */
```

The shared types are accessible in Swift files after importing the `MySharedTypes` module, for example:

```swift
import MySharedTypes

let vertex = AAPLVertex(position: .init(250, -250), color: .init(1, 0, 0, 1))
```

#### Accessing the Shared C Structs in Metal

Using the same package structure defined above, the shared types are accessible in Metal files after importing the appropriate header file:

```metal
// A relative path to SharedTypes.h.
#import "../MySharedTypes/include/SharedTypes.h"

// Use any C types found in the imported header in this Metal file.
```

#### Retrieving the Precompiled Metal Library

Swift Package Manager compiles the Metal source to a `.metallib` and stores it in the resource bundle of the target. This resource bundle is accessible from Swift through the `Bundle.module` static property.

To create a `MTLLibrary` from this bundle in the Swift target:

```swift
do {
  // device is a `MTLDevice`.
  let library = try device.makeDefaultLibrary(bundle: Bundle.module)
} catch {
  // Handle the error.
}
```

For more information about the `Bundle.module` static property, see [`Bundling resources with a Swift package`](https://developer.apple.com/documentation/Xcode/bundling-resources-with-a-swift-package).

#### Introducing a Custom Metal Compilation Step

You might want to invoke the `metal` command-line tool yourself, and provide it with arguments that fit your specific needs. For example, you could compile your Metal source with debug symbols to enable shader debugging in a client app.

To introduce a custom Metal compilation step to the build process, create a Swift Package Build Tool Plugin that invokes the `metal` command-line tool with custom arguments, precompiles a `.metallib`, and stores it in the target’s resources directory by specifying it as an output file of the build command. Then, apply the plugin to the target that contains your `.metal` files.

For more information about creating and applying a Swift Package Build Tool Plugin, see [`Create Swift Package plugins`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110401/).

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3133-packaging-a-renderer)*
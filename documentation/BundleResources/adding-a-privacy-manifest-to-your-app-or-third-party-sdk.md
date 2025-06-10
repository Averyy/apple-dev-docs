# Adding a privacy manifest to your app or third-party SDK

**Framework**: Bundle Resources

Report the data you collect and the required reasons API you use in your app or third-party SDK.

#### Overview

A privacy manifest is a property list file (`PrivacyInfo.xcprivacy`) that you add to your target’s resources. The privacy manifest describes the privacy practices of an app or third-party SDK. To add a privacy manifest to your app or third-party SDK using Xcode, see [`Privacy manifest files`](privacy-manifest-files.md). All privacy manifest files in your app must be valid, containing only the expected keys and values. For more information, see “Describe the data your app or third-party SDK collects,” in [`Describing data use in privacy manifests`](describing-data-use-in-privacy-manifests.md).

> ❗ **Important**: App Store Connect rejects app submissions that include invalid privacy manifest files. If you upload an app to App Store Connect that contains privacy manifest files with unexpected keys or values, you receive an email that includes the name and path of the invalid files in your app bundle. If an invalid file comes from a third-party SDK, contact its developer for an updated version of the SDK that includes a valid privacy manifest. To troubleshoot invalid privacy manifests, see [`TN3181: Debugging an invalid privacy manifest`](https://developer.apple.com/documentation/Technotes/tn3181-debugging-invalid-privacy-manifest). Starting February 12, 2025, apps you submit for review in App Store Connect must contain a valid privacy manifest file for a certain number of commonly used third-party SDKs. For more information, see [`Upcoming third-party SDK requirements`](https://developer.apple.comhttps://developer.apple.com/support/third-party-SDK-requirements/).

When you add a privacy manifest to the target that builds your app or third-party SDK in Xcode, Xcode automatically places this file in the correct location based on the type of product and its target platform. If you don’t use Xcode to build your product, use the information below to place the privacy manifest in the correct location. Even if you use Xcode, you might find this information useful to verify the privacy manifest location in your product.

##### Add a Privacy Manifest to Your App

If you build an iOS, iPadOS, tvOS, visionOS, or watchOS app, place the privacy manifest at the root of your app’s bundle. The example below shows the bundle structure of an iOS app called `Sample`, which lists `PrivacyInfo.xcprivacy` at `Sample.app/PrivacyInfo.xcprivacy`:

```swift
Sample.app/
    Info.plist
    Sample
    PrivacyInfo.xcprivacy 
    ...
```

For macOS and Mac Catalyst apps, place the privacy manifest file in `Contents/Resources/` in your app’s bundle. The following example shows the bundle structure of a macOS app called `MacSample`, which lists `PrivacyInfo.xcprivacy` at `MacSample.app/Contents/Resources/PrivacyInfo.xcprivacy`:

```swift
MacSample.app/
    Contents/
        Info.plist
        MacOS/
            MacSample
        Resources/
            PrivacyInfo.xcprivacy
        ...
```

##### Add a Privacy Manifest to Your Framework

The location where you place the privacy manifest in your framework depends on the platform. For iOS, iPadOS, tvOS, visionOS, or watchOS frameworks, place the privacy manifest at the root of your framework’s bundle. The example below shows the layout of an iOS framework called `SampleFramework`, which lists `PrivacyInfo.xcprivacy` at `SampleFramework.framework/PrivacyInfo.xcprivacy`:

```swift
SampleFramework.framework/
    Info.plist 
    SampleFramework
    PrivacyInfo.xcprivacy 
    ...
```

For macOS and Mac Catalyst frameworks, place the privacy manifest file in `Versions/A/Resources/` in your framework’s bundle. The following example shows the layout of a macOS framework named `MacSampleFramework` that supports a single version (`A)`and includes a privacy manifest file. Its bundle structure lists `PrivacyInfo.xcprivacy` at `MacSampleFramework.framework/Versions/A/Resources/PrivacyInfo.xcprivacy`:

```swift
MacSampleFramework.framework/
    MacSampleFramework -> Versions/Current/MacSampleFramework
    Resources -> Versions/Current/Resources
    Versions/
        Current -> A
        A/
            MacSampleFramework
            Resources/
                Info.plist 
                PrivacyInfo.xcprivacy
            ...
    ...
```

##### Add a Privacy Manifest to Your Swift Package

A Swift package’s resources can include its privacy manifest file. For more information about adding resource files to Swift packages, see [`Bundling resources with a Swift package`](https://developer.apple.com/documentation/Xcode/bundling-resources-with-a-swift-package). Source files reside in a subfolder of a package’s `Sources` directory that has the same name as the target they belong to. This is the default location for resources. If your resource files reside in the default location, add the privacy manifest to it. The following example shows a package manifest that declares the `SomeLibrary` target. Place your privacy manifest file in  if you don’t specify an alternative location, as shown below:

```swift
SamplePackage/
    README.md
    Package.swift
    Sources/
        SomeLibrary/
            SomeLibrary.swift
            Product.swift
            PrivacyInfo.xcprivacy
            ...
    Tests/
        ...
```

Alternatively, if your resource files reside in a subfolder separate from your source files, add the privacy manifest to this directory. Place your privacy manifest file in `Sources/SomeLibrary/Resources` if you put all your resource files into a directory named `Resources`:

```swift
SamplePackage/
    README.md
    Package.swift
    Sources/
        SomeLibrary/
            SomeLibrary.swift
            Product.swift
            ...
            Resources/
                PrivacyInfo.xcprivacy
                ...
    Tests/
        ...
```

Xcode doesn’t recognize privacy manifest files as resources by default. After adding the manifest file to your package, explicitly declare the file or the directory that includes it as a package resource. In the following example, the package manifest declares `PrivacyInfo.xcprivacy` as an explicit resource:

```swift
targets: [
    .target(
        name: "SomeLibrary",
        resources: [
            .process("PrivacyInfo.xcprivacy")]
    ),
]
```

In this example, the package manifest lists the `Resources` directory as an explicit resource:

```swift
targets: [
    .target(
        name: "SomeLibrary",
        resources: [
            .process("Resources")]
    ),
]
```

If you distribute your binary framework as a Swift package, check that your XCFramework bundle includes a privacy manifest for each platform that you support. For more information, see [`Distributing binary frameworks as Swift packages`](https://developer.apple.com/documentation/Xcode/distributing-binary-frameworks-as-swift-packages).

##### Distribute Your Static Library with a Privacy Manifest

A static library is an archive of object files with a `.a` file extension. It doesn’t support resources such as the privacy manifest. If you currently distribute your SDK as a static library and want to update it to include a privacy manifest in Xcode, create a new static framework target that includes all your static library’s source files and resources, then add the privacy manifest to the target’s resource. For more information on how to create a static framework, see [`Creating a static framework`](https://developer.apple.com/documentation/Xcode/creating-a-static-framework).

If you don’t use Xcode to build your static library, create a static framework bundle for your static library manually, then add the privacy manifest to the bundle as a resource. For more information about framework bundle structure, see [`Placing content in a bundle`](placing-content-in-a-bundle.md). To identify the privacy manifest location in the static framework, see [`Add a privacy manifest to your framework`](adding-a-privacy-manifest-to-your-app-or-third-party-sdk#Add-a-privacy-manifest-to-your-framework.md).

##### Verify Your Xcframework Bundle Includes the Necessary Privacy Manifests

An XCFramework bundle is a binary package that can include multiple platform-specific variants of a framework or library. It supports distribution of Swift and C-based code. For more information about creating an XCFramework bundle, see [`Creating a multiplatform binary framework bundle`](https://developer.apple.com/documentation/Xcode/creating-a-multi-platform-binary-framework-bundle).

After adding a privacy manifest to your framework, consider distributing it as a signed XCFramework bundle. When you generate an XCFramework bundle with your framework, the generated bundle contains a privacy manifest file for each platform that your framework supports. The framework platform determines the location of the manifest file. When you sign your XCFramework bundle, developers who incorporate the framework can see whether updates to the framework have compatible code signatures. For more information, see [`Verifying the origin of your XCFrameworks`](https://developer.apple.com/documentation/Xcode/verifying-the-origin-of-your-xcframeworks).

After an update, `SampleFramework` supports iOS, iOS Simulator, Mac Catalyst, and macOS. The `MyArchives` directory contains archives of each variant of `SampleFramework`. Running the following command in Terminal creates an XCFramework with variants for iOS, iOS Simulator, Mac Catalyst, and macOS:

```swift
xcodebuild -create-xcframework 
-archive MyArchives/SampleFramework-iOS.xcarchive -framework SampleFramework.framework
-archive MyArchives/SampleFramework-macOS.xcarchive -framework SampleFramework.framework
-archive MyArchives/SampleFramework-iOS_Simulator.xcarchive -framework SampleFramework.framework 
-archive MyArchives/SampleFramework-Mac_Catalyst.xcarchive -framework SampleFramework.framework 
-output xcframeworks/SampleFramework.xcframework
```

Each variant of `SampleFramework` contains a privacy manifest file at the appropriate location, as shown below:

```swift
SampleFramework.xcframework/
    Info.plist
    ios-arm64/
       dSYMs/
           ...
       SampleFramework.framework/
           Info.plist
           SampleFramework
           PrivacyInfo.xcprivacy 
           ...
    macos-arm64_x86_64/
        dSYMs/
            ...
        SampleFramework.framework/
            SampleFramework -> Versions/Current/SampleFramework
            Resources -> Versions/Current/Resources
            Versions/
                Current -> A
                A/
                    SampleFramework
                    Resources/
                        Info.plist
                        PrivacyInfo.xcprivacy
                    ...
            ...
    ios-arm64_x86_64-simulator/
        dSYMs/
            ...
        SampleFramework.framework/
            Info.plist
            SampleFramework
            PrivacyInfo.xcprivacy 
            ...
    ios-arm64_x86_64-maccatalyst/
        dSYMs/
           ...
        SampleFramework.framework/
            SampleFramework -> Versions/Current/SampleFramework
            Resources -> Versions/Current/Resources
            Versions/
                Current -> A
                A/
                    SampleFramework
                    Resources/
                        Info.plist 
                        PrivacyInfo.xcprivacy
                    ...
            ...
```

To identify the privacy manifest location in frameworks, see [`Add a privacy manifest to your framework`](adding-a-privacy-manifest-to-your-app-or-third-party-sdk#Add-a-privacy-manifest-to-your-framework.md). To ship your static library with a privacy manifest, see [`Distribute your static library with a privacy manifest`](adding-a-privacy-manifest-to-your-app-or-third-party-sdk#Distribute-your-static-library-with-a-privacy-manifest.md).

##### Locate an Invalid Privacy Manifest in Your App Archive

To find an invalid privacy manifest in your app archive:

1. Gather the location of the file from the email you received from Apple.
2. In Xcode, choose Window > Organizer, then click Archives.
3. Control-click your app archive in the organizer, and choose Show in Finder from the contextual menu. Xcode opens the Finder to the location of your archive.
4. In the Finder, control-click your archive, and choose Show Package Contents to open it.
5. Navigate to the location of the privacy manifest in your archive.

##### Managing an Invalid Privacy Manifest

If you’re unable to obtain a valid privacy manifest from a third-party SDK developer and need to submit your app, locate the invalid privacy manifest in your app archive, delete it, and submit your archive using Xcode. Alternatively, locate the invalid privacy manifest in your app, fix the validation issues in the file, and submit your archive using Xcode. To troubleshoot invalid privacy manifests, see [`TN3181: Debugging an invalid privacy manifest`](https://developer.apple.com/documentation/Technotes/tn3181-debugging-invalid-privacy-manifest).

> ❗ **Important**: Removing or modifying the invalid privacy manifest breaks the archived app’s signature. Xcode will re-sign your app when you distribute your archive from the Archives organizer. For more information, see “Select a method for distribution,” in [`Distributing your app for beta testing and releases`](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases).

## See Also

- [Describing data use in privacy manifests](describing-data-use-in-privacy-manifests.md)
  Declare the data collected by your app or by third-party SDKs.
- [Describing use of required reason API](describing-use-of-required-reason-api.md)
  Ensure your use of covered API is consistent with policy.
- [App Privacy Configuration](app-privacy-configuration.md)
  A data structure that represents the root object in a privacy manifest file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)*
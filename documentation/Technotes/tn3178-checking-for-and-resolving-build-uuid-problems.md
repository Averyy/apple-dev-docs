# TN3178: Checking for and resolving build UUID problems

**Framework**: Technotes

Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.

#### Overview

Mach-O is the executable image format on Apple platforms.  A Mach-O image is a Mach-O file that the system can load and execute without further processing.  This includes executables, frameworks, dynamic libraries, and bundles.

> **Note**: Mach-O images have nothing to do with images in the more general sense, like PNG files.

A Mach-O image should contain a UUID that identifies the image.  This build UUID is vital to various subsystems.  For example, the build UUID connects an image to its debug symbol (`dSYM`) file, as explained in [`Building your app to include debugging information`](https://developer.apple.com/documentation/Xcode/building-your-app-to-include-debugging-information) and [`Adding identifiable symbol names to a crash report`](https://developer.apple.com/documentation/Xcode/adding-identifiable-symbol-names-to-a-crash-report).

Most Mach-O images are created by the Apple linker (`ld`).  If you use Xcode, it invokes the Apple linker as part of its build process.  The Apple linker sets the build UUID to a unique value, so most developers never run into build UUID problems.  However, you might run into problems if:

- Your Mach-O image has no build UUID.
- You use the same Mach-O executable for multiple apps.

This technote explains how to investigate and resolve such problems.

#### Display the Build Uuid

To view a Mach-O image’s build UUID, run the `dwarfdump` command with the `--uuid` option:

```shell
% dwarfdump --uuid /usr/bin/true 
UUID: E3F22F87-0B68-3B06-A845-8402D70B8FE9 (x86_64) /usr/bin/true
UUID: B6A1C19C-94AC-3659-AD62-BDF1839A8683 (arm64e) /usr/bin/true
```

In a universal binary each architecture has its own build UUID.

Alternatively, run the `otool` command to display the `LC_UUID` load command:

```shell
% otool -l -arch x86_64 /usr/bin/true | grep -B 1 -A 2 LC_UUID 
Load command 8
     cmd LC_UUID
 cmdsize 24
    uuid E3F22F87-0B68-3B06-A845-8402D70B8FE9
```

> **Note**: To learn more about these tools, see the UNIX online manual, known as .  For information on how to access that documentation, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

By default the Apple linker sets the build UUID based on a hash of the built code.  This promotes reproducible builds.

> **Note**: The central idea of reproducible builds is that the same source code built with the same tools and settings should produce the same binary.  Apple tools strive to support reproducible builds within the constraints imposed by the Mach-O file format.  That’s why the linker generates a hash-based UUID by default.

The `-random_uuid` option tells the linker to generate a random build UUID.  This is rarely used; see the `ld` man page for more about it.

The `-no_uuid` option tells the linker to add no build UUID.  The next section explains why this is a bad idea.

There’s no Apple command to explicitly set a Mach-O image’s build UUID after the fact.

If a Mach-O image is signed, that signature covers the build UUID.

#### Ensure Each Mach O Image Has a Build Uuid

Every Mach-O image should have a build UUID.  While it’s possible to create an image without a UUID, this is almost always a bad idea:

- An image without a build UUID might encounter problems during development.  For example, Apple’s crash reporter can’t symbolicate an address in an image that has no UUID.
- A Mach-O executable without a build UUID might encounter weird problems at runtime, for example, when it interacts with the network subsystem.

If you suspect that your Mach-O image is missing its build UUID, run `dwarfdump` to check for its presence.  See the previous section for an example of how to do this.

If that confirms that your Mach-O image is in fact missing its build UUID, investigate how the image was created.  There are two common cases:

- If you created the image with the Apple linker, check to see if the link command includes the `-no_uuid` option.  If it does, remove that option.
- Some third-party tools create Mach-O images without a build UUID.  If you’re using third-party tooling, consult its documentation for advice on how to configure it to add a UUID.

#### Use Unique Build Uuids

Each distinct Mach-O image must have its own unique build UUID.

Consider one of the critical use cases for build UUIDs, namely symbolication.  If two different Mach-O images had the same build UUID, you wouldn’t be able to match up an image with the correct debug symbol (`dSYM`) file.

Normally this isn’t a problem because both UUID generation approaches described above—hash-based UUIDs and random UUIDs—result in a unique build UUID.  However, there’s a subtlety around the concept of .

Imagine you ship a dynamic library that’s embedded in multiple apps.  Each copy of this library has the same build UUID, and that’s absolutely fine.

Things get trickier when it comes to apps.  Imagine you’re shipping multiple apps based on the same code.  For example, you might have a  and a  variant of your app built from the same code, or you might have a single app that you reskin for multiple clients.

By definition, each app has a unique bundle ID; the bundle ID is the primary mechanism used to distinguish between different apps.  However, some OS subsystems use a process’s main executable UUID—the build UUID of the Mach-O executable that the process is running—as a shortcut to identify the app.  If you have two apps with different bundle IDs and the same main executable UUID, you might encounter weird problems with those subsystems.  For example, the network subsystem might apply constraints for one of your apps to the other app (r. 30421029).

Normally this isn’t a problem because every app is built from different source code, which produces different built code, which hashes to a different UUID.  You run into problems when you use exactly the same code to build your app, or you build your app’s executable once and then reskin it by changing just resources.

If you encounter weird problems after installing two variants of your app on the same device, especially when it comes to the network subsystem, check that the main executable of each app has a different build UUID.  Use `dwarfdump` for this, as explained earlier.

#### Force a Unique Main Executable Uuid

If `dwarfdump` reveals that two of your apps have the same main executable UUID, fix that before distributing your apps.  How you do that depends on how your app is built.

The easiest fix is to build both apps from source code.  Typically, the linker assigns each app a unique build UUID because:

- Most apps contain some Swift code.
- In Swift, the name mangling includes the module name.
- The module name defaults to the app name, which is different for each app.

> **Note**: In Xcode, use the [`Build settings reference`](https://developer.apple.com/documentation/Xcode/build-settings-reference) to change the module name.  It defaults to the app name, with any unrepresentable characters, such as space, replaced by underscore (`_`).

If that doesn’t resolve the issue, add some unique code to each app.

Once you’re done, run `dwarfdump` to confirm that you’ve achieved your ultimate goal of giving each app a unique main executable UUID.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3178-checking-for-and-resolving-build-uuid-problems)*
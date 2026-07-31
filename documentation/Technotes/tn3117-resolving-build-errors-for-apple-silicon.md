# TN3117: Resolving architecture build errors on Apple silicon

**Framework**: Technotes

Update your app’s architecture build settings to support building macOS, iOS, watchOS, and tvOS apps on Apple silicon.

#### Overview

Xcode’s default architecture build settings provide the recommended combinations of CPU architectures to ship your app to all supported devices on each of Apple’s platforms.

| Name | Build Setting | Default Value |
| --- | --- | --- |
| Architectures | `ARCHS` | `$(ARCHS_STANDARD)` |
| Build Active Architectures Only | `ONLY_ACTIVE_ARCH` | `Yes` for Debug configurations, `No` for Release configurations |
| Excluded Architectures | `EXCLUDED_ARCHS` | No value |
| Valid Architectures | `VALID_ARCHS` | All supported architectures for the platform (Deprecated setting) |

For an overview of each of these build settings, see the [`Build settings reference`](https://developer.apple.com/documentation/Xcode/build-settings-reference).

By keeping your architecture build settings set to these default values, you’ll automatically build with the latest recommended CPU architectures, which change as Apple’s platforms evolve. For example, a Mac app using the default architecture build settings automatically gains support for both Apple silicon and Intel-based Macs once built with Xcode 12.2 or later.

When you add a Mac with Apple silicon to your development team, you may find that your app builds with errors due to deviations from the default architecture build settings, or due to pre-built libraries that haven’t been updated to support Apple silicon. Some examples of these errors:

```None
error: The armv7 architecture is deprecated. You should update your ARCHS build
setting to remove the armv7 architecture. 
```

```None
warning: None of the architectures in ARCHS (arm64) are valid. Consider setting
ARCHS to $(ARCHS_STANDARD) or updating it to include at least one value from
VALID_ARCHS (arm64, arm64e, armv7, armv7s) which is not in
EXCLUDED_ARCHS (arm64).
```

```None
No architectures to compile for

```

```None
<AppName>'s architectures (<Xcode Target Architecture>) include none that the
<iOS Simulator or Device Name> can execute (<Run Destination Architecture>)
```

```None
Missing 64-bit support. iOS apps uploaded to App Store Connect must
include 64-bit support.
```

If you receive any of those error messages, the combination of values set in `ARCHS`, `VALID_ARCHS`, and `EXCLUDED_ARCHS` prevented the build from having the necessary architectures. The first step in resolving the build error is to reset each of these build settings back to their default value for every target in your app. See [`Configuring the build settings of a target`](https://developer.apple.com/documentation/Xcode/configuring-the-build-settings-of-a-target) for how to modify build settings, and [`Unset Valid Architectures`](tn3117-resolving-build-errors-for-apple-silicon#Unset-Valid-Architectures.md) for special considerations when resetting `VALID_ARCHS`.

Once these build settings are reset back to their default values, build your app to see if the build succeeds. If your build still completes with errors, use the information in the remainder of this article to resolve those errors. If you are building a Mac app, also consult [`Building a universal macOS binary`](https://developer.apple.com/documentation/Apple-Silicon/building-a-universal-macos-binary) for additional information on resolving build issues unique to Mac apps.

#### Unset Valid Architectures

Xcode 12 deprecated the `VALID_ARCHS` build setting, and moved it from the Architectures build settings group to the User-Defined build settings group. All targets overriding this setting should completely remove the override from the Xcode project by looking at the User-Defined group of build settings.

![Xcode’s build settings with ](https://docs-assets.developer.apple.com/published/c9d391e3a5b8b52b1bf4c2b1e611fc75/tn3117-valid-archs%402x.png)

To remove this setting from a target, use the Delete key to remove it. Once `VALID_ARCHS` is no longer set for a target, it will disappear from the User-Defined build setting group.

> **Note**: Ensure you completely remove `VALID_ARCHS` by using the Delete key. Do not change its value to an empty value, leaving the setting visible in the User-Defined group.

If `VALID_ARCHS` was intentionally preventing a target from building for a specific architecture, modify the `EXCLUDED_ARCHS` build setting as needed to achieve the same results as before.

#### Exclude Architectures Sparingly

Strive for your app, including all of its pre-compiled libraries, to always build for the complete set of architectures defined by the default value of the `ARCHS` build setting. Only use the `EXCLUDED_ARCHS` build setting on targets where the final released app is not using the target’s functionality on a specific architecture, such as a Mac app that only supports a legacy feature on Intel-based Mac computers. Do not modify the `ARCHS` build setting to achieve the same result.

#### Update Pre Compiled Libraries with Apple Silicon Support

Apps for iOS, watchOS, and tvOS that depend on pre-compiled libraries not updated to support the simulator on Apple silicon will encounter one of these build errors:

```None
building for iOS Simulator, but linking in object file built for iOS,
for architecture arm64
```

```None
note: 'Example.xcframework' is missing architecture(s) required by this target
(arm64), but may still be link-compatible. (in target 'ExampleApp' from project
'ExampleApp')
```

If the library named in the error message is from a vendor, see [`Update pre-compiled libraries from vendors`](tn3117-resolving-build-errors-for-apple-silicon#Update-pre-compiled-libraries-from-vendors.md). If you have source code for the library, rebuild the library as an XCFramework with support for the simulator on Apple silicon. To learn how to build an XCFramework, see [`Creating a multiplatform binary framework bundle`](https://developer.apple.com/documentation/Xcode/creating-a-multi-platform-binary-framework-bundle).

> ❗ **Important**: To resolve these errors, either rebuild the library or follow the advice in [`Update pre-compiled libraries from vendors`](tn3117-resolving-build-errors-for-apple-silicon#Update-pre-compiled-libraries-from-vendors.md). Don’t launch Xcode using Rosetta to resolve these errors.

If you’re developing a watchOS app, all XCFrameworks for your watchOS app must contain `arm64` or `x86_64` libraries built specifically for the watchOS simulator. If you need to test your watchOS app specifically using the `i386` architecture with the watchOS simulator, use an Intel-based Mac.

> **Note**: A pre-compiled library must be built as an XCFramework to separate the device and simulator builds. Combining architectures for iOS, watchOS, or tvOS and their respective simulators into a single binary file is not supported.

##### Update Pre Compiled Libraries From Vendors

If the library producing the build error is a pre-compiled library from a vendor and you don’t have the source code, contact the vendor for an updated XCFramework supporting Apple silicon. If an update isn’t available from the vendor, temporarily use the `EXCLUDED_ARCHS` build setting to exclude `arm64` for the simulator SDK as shown in the figure below. Do not exclude `arm64` for any other SDK.

![Xcode’s build settings with ](https://docs-assets.developer.apple.com/published/569d1af9b27571ba97ee33855f112f35/tn3117-excluded-archs-simulator%402x.png)

After temporarily changing `EXCLUDED_ARCHS`, select the appropriate simulator destinations through the Product > Destination > Destination Architectures menu, and choose Show Rosetta Destinations. Once the library is updated with Apple silicon support and `EXCLUDED_ARCHS` is unset, choose Show Apple Silicon Destinations from the same menu. These menu items are available starting with Xcode 14.3.

![Xcode’s menu for displaying simulator destinations](https://docs-assets.developer.apple.com/published/8d098b22ef97e0e2d162cefe9eec7986/tn3117-destination_archs%402x.png)

> ❗ **Important**: Always contact the library vendor to request an updated library supporting the simulator on Apple silicon. Modifications to the `EXCLUDED_ARCHS` build setting for a simulator SDK are not a replacement for getting an updated library, and should only be used while waiting for the vendor to make an updated library available. Remove the changes to `EXCLUDED_ARCHS` after receiving the updated library.

#### Revision History

- **2026-03-11** Updated the text of the error messages.
- **2023-04-11** Added information about the Destination Architectures menu in Xcode 14.3.
- **2022-10-11** Updated link about creating XCFrameworks.
- **2022-07-12** Added additional information on excluding architectures.
- **2022-05-24** Made minor editorial changes.
- **2022-02-22** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3117-resolving-build-errors-for-apple-silicon)*
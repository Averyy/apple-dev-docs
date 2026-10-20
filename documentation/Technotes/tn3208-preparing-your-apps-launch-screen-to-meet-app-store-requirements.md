# TN3208: Preparing your app’s launch screen to meet App Store requirements

**Framework**: Technotes  
**Role**: Technote

Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.

#### Overview

A [launch screen](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens) appears instantly when your app starts up and is quickly replaced with your app’s first screen, giving the impression that your app is fast and responsive.

Starting in iOS 27 and iPadOS 27, App Store Connect requires your app to include a launch screen configuration in its `Info.plist`. This applies to both iPhone and iPad apps distributed through the App Store and alternative app marketplaces. If your app already includes a launch screen, you don’t need to make any changes.

A launch screen supports modern system features like multitasking and dynamic resizing. To learn about supporting resizable scenes, see [TN3192: Migrating your app from the deprecated UIRequiresFullScreen key](./tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md).

#### Understand the App Store submission requirement

When you upload an app built with the iOS 27 SDK or later, App Store Connect validates that your app’s `Info.plist` contains at least one of the following keys:

- [`UILaunchStoryboardName`](../BundleResources/information-property-list/uilaunchstoryboardname.md)
- [`UILaunchStoryboards`](../BundleResources/information-property-list/uilaunchstoryboards.md)
- [`UILaunchScreen`](../BundleResources/information-property-list/uilaunchscreen.md)
- [`UILaunchScreens`](../BundleResources/information-property-list/uilaunchscreens.md)

If none of these keys are present, App Store Connect rejects the upload with the following error:

```
ITMS-90870: Missing launch screen. Apps built with the iOS 27 SDK or later must provide a launch screen using an Xcode storyboard or UILaunchScreen. 
Make sure the Info.plist contains one of the following keys: UILaunchStoryboardName, UILaunchStoryboards, UILaunchScreen, UILaunchScreens. 
For details, visit: https://developer.apple.com/documentation/technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.
```

#### Add a launch screen to your app

Add the [`UILaunchScreen`](../BundleResources/information-property-list/uilaunchscreen.md) key to your app’s `Info.plist` to configure a launch screen. Xcode includes this key by default in new SwiftUI projects when the `Generate Info.plist File` and `Launch Screen (Generation)` build settings are enabled.

If you need a custom layout, use a launch screen storyboard instead.

To learn about configuring your app’s launch screen, see [Specifying your app’s launch screen](../Xcode/specifying-your-apps-launch-screen.md).

#### Verify your launch screen

To verify your launch screen, delete the app from the device or Simulator, then build and run. Your launch screen should appear briefly before your app’s first screen loads.

If you see a blank screen, an outdated launch screen, or no launch screen at all, see [TN3118: Debugging your app’s launch screen](./tn3118-debugging-your-apps-launch-screen.md) for troubleshooting steps.

#### Revision History

- **2026-09-14** Updated the ITMS-90870 error message to reflect the iOS 27 launch screen requirement.
- **2026-06-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements)*
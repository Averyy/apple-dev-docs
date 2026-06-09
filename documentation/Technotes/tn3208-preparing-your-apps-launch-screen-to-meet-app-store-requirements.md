# TN3208: Preparing your app’s launch screen to meet App Store requirements

**Framework**: Technotes

Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.

#### Overview

A [`launch screen`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens) appears instantly when your app starts up and is quickly replaced with your app’s first screen, giving the impression that your app is fast and responsive.

Starting in iOS 27 and iPadOS 27, App Store Connect requires your app to include a launch screen configuration in its `Info.plist`. This applies to both iPhone and iPad apps distributed through the App Store and alternative app marketplaces. If your app already includes a launch screen, you don’t need to make any changes.

A launch screen supports modern system features like multitasking and dynamic resizing. To learn about supporting resizable scenes, see [`TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key`](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md).

#### Understand the App Store Submission Requirement

When you upload an app built with the iOS 27 SDK or later, App Store Connect validates that your app’s `Info.plist` contains at least one of the following keys:

- [`UILaunchStoryboardName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchStoryboardName)
- [`UILaunchStoryboards`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchStoryboards)
- [`UILaunchScreen`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchScreen)
- [`UILaunchScreens`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchScreens)

If none of these keys are present, App Store Connect rejects the upload with the following error:

```None
ITMS-90870: Missing launch screen. Starting with the iOS 27 release this fall, 
apps built with the iOS 27 SDK or later must provide a launch screen using an Xcode storyboard or UILaunchScreen. 
Make sure the Info.plist contains one of the following keys: UILaunchStoryboardName, UILaunchStoryboards, UILaunchScreen, UILaunchScreens. 
For details, visit: https://developer.apple.com/documentation/technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.
```

#### Add a Launch Screen to Your App

Add the [`UILaunchScreen`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchScreen) key to your app’s `Info.plist` to configure a launch screen. Xcode includes this key by default in new SwiftUI projects when the `Generate Info.plist File` and `Launch Screen (Generation)` build settings are enabled.

If you need a custom layout, use a launch screen storyboard instead.

To learn about configuring your app’s launch screen, see [`Specifying your app’s launch screen`](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen).

#### Verify Your Launch Screen

To verify your launch screen, delete the app from the device or Simulator, then build and run. Your launch screen should appear briefly before your app’s first screen loads.

If you see a blank screen, an outdated launch screen, or no launch screen at all, see [`TN3118: Debugging your app’s launch screen`](tn3118-debugging-your-apps-launch-screen.md) for troubleshooting steps.

#### Revision History

- **2026-06-08** First published.

## See Also

- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements)*
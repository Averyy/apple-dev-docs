# TN3108: Viewing the interface of your Swift code

**Framework**: Technotes

Learn how to navigate to the interface file of a Swift implementation file.

#### Overview

Xcode generates an interface file that includes all your source code’s internal and public declarations when using the Assistant editor, the Related Items, or the Navigate menu.

#### Using the Assistant Editor

1. In the project navigator, select your implementation file.
2. Choose Editor > Assistant.

The generated interface for your Swift code appears in the assistant editor on the right. ![View the interface file in Counterparts mode.](https://docs-assets.developer.apple.com/published/7b53f71925156e2819783e0f1ee8bb7c/tn3108-counterparts_grouping%402x.png)

#### Using the Related Items Button

1. In the project navigator, select your implementation file.
2. Click the Related Items icon in the [`editor`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev79c94bf05)’s jump bar.
3. In the menu that appears, choose Counterparts > [Filename] to view your interface file. ![choose Counterparts > Filename to view the interface file.](https://docs-assets.developer.apple.com/published/eb299040a3183302ed82b221d05d0ba9/tn3108-select_counterparts_filename%402x.png)

Alternatively, choose Generated Interface > [Filename] from the menu.

To navigate back to your implementation file, choose Original Source from the menu. ![choose Original Source to navigate back to the implementation file.](https://docs-assets.developer.apple.com/published/62a24b0a4d39bc57d5214a0fc49f1b68/tn3108-related_original_source%402x.png)

#### Using the Navigate Menu

In the project navigator, select your implementation file, then choose Navigate > Jump to Next Counterpart to view the interface file. ![Choose Jump to Next Counterpart to view the interface file.](https://docs-assets.developer.apple.com/published/5bfc2ba9e51989c723d220aba1819a81/tn3108-jump_next_counterpart%402x.png)

To navigate back to your implementation file, choose Navigate > Jump to Previous Counterpart or Navigate > Jump to Original Source [Filename]. ![Choose Navigate > Jump to Previous Counterpart to navigate back to the implementation file.](https://docs-assets.developer.apple.com/published/8bdc09981efd12c6dd5394c2c2b82189/tn3108-navigate_original_source%402x.png)

#### Revision History

- **2022-05-24** Made minor editorial changes.
- **2022-02-08** Republished as TN3108 with significant editorial changes.
- **2016-03-23** First published as QA1914.

## See Also

- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3108-viewing-the-interface-of-your-swift-code)*
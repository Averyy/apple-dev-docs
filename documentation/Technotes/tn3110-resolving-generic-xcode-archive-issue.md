# TN3110: Resolving generic Xcode archive issue

**Framework**: Technotes

Identify common configurations that cause a generic Xcode archive.

#### Overview

The Archives organizer reports your archive as an *app archive* if it contains a single top-level app and a *generic Xcode archive*, otherwise. ![A generic archive.](https://docs-assets.developer.apple.com/published/f2d93098ac3d94ad520da9f1b21631de/tn3110-generic_archive%402x.png) You can validate and distribute an app archive. A generic archive, which may contain unexpected items such as header files, static libraries, or frameworks, can’t be validated nor distributed.

#### Ensure the Skip Install Build Setting Is Properly Configured

The [`Skip Install (SKIP_INSTALL)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6) build setting determines whether to install built products within the archive.

When enabled for an app, Xcode doesn’t install the app within the archive. The produced archive doesn’t contain the single top-level app as expected. To generate an app archive, confirm that Skip Install is disabled for your app. ![Disable Skip Install for apps.](https://docs-assets.developer.apple.com/published/39807425f0be998c6e375b5ec168bbb5/tn3110-skip_install_apps%402x.png)

When disabled for an app’s dependencies such as frameworks, Xcode adds these dependencies to the app’s archive. The produced archive contains multiple folders rather than the expected single top-level app. To generate an app archive, confirm that Skip Install is enabled for all your app’s dependencies. ![Enable Skip Install for dependencies.](https://docs-assets.developer.apple.com/published/4375c94351bbdf54e470b42c78152fc3/tn3110-skip_install_dependencies%402x.png)

#### Use a Copy Files Build Phase

If your app links against static libraries, confirm that they all use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export their header files. The produced app archive contains header files when static libraries use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export these files.

#### Ensure the Installation Directory Build Setting Is Properly Configured

The [`Installation Directory (INSTALL_PATH)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6?sub=devabd541cd5) build setting specifies the directory where to install built products. It takes default values according to the product being built. To generate an app archive, confirm that Installation Directory is set to the default value such as `$(LOCAL_APPS_DIR)` for apps.

#### Revision History

- **2022-02-08** First published.

## See Also

- [TN3213: Moving from Multipeer Connectivity to Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md)
  Learn how to migrate your Multipeer Connectivity app to Network framework.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3110-resolving-generic-xcode-archive-issue)*
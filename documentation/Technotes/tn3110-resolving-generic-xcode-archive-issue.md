# TN3110: Resolving generic Xcode archive issue

**Framework**: Technotes

Identify common configurations that cause a generic Xcode archive.

#### Overview

The Archives organizer reports your archive as an  if it contains a single top-level app and a , otherwise. ![A generic archive.](https://docs-assets.developer.apple.com/published/f2d93098ac3d94ad520da9f1b21631de/tn3110-generic_archive%402x.png) You can validate and distribute an app archive. A generic archive, which may contain unexpected items such as header files, static libraries, or frameworks, can’t be validated nor distributed.

#### Ensure the Skip Install Build Setting Is Properly Configured

The [`Skip Install (SKIP_INSTALL)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6) build setting determines whether to install built products within the archive.

When enabled for an app, Xcode doesn’t install the app within the archive. The produced archive doesn’t contain the single top-level app as expected. To generate an app archive, confirm that Skip Install is disabled for your app. ![Disable Skip Install for apps.](https://docs-assets.developer.apple.com/published/39807425f0be998c6e375b5ec168bbb5/tn3110-skip_install_apps%402x.png)

When disabled for an app’s dependencies such as frameworks, Xcode adds these dependencies to the app’s archive. The produced archive contains multiple folders rather than the expected single top-level app. To generate an app archive, confirm that Skip Install is enabled for all your app’s dependencies. ![Enable Skip Install for dependencies.](https://docs-assets.developer.apple.com/published/4375c94351bbdf54e470b42c78152fc3/tn3110-skip_install_dependencies%402x.png)

#### Use a Copy Files Build Phase

If your app links against static libraries, confirm that they all use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export their header files. The produced app archive contains header files when static libraries use a [`Copy files`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev50bab713d) build phase to export these files.

#### Ensure the Installation Directory Build Setting Is Properly Configured

The [`Installation Directory (INSTALL_PATH)`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/itcaec37c2a6?sub=devabd541cd5) build setting specifies the directory where to install built products. It takes default values according to the product being built. To generate an app archive, confirm that Installation Directory is set to the default value such as `$(LOCAL_APPS_DIR)` for apps.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3110-resolving-generic-xcode-archive-issue)*
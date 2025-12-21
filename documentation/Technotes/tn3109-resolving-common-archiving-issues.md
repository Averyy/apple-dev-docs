# TN3109: Resolving common archiving issues

**Framework**: Technotes

Handle common issues that arise while archiving apps.

#### Overview

When you choose Product > Archive, Xcode creates an archive of your app that will appear in the Archives organizer. If the Archives organizer reports your archive as an app archive, then you can validate or distribute it.

#### The Archive Command in the Product Menu Is Disabled

You can choose Product > Archive in Xcode after meeting these requirements:

- You’ve selected a real device or build-only device as the run destination in the scheme building your app. Apps built with simulator SDKs can’t be archived nor submitted to the App Store; see [`Running Your App in the Simulator or on a Device`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/running-your-app-in-the-simulator-or-on-a-device).
- You’ve enabled the archive action for the scheme building your app. ![Select archive in the scheme editor.](https://docs-assets.developer.apple.com/published/e672b8476b44d40042786a3ed6f8211b/tn3109-archive_selected%402x.png)

#### Xcode Successfully Archived My App But the Archive Doesnt Appear in the Archives Organizer

Archives appear in the Archives organizer when meeting these requirements:

- Your archive is an app archive. If the Archives organizer reports your archive as generic, read [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md).
- You’ve selected the `Reveal Archive in Organizer` option in the archive action for the scheme building your app. ![Select Reveal Archive in Organizer in the scheme editor.](https://docs-assets.developer.apple.com/published/e6fce9da555706cdc1e23f0549d96c2b/tn3109-reveal_archive_in_organizer%402x.png)

#### The Validate Content Button Is Disabled

You have a generic Xcode archive. The Validate Content button is enabled for app archives and disabled for generic ones. ![The Validate Content button is disabled.](https://docs-assets.developer.apple.com/published/f7ae0549f618117d42cac721cf3a437e/tn3109-validate_content_disabled%402x.png) See [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md) for details.

#### Unexpected Build Products and Archive Methods in the Archive Organizer When Attempting to Distribute My Archive

If the Archives organizer offers to distribute your archive’s built product or to export a copy of it, then your archive is likely a generic one. ![Select Built Products or Archive in the Archives organizer.](https://docs-assets.developer.apple.com/published/7cac2c86a9f9c70ffc48feb4d8660dfc/tn3109-select_distribution_method%402x.png) Read [`TN3110: Resolving generic Xcode archive issue`](tn3110-resolving-generic-xcode-archive-issue.md) for information on how to resolve it.

#### Revision History

-  Made minor editorial changes.
-  Republished as TN3109 with significant editorial changes.
-  Updated for Xcode 7.
-  Updated for Xcode 7.
-  Made editorial changes.
-  Updated for Xcode 6.
-  Fixed typos.
-  Updated the “Unexpected Save Built Products and Export as Xcode Archive options in the Archives Organizer when attempting to distribute my archive” section.
-  Added information on how to resolve the Archives Organizer’s “Save Built Products” and “Export as Xcode Archive” issue.
-  First published as TN2215.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3109-resolving-common-archiving-issues)*
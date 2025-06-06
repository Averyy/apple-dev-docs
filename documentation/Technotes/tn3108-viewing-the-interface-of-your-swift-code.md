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

-  Made minor editorial changes.
-  Republished as TN3108 with significant editorial changes.
-  First published as QA1914.

## See Also

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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3108-viewing-the-interface-of-your-swift-code)*
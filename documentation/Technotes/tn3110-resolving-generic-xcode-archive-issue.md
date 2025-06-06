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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3110-resolving-generic-xcode-archive-issue)*
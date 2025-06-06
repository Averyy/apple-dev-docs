# TN3118: Debugging your app’s launch screen

**Framework**: Technotes

Understand why your app’s launch screen is not displayed or updated.

#### Overview

A [`Launch Screen`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens) appears instantly when your app starts up and is quickly replaced with the app’s first screen, giving the impression that your app is fast and responsive. As you upgrade your application’s launch screen you may discover that the old version still appears or that it appears empty. This article explains possible reasons and how to fix them.

#### Launch Screen Does Not Display Properly

Check why your launch screen fails to display:

-  Your new Xcode build has not overwritten the old launch screen. Clean your build folder for your project. In Xcode, select your target, then select the menu Product, menu item Clean Build Folder. Remove the app from device or Simulator. Build and run the app again.
-  When your app enters the background, iOS takes a snapshot of the app, and displays the snapshot on subsequent launches. If you want your launch screen to appear again, remove your app from the device, and run it again from Xcode.

For SwiftUI-based or UIKit-based apps that use a launch screen in its Information Property List:

- . It is missing the [`UILaunchScreen`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchScreen) key-value, or the [`UIImageName`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UILaunchScreen/UIImageName) key-value does match with the image name what is found in the asset catalog. Be aware that case sensitivity is important.

For UIKit-based apps using a Storyboard Launch Screen:

-  Select your Xcode target, goto the General tab, refer to the ‘App Icons and Launch Images’ section. The Launch Screen File setting should match the name of your launch screen storyboard found in the Project Navigator. To find out more about setting up your Launch Screen in Xcode, refer to [`Specifying your app’s launch screen`](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen).

![The launch screen file name setting.](https://docs-assets.developer.apple.com/published/99e629c2eb2362f16f1c0d263dcaf4f6/tn3118-launch_screen_file_setting%402x.png)

-  If you are using static images in your launch screen, check to make sure the image originates from the product’s asset catalog as a JPG or PNG image.
- . Xcode will warn you: “Warning: Unsupported Configuration: ‘View Controller’ is unreachable because it has no entry points”. Select the view controller scene in your launch screen storyboard. Make sure Is Initial View Controller is checked.

![The initial view controller setting.](https://docs-assets.developer.apple.com/published/7230defec45e5d8ceb5d8d971aef45f5/tn3118-initial_view_controller%402x.png)

> **Note**:  If you are using a 3rd party development environment that provides the launch screen for your app, contact that 3rd party support team for help.

#### App Launching with State Restoration

Implement state restoration in your app so that the launch screen is used less often. iOS snapshots your app when it’s suspended and may use this snapshot instead of the launch screen the next time the app is launched. Users expect your app to be in the same state as when they left it. For more information on state restoration refer to [`About the UI restoration process`](https://developer.apple.com/documentation/UIKit/about-the-ui-restoration-process).

#### Revision History

-  Fixed some broken links.
-  Made minor editorial changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3118-debugging-your-apps-launch-screen)*
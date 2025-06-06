# TN3115: Bluetooth State Restoration app relaunch rules

**Framework**: Technotes

Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.

#### Overview

Bluetooth State Restoration on iOS will relaunch an app in the background for pending Core Bluetooth requests. There are, though, certain conditions where the system will  relaunch and restore your app regardless of pending requests.

Because of user actions, it’s possible that an app may no longer be eligible to be restored in response to a Bluetooth event. Therefore it’s important to educate the users of your app, so that they understand how their actions affect the functionality of it.

Well designed apps will be resilient under such conditions.

| App or Device State | Will the app be relaunched? |
| --- | --- |
| App suspended in memory | (see note 1) |
| App removed from memory |  |
| App crashed |  |
| App Force Quit by the user |  |
| Bluetooth power toggled | (see note 2) |
| Airplane Mode toggled | (see note 3) |
| Device restarted | (see note 4) |

Notes:

1. App will be activated without needing a relaunch.
2. Users may toggle Bluetooth power through Settings, Control Center, or via Airplane mode.
3. Only if Bluetooth power is not toggled with Airplane Mode. Users may configure the Airplane Mode switch to not toggle Bluetooth power.
4. If the device requires a passcode to unlock, apps will not be relaunched until the device is unlocked for the first time after a restart.

Also, it’s important to keep in mind that your app will be relaunched and restored  it’s waiting for a specific Bluetooth event or action (like scanning, connecting, or a subscribed notification characteristic, and for peripheral apps, actively advertising), and the corresponding Bluetooth event has occurred.

For more information on Bluetooth State Preservation and Restoration refer to [`State Preservation and Restoration`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html#//apple_ref/doc/uid/TP40013257-CH7-SW10) in [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257-CH1-SW1)

#### Revision History

-  Republished as TN3115. Made clarifications to the document.
-  First published as QA1962.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3115-bluetooth-state-restoration-app-relaunch-rules)*
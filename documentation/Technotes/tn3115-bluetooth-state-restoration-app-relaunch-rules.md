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
| App Force Quit by the user | (see note 5) |
| Bluetooth power toggled | (see note 2) |
| Control Center Bluetooth button toggled | (see note 5) |
| Airplane Mode toggled | (see note 3) |
| Device restarted | (see note 4) |

Notes:

1. App will be activated without needing a relaunch.
2. Users may toggle Bluetooth power through Settings
3. Only if Bluetooth is not toggled with Airplane Mode. Users may configure the Airplane Mode switch to not toggle Bluetooth. Also, see note 5.
4. If the device requires a passcode to unlock, apps will not be relaunched until the device is unlocked for the first time after a restart.
5. Starting in iOS 26 and iPadOS 26, only apps that use [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) to setup Bluetooth accessories will be relaunched.

Also, it’s important to keep in mind that your app will be relaunched and restored  it’s waiting for a specific Bluetooth event or action (like scanning, connecting, or a subscribed notification characteristic, and for peripheral apps, actively advertising), and the corresponding Bluetooth event has occurred.

For more information on Bluetooth State Preservation and Restoration refer to [`State Preservation and Restoration`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html#//apple_ref/doc/uid/TP40013257-CH7-SW10) in [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257-CH1-SW1)

#### Revision History

-  Updated for iOS 26 and iPadOS 26.
-  Republished as TN3115. Made clarifications to the document.
-  First published as QA1962.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3115-bluetooth-state-restoration-app-relaunch-rules)*
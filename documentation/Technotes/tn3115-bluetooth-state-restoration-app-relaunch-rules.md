# TN3115: Bluetooth State Restoration app relaunch rules

**Framework**: Technotes

Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.

#### Overview

Bluetooth State Restoration on iOS will relaunch an app in the background for pending Core Bluetooth requests. There are, though, certain conditions where the system will **not** relaunch and restore your app regardless of pending requests.

Because of user actions, it’s possible that an app may no longer be eligible to be restored in response to a Bluetooth event. Therefore it’s important to educate the users of your app, so that they understand how their actions affect the functionality of it.

Well designed apps will be resilient under such conditions.

| App or Device State | Will the app be relaunched? |
| --- | --- |
| App suspended in memory | (see note 1) |
| App removed from memory | **Yes** |
| App crashed | **Yes** |
| App Force Quit by the user | **No** (see note 5) |
| Bluetooth power toggled | **No** (see note 2) |
| Control Center Bluetooth button toggled | **Yes** (see note 5) |
| Airplane Mode toggled | **Yes** (see note 3) |
| Device restarted | **Yes** (see note 4) |

Notes:

1. App will be activated without needing a relaunch.
2. Users may toggle Bluetooth power through Settings
3. Only if Bluetooth is not toggled with Airplane Mode. Users may configure the Airplane Mode switch to not toggle Bluetooth. Also, see note 5.
4. If the device requires a passcode to unlock, apps will not be relaunched until the device is unlocked for the first time after a restart.
5. Starting in iOS 26 and iPadOS 26, only apps that use [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit) to setup Bluetooth accessories will be relaunched.

Also, it’s important to keep in mind that your app will be relaunched and restored **if and only if** it’s waiting for a specific Bluetooth event or action (like scanning, connecting, or a subscribed notification characteristic, and for peripheral apps, actively advertising), and the corresponding Bluetooth event has occurred.

For more information on Bluetooth State Preservation and Restoration refer to [`State Preservation and Restoration`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothBackgroundProcessingForIOSApps/PerformingTasksWhileYourAppIsInTheBackground.html#//apple_ref/doc/uid/TP40013257-CH7-SW10) in [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257-CH1-SW1)

#### Revision History

- **2025-09-15** Updated for iOS 26 and iPadOS 26.
- **2022-02-08** Republished as TN3115. Made clarifications to the document.
- **2017-09-08** First published as QA1962.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3115-bluetooth-state-restoration-app-relaunch-rules)*
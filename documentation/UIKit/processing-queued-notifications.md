# Processing queued notifications

**Framework**: UIKit

Respond to notifications when coming out of the suspended state.

#### Overview

When settings or device conditions change, the system generates notifications so that apps can respond accordingly. These notifications are delivered immediately to apps that are running, but their delivery is delayed for apps that are suspended. For a suspended app, pending notifications are delivered as soon after the app begins running again (either in the foreground or in the background).

The following table lists the notifications that apps can receive after they start running again. You must explicitly add an observer to these notifications to receive them. The system coalesces multiple related notifications so that the app receives only one notification with the net changes.

| Event | Notifications |
| --- | --- |
| The user changed your app’s preferences | [`didChangeNotification`](https://developer.apple.com/documentation/Foundation/UserDefaults/didChangeNotification) |
| The current language or locale settings changed | [`currentLocaleDidChangeNotification`](https://developer.apple.com/documentation/Foundation/NSLocale/currentLocaleDidChangeNotification) |
| The screen mode of a display changes | [`modeDidChangeNotification`](uiscreen/modedidchangenotification.md) |
| An external display is connected or disconnected | [`didConnectNotification`](uiscreen/didconnectnotification.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`didDisconnectNotification`](uiscreen/diddisconnectnotification.md) |
| An accessory is connected or disconnected | [`EAAccessoryDidConnect`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/EAAccessoryDidConnect) (Swift) or [`EAAccessoryDidConnectNotification`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryDidConnectNotification) (Objective-C) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`EAAccessoryDidDisconnect`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/EAAccessoryDidDisconnect) (Swift) or [`EAAccessoryDidDisconnectNotification`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryDidDisconnectNotification) (Objective-C) |
| The status of the user’s iCloud account changed | [`NSUbiquityIdentityDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSUbiquityIdentityDidChange) |
| The device orientation changed | [`orientationDidChangeNotification`](uidevice/orientationdidchangenotification.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (UIKit automatically updates the interface orientation of your view controllers when appropriate.) |
| There was a significant time change | [`significantTimeChangeNotification`](uiapplication/significanttimechangenotification.md) |
| The battery level or battery state changed | [`batteryLevelDidChangeNotification`](uidevice/batteryleveldidchangenotification.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`batteryStateDidChangeNotification`](uidevice/batterystatedidchangenotification.md) |
| The device’s proximity to the user changed | [`proximityStateDidChangeNotification`](uidevice/proximitystatedidchangenotification.md) |

When a suspended app starts running again, the system delivers any queued notifications on the app’s main thread before it delivers any touch events or user input. Handle all notifications as quickly as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/processing-queued-notifications)*
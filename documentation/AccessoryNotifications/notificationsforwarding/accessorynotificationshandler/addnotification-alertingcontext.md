# addNotification(_:alertingContext:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Provides a new notification for display on your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func addNotification(_ notification: AccessoryNotification, alertingContext: AlertingContext) async throws -> Bool
```

#### Return Value

`true` if the accessory alerted for the notification, `false` otherwise. If this method throws an error, the system assumes the accessory did not alert.

#### Discussion

Parse the notification details, select the information to display on your accessory, and convert it to data for transmission. Return `true` if your accessory successfully alerts for the notification.

## Parameters

- `notification`: The notification to add.
- `alertingContext`: Context for evaluating whether the notification can alert or be delivered quietly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:))*
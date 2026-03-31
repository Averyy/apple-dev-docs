# addNotification(_:alertingContext:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Called when a notification has been added.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func addNotification(_ notification: AccessoryNotification, alertingContext: AlertingContext) async throws -> Bool
```

#### Return Value

`true` if the accessory alerted for the notification, `false` otherwise. If this method throws an error, the system assumes the accessory did not alert for the notification.

## Parameters

- `notification`: The notification that was added.
- `alertingContext`: The context to use to evaluate whether a notification should alert or be delivered quietly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:))*
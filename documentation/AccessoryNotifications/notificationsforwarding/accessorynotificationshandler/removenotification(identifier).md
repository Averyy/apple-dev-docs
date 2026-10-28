# removeNotification(identifier:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes a previously-posted notification from your accessory.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func removeNotification(identifier: AccessoryNotification.Identifier)
```

## Discussion

The system calls this method when a notification needs to be removed, such as when a person dismisses it on another device or when the person deletes the app that sent the notification.

## Parameters

- `identifier`: The identifier of the notification to remove.

## See Also

### Removing notifications
- [func removeAllNotifications()](./removeallnotifications%28%29.md)
  Removes all notifications from the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/removenotification(identifier:))*
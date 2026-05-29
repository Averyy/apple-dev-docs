# AccessoryError.coordinationTimeout

**Framework**: Accessory Notifications  
**Kind**: case

An error that indicates alert coordination timed out.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case coordinationTimeout
```

#### Discussion

The system sets a timeout to determine whether an accessory successfully alerts for a notification. The system generates this error if your accessory doesn’t return from [`addNotification(_:alertingContext:)`](notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:).md) within the timeout.

## See Also

- [AccessoryError.invalidNotificationResponse](accessoryerror/invalidnotificationresponse.md)
  An error that indicates the system failed to handle a notification response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror/coordinationtimeout)*
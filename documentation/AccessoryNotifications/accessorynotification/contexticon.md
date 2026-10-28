# contextIcon

**Framework**: Accessory Notifications  
**Kind**: property  
**Role**: Instance Property

A secondary icon that provides additional contextual information about the notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
let contextIcon: AccessoryNotification.File?
```

## Discussion

For communication notifications, this image might be a message sender’s avatar or group chat icon.

## See Also

### Accessing related media
- [let attachments: [AccessoryNotification.File]](./attachments.md)
  An array of files sent with the notification.
- [let sourceIcon: AccessoryNotification.File?](./sourceicon.md)
  An icon that represents the app that sent the notification.
- [AccessoryNotification.File](./file.md)
  A file associated with a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/contexticon)*
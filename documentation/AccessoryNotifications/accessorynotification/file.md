# AccessoryNotification.File

**Framework**: Accessory Notifications  
**Kind**: struct

A file associated with a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct File
```

#### Overview

The [`AccessoryNotification`](accessorynotification.md) structure’s [`attachments`](accessorynotification/attachments.md), [`sourceIcon`](accessorynotification/sourceicon.md), and [`contextIcon`](accessorynotification/contexticon.md) properties use this type.

## Topics

### Accessing file data
- [var url: URL](accessorynotification/file/url.md)
  A URL that locates the file’s data.
### Determining the file type
- [var type: UTType](accessorynotification/file/type.md)
  A uniform type identifier for the file.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)

## See Also

- [let attachments: [AccessoryNotification.File]](accessorynotification/attachments.md)
  An array of files sent with the notification.
- [let sourceIcon: AccessoryNotification.File?](accessorynotification/sourceicon.md)
  An icon that represents the app that sent the notification.
- [let contextIcon: AccessoryNotification.File?](accessorynotification/contexticon.md)
  A secondary icon that provides additional contextual information about the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/file)*
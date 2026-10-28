# AccessoryNotification.File

**Framework**: Accessory Notifications  
**Kind**: struct  
**Role**: Structure

A file associated with a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct File
```

## Overview

The [`AccessoryNotification`](../accessorynotification.md) structure’s [`attachments`](./attachments.md), [`sourceIcon`](./sourceicon.md), and [`contextIcon`](./contexticon.md) properties use this type.

## Topics

### Accessing file data
- [var url: URL](./file/url.md)
  A URL that locates the file’s data.
### Determining the file type
- [var type: UTType](./file/type.md)
  A uniform type identifier for the file.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)

## See Also

### Accessing related media
- [let attachments: [AccessoryNotification.File]](./attachments.md)
  An array of files sent with the notification.
- [let sourceIcon: AccessoryNotification.File?](./sourceicon.md)
  An icon that represents the app that sent the notification.
- [let contextIcon: AccessoryNotification.File?](./contexticon.md)
  A secondary icon that provides additional contextual information about the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/file)*
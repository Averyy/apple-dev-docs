# FileHandle.ConnectionAcceptedMessage

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct ConnectionAcceptedMessage
```

## Topics

### Initializers
- [init(fileHandleItem: Result<FileHandle, POSIXError>)](filehandle/connectionacceptedmessage/init(filehandleitem:).md)
### Instance Properties
- [var fileHandleItem: Result<FileHandle, POSIXError>](filehandle/connectionacceptedmessage/filehandleitem.md)
### Type Methods
- [static func makeNotification(FileHandle.ConnectionAcceptedMessage) -> Notification](filehandle/connectionacceptedmessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage)*
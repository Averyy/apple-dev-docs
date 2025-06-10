# FileHandle.ReadCompletionMessage

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
struct ReadCompletionMessage
```

## Topics

### Initializers
- [init(dataItem: Result<Data, POSIXError>)](filehandle/readcompletionmessage/init(dataitem:).md)
### Instance Properties
- [var dataItem: Result<Data, POSIXError>](filehandle/readcompletionmessage/dataitem.md)
### Type Methods
- [static func makeNotification(FileHandle.ReadCompletionMessage) -> Notification](filehandle/readcompletionmessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [NotificationCenter.Message](notificationcenter/message.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readcompletionmessage)*
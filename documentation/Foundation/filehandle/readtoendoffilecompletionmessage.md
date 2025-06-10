# FileHandle.ReadToEndOfFileCompletionMessage

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
struct ReadToEndOfFileCompletionMessage
```

## Topics

### Initializers
- [init(dataItem: Result<Data, POSIXError>)](filehandle/readtoendoffilecompletionmessage/init(dataitem:).md)
### Instance Properties
- [var dataItem: Result<Data, POSIXError>](filehandle/readtoendoffilecompletionmessage/dataitem.md)
### Type Methods
- [static func makeNotification(FileHandle.ReadToEndOfFileCompletionMessage) -> Notification](filehandle/readtoendoffilecompletionmessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [NotificationCenter.Message](notificationcenter/message.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readtoendoffilecompletionmessage)*
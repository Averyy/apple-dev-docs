# messages(of:for:bufferSize:)

**Framework**: Foundation  
**Kind**: method

Returns an asynchronous sequence of messages produced by this center for a given subject and identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func messages<Identifier, Message>(of subject: Message.Subject, for identifier: Identifier, bufferSize limit: Int = 10) -> some Sendable & AsyncSequence<Message, Never> where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType, Message.Subject : AnyObject
```

#### Return Value

An asynchronous sequence of messages produced by this center.

## Parameters

- `subject`: The subject to observe. Specify a metatype to observe all values for a given type.
- `identifier`: An identifier representing a specific message type.
- `limit`: The maximum number of messages allowed to buffer.

## See Also

- [func messages<Identifier, Message>(of: Message.Subject.Type, for: Identifier, bufferSize: Int) -> some Sendable & AsyncSequence<Message, Never>
](notificationcenter/messages(of:for:buffersize:)-1ub69.md)
  Returns an asynchronous sequence of messages produced by this center for a given subject type and identifier.
- [func messages<Message>(of: Message.Subject?, for: Message.Type, bufferSize: Int) -> some Sendable & AsyncSequence<Message, Never>
](notificationcenter/messages(of:for:buffersize:)-623kg.md)
  Returns an asynchronous sequence of messages produced by this center for a given subject and message type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messages(of:for:buffersize:)-4tof0)*
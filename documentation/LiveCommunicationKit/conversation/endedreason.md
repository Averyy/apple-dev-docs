# Conversation.EndedReason

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that describe why a conversation ended.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum EndedReason
```

## Topics

### Reasons
- [Conversation.EndedReason.declinedElsewhere](conversation/endedreason/declinedelsewhere.md)
  Another device declined the conversation.
- [Conversation.EndedReason.failed](conversation/endedreason/failed.md)
  An error occurred while attempting to service the conversation.
- [Conversation.EndedReason.joinedElsewhere](conversation/endedreason/joinedelsewhere.md)
  Another device joined the conversation.
- [Conversation.EndedReason.remoteEnded](conversation/endedreason/remoteended.md)
  The remote party explicitly ended the conversation.
- [Conversation.EndedReason.unanswered](conversation/endedreason/unanswered.md)
  The conversation didn’t complete the connection process and was never explicitly ended.
### Initializers
- [init?(rawValue: Int)](conversation/endedreason/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](conversation/endedreason/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Conversation.EndedReason.RawValue](conversation/endedreason/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](conversation/endedreason/equatable-implementations.md)
- [RawRepresentable Implementations](conversation/endedreason/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Conversation.Event](conversation/event.md)
  Values that tell the system what happened during a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/endedreason)*
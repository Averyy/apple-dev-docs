# Conversation.EndedReason

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

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
- [Conversation.EndedReason.declinedElsewhere](./endedreason/declinedelsewhere.md)
  Another device declined the conversation.
- [Conversation.EndedReason.failed](./endedreason/failed.md)
  An error occurred while attempting to service the conversation.
- [Conversation.EndedReason.joinedElsewhere](./endedreason/joinedelsewhere.md)
  Another device joined the conversation.
- [Conversation.EndedReason.remoteEnded](./endedreason/remoteended.md)
  The remote party explicitly ended the conversation.
- [Conversation.EndedReason.unanswered](./endedreason/unanswered.md)
  The conversation didn’t complete the connection process and was never explicitly ended.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing a conversation
- [Conversation.Event](./event.md)
  Values that tell the system what happened during a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/endedreason)*
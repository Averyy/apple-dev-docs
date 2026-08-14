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

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Conversation.Event](conversation/event.md)
  Values that tell the system what happened during a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/endedreason)*
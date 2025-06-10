# Conversation.Event

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that tell the system what happened during a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum Event
```

## Topics

- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that conversation successfully connected at a point in time.
- [case conversationEnded(Date, Conversation.EndedReason)](conversation/event/conversationended(_:_:).md)
  Informs that system that a conversation ended at a point in time with a reason.
- [Conversation.Event.conversationStartedConnecting(_:)](conversation/event/conversationstartedconnecting(_:).md)
  Informs the system that a conversation has started to connect participants at a point in time.
- [case conversationUpdated(Conversation.Update)](conversation/event/conversationupdated(_:).md)
  Updates a conversation’s attributes and capabilities.
### Operators
- [static func == (Conversation.Event, Conversation.Event) -> Bool](conversation/event/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](conversation/event/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](conversation/event/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](conversation/event/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](conversation/event/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](conversation/event/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Conversation.EndedReason](conversation/endedreason.md)
  Values that describe why a conversation ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event)*
# Conversation.Event

**Framework**: LiveCommunicationKit  
**Kind**: enum

Specifies the type of event that has happened.

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

### Operators
- [static func == (Conversation.Event, Conversation.Event) -> Bool](conversation/event/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that `Conversation` successfully connected at the given `Date`.
- [case conversationEnded(Date, Conversation.EndedReason)](conversation/event/conversationended(_:_:).md)
  Informs that system that `Conversation` ended at the given `Date`, with the given `EndedReason`.
- [Conversation.Event.conversationStartedConnecting(_:)](conversation/event/conversationstartedconnecting(_:).md)
  Informs that system that `Conversation` has started connecting at the given `Date`.
- [case conversationUpdated(Conversation.Update)](conversation/event/conversationupdated(_:).md)
  Updates a `Conversation` with the given `Update`.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event)*
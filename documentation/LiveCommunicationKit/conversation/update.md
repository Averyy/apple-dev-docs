# Conversation.Update

**Framework**: LiveCommunicationKit  
**Kind**: struct

A type that describes new, changed, or deleted capabilities and attributes of a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Update
```

## Topics

### Initializers
- [init(localMember: Handle?, members: Set<Handle>?, activeRemoteMembers: Set<Handle>?, capabilities: Conversation.Capabilities?)](conversation/update/init(localmember:members:activeremotemembers:capabilities:).md)
  Creates an object with updated conversation attributes and capabilities.
- [init(from: any Decoder) throws](conversation/update/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Attributes
- [var activeRemoteMembers: Set<Handle>?](conversation/update/activeremotemembers.md)
  All active remote participants.
- [var capabilities: Conversation.Capabilities?](conversation/update/capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var localMember: Handle?](conversation/update/localmember.md)
  The local participant in the conversation.
- [var members: Set<Handle>?](conversation/update/members.md)
  All participants of the conversation, including invited, but inactive remote participants.
### Operators
- [static func == (Conversation.Update, Conversation.Update) -> Bool](conversation/update/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](conversation/update/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](conversation/update/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](conversation/update/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](conversation/update/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Conversation.Capabilities](conversation/capabilities.md)
  A type that describes capabilities of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update)*
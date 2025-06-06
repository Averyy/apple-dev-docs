# Conversation.Update

**Framework**: LiveCommunicationKit  
**Kind**: struct

An encapsulation of new, changed, or deleted information about a conversation.

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

### Operators
- [static func == (Conversation.Update, Conversation.Update) -> Bool](conversation/update/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](conversation/update/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(localMember: Handle?, members: Set<Handle>?, activeRemoteMembers: Set<Handle>?, capabilities: Conversation.Capabilities?)](conversation/update/init(localmember:members:activeremotemembers:capabilities:).md)
  Creates a new `Update`. Note that `nil` value means “no change”.
### Instance Properties
- [var activeRemoteMembers: Set<Handle>?](conversation/update/activeremotemembers.md)
  All active remote members.
- [var capabilities: Conversation.Capabilities?](conversation/update/capabilities.md)
  Functionality that the conversation supports once the `Update` is applied.
- [var hashValue: Int](conversation/update/hashvalue.md)
  The hash value.
- [var localMember: Handle?](conversation/update/localmember.md)
  The local member in the conversation.
- [var members: Set<Handle>?](conversation/update/members.md)
  All members of the conversation, including inactive (but invited) remote members.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update)*
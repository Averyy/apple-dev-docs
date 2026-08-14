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
### Attributes
- [var activeRemoteMembers: Set<Handle>?](conversation/update/activeremotemembers.md)
  All active remote participants.
- [var capabilities: Conversation.Capabilities?](conversation/update/capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var localMember: Handle?](conversation/update/localmember.md)
  The local participant in the conversation.
- [var members: Set<Handle>?](conversation/update/members.md)
  All participants of the conversation, including invited, but inactive remote participants.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Conversation.Capabilities](conversation/capabilities.md)
  A type that describes capabilities of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update)*
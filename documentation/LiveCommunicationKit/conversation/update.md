# Conversation.Update

**Framework**: LiveCommunicationKit  
**Kind**: struct  
**Role**: Structure

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
- [init(localMember: Handle?, members: Set<Handle>?, activeRemoteMembers: Set<Handle>?, capabilities: Conversation.Capabilities?)](./update/init%28localmember,members,activeremotemembers,capabilities%29.md)
  Creates an object with updated conversation attributes and capabilities.
### Attributes
- [var activeRemoteMembers: Set<Handle>?](./update/activeremotemembers.md)
  All active remote participants.
- [var capabilities: Conversation.Capabilities?](./update/capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var localMember: Handle?](./update/localmember.md)
  The local participant in the conversation.
- [var members: Set<Handle>?](./update/members.md)
  All participants of the conversation, including invited, but inactive remote participants.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Updating a conversation
- [Conversation.Capabilities](./capabilities.md)
  A type that describes capabilities of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update)*
# activeRemoteMembers

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

All active remote participants.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
var activeRemoteMembers: Set<Handle>? { get set }
```

## See Also

### Attributes
- [var capabilities: Conversation.Capabilities?](./capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var localMember: Handle?](./localmember.md)
  The local participant in the conversation.
- [var members: Set<Handle>?](./members.md)
  All participants of the conversation, including invited, but inactive remote participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update/activeremotemembers)*
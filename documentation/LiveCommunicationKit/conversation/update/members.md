# members

**Framework**: LiveCommunicationKit  
**Kind**: property

All participants of the conversation, including invited, but inactive remote participants.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
var members: Set<Handle>? { get set }
```

## See Also

- [var activeRemoteMembers: Set<Handle>?](conversation/update/activeremotemembers.md)
  All active remote participants.
- [var capabilities: Conversation.Capabilities?](conversation/update/capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var localMember: Handle?](conversation/update/localmember.md)
  The local participant in the conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update/members)*
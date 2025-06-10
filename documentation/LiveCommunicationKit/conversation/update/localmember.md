# localMember

**Framework**: LiveCommunicationKit  
**Kind**: property

The local participant in the conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
var localMember: Handle? { get set }
```

## See Also

- [var activeRemoteMembers: Set<Handle>?](conversation/update/activeremotemembers.md)
  All active remote participants.
- [var capabilities: Conversation.Capabilities?](conversation/update/capabilities.md)
  Functionality that the conversation supports after the system applies the update.
- [var members: Set<Handle>?](conversation/update/members.md)
  All participants of the conversation, including invited, but inactive remote participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update/localmember)*
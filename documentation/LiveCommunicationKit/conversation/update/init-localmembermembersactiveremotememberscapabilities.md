# init(localMember:members:activeRemoteMembers:capabilities:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an object with updated conversation attributes and capabilities.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(localMember: Handle? = nil, members: Set<Handle>? = nil, activeRemoteMembers: Set<Handle>? = nil, capabilities: Conversation.Capabilities? = nil)
```

## Parameters

- `localMember`: The local participant.
- `members`: All participants.
- `activeRemoteMembers`: The active remote participants.
- `capabilities`: The conversation’s capabilities.

## See Also

- [init(from: any Decoder) throws](conversation/update/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/update/init(localmember:members:activeremotemembers:capabilities:))*
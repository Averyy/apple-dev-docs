# init(conversationUUID:handles:isVideo:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an action that starts an outgoing conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(conversationUUID: UUID, handles: [Handle], isVideo: Bool)
```

## Parameters

- `conversationUUID`: The unique identifier of the conversation to start.
- `handles`: The handles of all remote members who receive an invite  to join the conversation.
- `isVideo`: A value that specifies if the conversation contains a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startconversationaction/init(conversationuuid:handles:isvideo:))*
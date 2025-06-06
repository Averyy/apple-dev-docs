# init(conversationUUID:handles:isVideo:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new `StartConversationAction`.

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

- `conversationUUID`: The unique identfiier of the   to which this action will be applied.
- `handles`: The  s of all remote members who will be invited to join the  .
- `isVideo`: Specifies if the   contains a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startconversationaction/init(conversationuuid:handles:isvideo:))*
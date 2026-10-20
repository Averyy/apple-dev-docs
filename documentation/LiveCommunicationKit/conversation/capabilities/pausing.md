# pausing

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Type Property

The conversation is active and can be temporarily paused.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static let pausing: Conversation.Capabilities
```

#### Discussion

Pausing a conversation can include stopping all microphone, camera, and speaker interaction.

## See Also

### Capabilities
- [static let merging: Conversation.Capabilities](./merging.md)
  The conversation can merge with another conversation to create a new conversation.
- [static let playingTones: Conversation.Capabilities](./playingtones.md)
  The conversation supports playing tone sequences.
- [static let unmerging: Conversation.Capabilities](./unmerging.md)
  The conversation is the result of merging two conversations and can be separated into the original conversations.
- [static let video: Conversation.Capabilities](./video.md)
  The conversation sends or displays video streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities/pausing)*
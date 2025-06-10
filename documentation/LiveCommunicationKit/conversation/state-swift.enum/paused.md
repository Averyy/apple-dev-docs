# Conversation.State.paused

**Framework**: LiveCommunicationKit  
**Kind**: case

Audio and video streams are paused, but may resume.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case paused
```

## See Also

- [Conversation.State.idle](conversation/state-swift.enum/idle.md)
  The conversation was registered with the system, but it’s not active yet.
- [Conversation.State.joined](conversation/state-swift.enum/joined.md)
  Audio and video streams are active and the local participant is able to engage with remote participants.
- [Conversation.State.joining](conversation/state-swift.enum/joining.md)
  The setup process of the conversation in progress; for example, establishing audio and video streams.
- [Conversation.State.leaving](conversation/state-swift.enum/leaving.md)
  Participants left the conversation and it’s in the process of ending.
- [Conversation.State.left](conversation/state-swift.enum/left.md)
  The conversation is no longer active and all audio and video sessions have ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/state-swift.enum/paused)*
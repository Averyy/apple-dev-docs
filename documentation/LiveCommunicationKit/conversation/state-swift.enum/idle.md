# Conversation.State.idle

**Framework**: LiveCommunicationKit  
**Kind**: case  
**Role**: Case

The conversation was registered with the system, but it’s not active yet.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case idle
```

## See Also

### States
- [Conversation.State.joined](./joined.md)
  Audio and video streams are active and the local participant is able to engage with remote participants.
- [Conversation.State.joining](./joining.md)
  The setup process of the conversation in progress; for example, establishing audio and video streams.
- [Conversation.State.leaving](./leaving.md)
  Participants left the conversation and it’s in the process of ending.
- [Conversation.State.left](./left.md)
  The conversation is no longer active and all audio and video sessions have ended.
- [Conversation.State.paused](./paused.md)
  Audio and video streams are paused, but may resume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/state-swift.enum/idle)*
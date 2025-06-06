# playerVoiceChatStateDidChangeHandler

**Framework**: GameKit  
**Kind**: property

A method that handles when a player’s voice chat changes state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChat.PlayerState) -> Void { get set }
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

Set this property to update your interface when the state of any player in the chat changes, including the local player. For example, update the names or avatars when the players are connecting, speaking, or disconnecting.

The handler receives the following parameters:

## See Also

- [GKVoiceChat.PlayerState](gkvoicechat/playerstate.md)
  The state of a player in a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playervoicechatstatedidchangehandler)*
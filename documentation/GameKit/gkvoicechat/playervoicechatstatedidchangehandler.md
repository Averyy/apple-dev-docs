# playerVoiceChatStateDidChangeHandler

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A method that handles when a player’s voice chat changes state.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.10+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChat.PlayerState) -> Void { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) void (^)(GKPlayer *, enum GKVoiceChatPlayerState) playerVoiceChatStateDidChangeHandler;
```

*macOS*

```objc
@property (atomic, copy) void (^)(GKPlayer *, enum GKVoiceChatPlayerState) playerVoiceChatStateDidChangeHandler;
```

## Mentions

- [Adding voice chat to multiplayer games](../adding-voice-chat-to-multiplayer-games.md)

#### Discussion

Set this property to update your interface when the state of any player in the chat changes, including the local player. For example, update the names or avatars when the players are connecting, speaking, or disconnecting.

The handler receives the following parameters:

- **`player`**: The player whose status changed.
- **`state`**: The new state of the player.

## See Also

### Receiving Updates About Other Participants
- [GKVoiceChat.PlayerState](./playerstate.md)
  The state of a player in a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playervoicechatstatedidchangehandler)*
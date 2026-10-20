# GKVoiceChat.PlayerState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The state of a player in a voice chat.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use SharePlay instead. See [Enable the local player to choose other players](../finding-multiple-players-for-a-game.md#Enable-the-local-player-to-choose-other-players) and [`startGroupActivity(playerHandler:)`](../gkmatchmaker/startgroupactivity%28playerhandler%29.md).

## Declaration

```swift
enum PlayerState
```

```c
enum GKVoiceChatPlayerState : NSInteger;
```

## Topics

### States
- [GKVoiceChat.PlayerState.connected](./playerstate/connected.md)
  The state when the player connects to the channel.
- [GKVoiceChat.PlayerState.disconnected](./playerstate/disconnected.md)
  The state when the player left the channel.
- [GKVoiceChat.PlayerState.speaking](./playerstate/speaking.md)
  The state when the player speaks.
- [GKVoiceChat.PlayerState.silent](./playerstate/silent.md)
  The state when the player isn’t speaking.
- [GKVoiceChat.PlayerState.connecting](./playerstate/connecting.md)
  The state when the player is connecting to the channel, but isn’t connected yet.
### Initializers
- [init?(rawValue: Int)](./playerstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving Updates About Other Participants
- [var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChat.PlayerState) -> Void](./playervoicechatstatedidchangehandler.md)
  A method that handles when a player’s voice chat changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playerstate)*
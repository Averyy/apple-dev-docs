# setPlayer(_:muted:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Mutes a player in the chat, including the local player.

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
func setPlayer(_ player: GKPlayer, muted isMuted: Bool)
```

```objc
- (void) setPlayer:(GKPlayer *) player muted:(BOOL) isMuted;
```

## Mentions

- [Adding voice chat to multiplayer games](../adding-voice-chat-to-multiplayer-games.md)

## Discussion

If you mute another player, the local player doesn’t hear voice data from that player.

## Parameters

- `player`: The player that GameKit mutes or unmutes.
- `isMuted`: Determines whether to mute or unmute the player.

## See Also

### Controlling Chat Volume
- [var volume: Float](./volume.md)
  The volume level for the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/setplayer(_:muted:))*
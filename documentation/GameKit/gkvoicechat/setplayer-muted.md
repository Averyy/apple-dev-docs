# setPlayer(_:muted:)

**Framework**: GameKit  
**Kind**: method

Mutes a player in the chat, including the local player.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPlayer(_ player: GKPlayer, muted isMuted: Bool)
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

If you mute another player, the local player doesn’t hear voice data from that player.

## Parameters

- `player`: The player that GameKit mutes or unmutes.
- `isMuted`: Determines whether to mute or unmute the player.

## See Also

- [var volume: Float](gkvoicechat/volume.md)
  The volume level for the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/setplayer(_:muted:))*
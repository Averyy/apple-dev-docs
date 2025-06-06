# setMute(_:forPlayer:)

**Framework**: GameKit  
**Kind**: method

Mutes a player in a voice chat.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func setMute(_ isMuted: Bool, forPlayer playerID: String)
```

#### Discussion

If you mute a player, the local player doesn’t hear voice data transmitted by that player.

## Parameters

- `isMuted`: Determines whether to mute or unmute the player.
- `playerID`: The player identifier string for a player in the match.

## See Also

- [var playerIDs: [String]?](gkvoicechat/playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](gkvoicechat/playerstateupdatehandler.md)
  Handles when a player in the chat changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/setmute(_:forplayer:))*
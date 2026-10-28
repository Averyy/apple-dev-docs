# setMute(_:forPlayer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Mutes a player in a voice chat.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`setPlayer(_:muted:)`](./setplayer%28_,muted%29.md) method instead.

## Declaration

```swift
func setMute(_ isMuted: Bool, forPlayer playerID: String)
```

```objc
- (void) setMute:(BOOL) isMuted forPlayer:(NSString *) playerID;
```

## Discussion

If you mute a player, the local player doesn’t hear voice data transmitted by that player.

## Parameters

- `isMuted`: Determines whether to mute or unmute the player.
- `playerID`: The player identifier string for a player in the match.

## See Also

### Deprecated Methods and Properties
- [var playerIDs: [String]?](./playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](./playerstateupdatehandler.md)
  Handles when a player in the chat changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/setmute(_:forplayer:))*
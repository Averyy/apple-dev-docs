# playerStateUpdateHandler

**Framework**: GameKit  
**Kind**: property

Handles when a player in the chat changes state.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void { get set }
```

#### Discussion

Your game sets this property with a block that GameKit calls when the state of any participant in the chat changes (including the local player). The block receives the following parameters:

## See Also

- [var playerIDs: [String]?](gkvoicechat/playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [func setMute(Bool, forPlayer: String)](gkvoicechat/setmute(_:forplayer:).md)
  Mutes a player in a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playerstateupdatehandler)*
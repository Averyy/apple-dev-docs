# playerStateUpdateHandler

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

Handles when a player in the chat changes state.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`setPlayer(_:muted:)`](./setplayer%28_,muted%29.md) method instead.

## Declaration

```swift
var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) void (^playerStateUpdateHandler)(NSString *playerID, GKVoiceChatPlayerState state);
```

*macOS*

```objc
@property (atomic, copy) void (^playerStateUpdateHandler)(NSString *playerID, GKVoiceChatPlayerState state);
```

## Discussion

Your game sets this property with a block that GameKit calls when the state of any participant in the chat changes (including the local player). The block receives the following parameters:

- **`playerID`**: The player identifier for the player whose status changed.
- **`state`**: The new state of the player. See [`GKVoiceChat.PlayerState`](./playerstate.md).

## See Also

### Deprecated Methods and Properties
- [var playerIDs: [String]?](./playerids.md)
  An array of strings containing the player identifiers for the players connected to the channel.
- [func setMute(Bool, forPlayer: String)](./setmute%28_,forplayer%29.md)
  Mutes a player in a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playerstateupdatehandler)*
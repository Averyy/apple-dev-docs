# playerIDs

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

An array of strings containing the player identifiers for the players connected to the channel.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`players`](./players.md) property instead.

## Declaration

```swift
var playerIDs: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSArray<NSString *> * playerIDs;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSArray<NSString *> * playerIDs;
```

## See Also

### Deprecated Methods and Properties
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](./playerstateupdatehandler.md)
  Handles when a player in the chat changes state.
- [func setMute(Bool, forPlayer: String)](./setmute%28_,forplayer%29.md)
  Mutes a player in a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/playerids)*
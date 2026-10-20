# playerID

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for a player.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.15
- tvOS 10.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 6.0

> **Deprecated**: Use [`gamePlayerID`](../gkplayer/gameplayerid.md) or [`teamPlayerID`](../gkplayer/teamplayerid.md) instead.

## Declaration

```swift
var playerID: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, readonly, nullable) NSString * playerID;
```

*macOS*

```objc
@property (atomic, retain, readonly, nullable) NSString * playerID;
```

## See Also

### Identifying a Player
- [var displayName: String?](./displayname.md)
  The Game Center profile name for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkbaseplayer/playerid)*
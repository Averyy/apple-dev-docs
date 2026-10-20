# playerID

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for a player of the game.

**Availability**:
- iOS 4.1+ - Deprecated in 13.0
- iPadOS 4.1+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use [`gamePlayerID`](./gameplayerid.md) or [`teamPlayerID`](./teamplayerid.md) instead.

## Declaration

```swift
var playerID: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, readonly, nonnull) NSString * playerID;
```

*macOS*

```objc
@property (atomic, retain, readonly, nonnull) NSString * playerID;
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](../protecting-the-player-s-privacy-using-scoped-identifiers.md)

#### Discussion

Never display the player identifier to the player. Use it only to identify a player in your code.

## See Also

### Identifying the player
- [var gamePlayerID: String](./gameplayerid.md)
  A unique identifier for a player of the game.
- [var teamPlayerID: String](./teamplayerid.md)
  A unique identifier for a player of all the games that you distribute using your developer account.
- [func scopedIDsArePersistent() -> Bool](./scopedidsarepersistent%28%29.md)
  Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.
- [let GKPlayerIDNoLongerAvailable: String](../gkplayeridnolongeravailable.md)
  A constant for a player ID that’s no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/playerid)*
# scopedIDsArePersistent()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func scopedIDsArePersistent() -> Bool
```

```objc
- (BOOL) scopedIDsArePersistent;
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](../protecting-the-player-s-privacy-using-scoped-identifiers.md)

## Return Value

Returns [`true`](../../Swift/true.md) if the [`gamePlayerID`](./gameplayerid.md) and [`teamPlayerID`](./teamplayerid.md) properties are the same across all instances of this game; otherwise, [`false`](../../Swift/false.md) if the identifiers are unique to this game instance only.

## Discussion

An instance is the time between when the game launches and when the game terminates.

## See Also

### Identifying the player
- [var gamePlayerID: String](./gameplayerid.md)
  A unique identifier for a player of the game.
- [var teamPlayerID: String](./teamplayerid.md)
  A unique identifier for a player of all the games that you distribute using your developer account.
- [let GKPlayerIDNoLongerAvailable: String](../gkplayeridnolongeravailable.md)
  A constant for a player ID that’s no longer available.
- [var playerID: String](./playerid.md)
  A unique identifier for a player of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/scopedidsarepersistent())*
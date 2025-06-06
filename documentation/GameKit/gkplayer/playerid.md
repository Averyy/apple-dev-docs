# playerID

**Framework**: GameKit  
**Kind**: property

A unique identifier for a player of the game.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var playerID: String { get }
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md)

#### Discussion

Never display the player identifier to the player. Use it only to identify a player in your code.

## See Also

- [var gamePlayerID: String](gkplayer/gameplayerid.md)
  A unique identifier for a player of the game.
- [var teamPlayerID: String](gkplayer/teamplayerid.md)
  A unique identifier for a player of all the games that you distribute using your developer account.
- [func scopedIDsArePersistent() -> Bool](gkplayer/scopedidsarepersistent.md)
  Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.
- [let GKPlayerIDNoLongerAvailable: String](gkplayeridnolongeravailable.md)
  A constant for a player ID that’s no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/playerid)*
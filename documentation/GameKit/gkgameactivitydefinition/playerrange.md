# playerRange

**Framework**: GameKit  
**Kind**: property

The range of players supported by this type of game activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var playerRange: (any RangeExpression)? { get }
```

#### Discussion

This can be nil if neither of minPlayers or maxPlayers are set by the developer, a closed range if both are set, or an open range suggesting this game activity supports an unlimited number of players.

## See Also

- [var supportsPartyCode: Bool](gkgameactivitydefinition/supportspartycode.md)
  Whether the activity can be joined by others via a party code.
- [var supportsUnlimitedPlayers: Bool](gkgameactivitydefinition/supportsunlimitedplayers.md)
  True if the activity supports an unlimited number of players. False if maxPlayers is set to a defined limit or if no player range is provided.
- [var playStyle: GKGameActivityPlayStyle](gkgameactivitydefinition/playstyle.md)
  The play style of the game activity.
- [enum GKGameActivityPlayStyle](gkgameactivityplaystyle.md)
  Play Style of the game activity. It can be either Asynchronous or Synchronous.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/playerrange)*
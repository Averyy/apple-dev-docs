# supportsUnlimitedPlayers

**Framework**: GameKit  
**Kind**: property

True if the activity supports an unlimited number of players. False if maxPlayers is set to a defined limit or if no player range is provided.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var supportsUnlimitedPlayers: Bool { get }
```

## See Also

- [var supportsPartyCode: Bool](gkgameactivitydefinition/supportspartycode.md)
  Whether the activity can be joined by others via a party code.
- [var playerRange: (any RangeExpression)?](gkgameactivitydefinition/playerrange.md)
  The range of players supported by this type of game activity.
- [var playStyle: GKGameActivityPlayStyle](gkgameactivitydefinition/playstyle.md)
  The play style of the game activity.
- [enum GKGameActivityPlayStyle](gkgameactivityplaystyle.md)
  Play Style of the game activity. It can be either Asynchronous or Synchronous.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/supportsunlimitedplayers)*
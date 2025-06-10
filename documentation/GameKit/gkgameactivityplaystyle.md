# GKGameActivityPlayStyle

**Framework**: GameKit  
**Kind**: enum

Play Style of the game activity. It can be either Asynchronous or Synchronous.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum GKGameActivityPlayStyle
```

## Topics

### Enumeration Cases
- [GKGameActivityPlayStyle.asynchronous](gkgameactivityplaystyle/asynchronous.md)
- [GKGameActivityPlayStyle.synchronous](gkgameactivityplaystyle/synchronous.md)
- [GKGameActivityPlayStyle.unspecified](gkgameactivityplaystyle/unspecified.md)
### Initializers
- [init?(rawValue: Int)](gkgameactivityplaystyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var supportsPartyCode: Bool](gkgameactivitydefinition/supportspartycode.md)
  Whether the activity can be joined by others via a party code.
- [var supportsUnlimitedPlayers: Bool](gkgameactivitydefinition/supportsunlimitedplayers.md)
  True if the activity supports an unlimited number of players. False if maxPlayers is set to a defined limit or if no player range is provided.
- [var playerRange: (any RangeExpression)?](gkgameactivitydefinition/playerrange.md)
  The range of players supported by this type of game activity.
- [var playStyle: GKGameActivityPlayStyle](gkgameactivitydefinition/playstyle.md)
  The play style of the game activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivityplaystyle)*
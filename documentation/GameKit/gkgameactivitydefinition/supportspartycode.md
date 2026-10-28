# supportsPartyCode

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

Whether the activity can be joined by others via a party code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var supportsPartyCode: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL supportsPartyCode;
```

## Discussion

> **See Also**: `-[GKGameActivityListener player:wantsToPlayGameActivity:completionHandler:]` where you can receive and handle game activities that players want to play in a party with friends.

## See Also

### Getting the activity capabilities
- [var supportsUnlimitedPlayers: Bool](./supportsunlimitedplayers.md)
  True if the activity supports an unlimited number of players. False if maxPlayers is set to a defined limit or if no player range is provided.
- [var playerRange: (any RangeExpression)?](./playerrange.md)
  The range of players supported by this type of game activity.
- [var playStyle: GKGameActivityPlayStyle](./playstyle.md)
  The play style of the game activity.
- [enum GKGameActivityPlayStyle](../gkgameactivityplaystyle.md)
  Play Style of the game activity. It can be either Asynchronous or Synchronous.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/supportspartycode)*
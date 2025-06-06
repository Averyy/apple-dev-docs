# playerGroup

**Framework**: GameKit  
**Kind**: property

A number identifying a subset of players invited to join a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var playerGroup: Int { get set }
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Creating matchmaking rules for backward compatibility](creating-matchmaking-rules-for-backward-compatibility.md)

#### Discussion

Game Center only finds players whose `GKMatchRequest` objects share the same `playerGroup` value. For example, use the `playerGroup` property to create matches based on skill level, game modes, or other common interests. The default value of this property is `1`.

## See Also

- [var playerAttributes: UInt32](gkmatchrequest/playerattributes.md)
  A mask that specifies the role that the local player would like to play in the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/playergroup)*
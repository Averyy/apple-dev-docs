# playerAttributes

**Framework**: GameKit  
**Kind**: property

A mask that specifies the role that the local player would like to play in the game.

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
var playerAttributes: UInt32 { get set }
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)

#### Discussion

If the value of this property is `0xFFFFFFFF` (the default), GameKit ignores this property. If the value is nonzero, GameKit uses the value as a mask that restricts the role of the player in the match. GameKit finds new players for the game so that the bitwise OR of all the player’s masks equals `0xFFFFFFFF`.

## See Also

- [var playerGroup: Int](gkmatchrequest/playergroup.md)
  A number identifying a subset of players invited to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/playerattributes)*
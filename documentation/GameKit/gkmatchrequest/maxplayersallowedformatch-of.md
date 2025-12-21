# maxPlayersAllowedForMatch(of:)

**Framework**: GameKit  
**Kind**: method

Returns the maximum number of players allowed in the match request for a given match type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func maxPlayersAllowedForMatch(of matchType: GKMatchType) -> Int
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Return Value

The maximum number of allowed players.

#### Discussion

For peer-to-peer, hosted, and turn-based matches, the maximum number of players is `16`.

## Parameters

- `matchType`: The kind of match.

## See Also

- [enum GKMatchType](gkmatchtype.md)
  The kind of match managed by Game Center.
- [var minPlayers: Int](gkmatchrequest/minplayers.md)
  The minimum number of players that can join the match.
- [var maxPlayers: Int](gkmatchrequest/maxplayers.md)
  The maximum number of players that can join the match.
- [var defaultNumberOfPlayers: Int](gkmatchrequest/defaultnumberofplayers.md)
  The default number of players for the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/maxplayersallowedformatch(of:))*
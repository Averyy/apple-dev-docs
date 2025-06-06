# init(playerIDs:)

**Framework**: GameKit  
**Kind**: init

Initializes a leaderboard request to retrieve the scores of a specific group of players.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(playerIDs: [String]?)
```

#### Return Value

An initialized leaderboard request.

#### Discussion

A leaderboard object that you initialize with this method ignores the [`playerScope`](gkleaderboard/playerscope-swift.property.md) and [`range`](gkleaderboard/range.md) properties. Instead, it retrieves scores for the specific list of players whose identifiers are in the `playerIDs` parameter.

## Parameters

- `playerIDs`: An array of   objects that holds the player identifier strings of the players to retrieve.

## See Also

- [init(players: [GKPlayer])](gkleaderboard/init(players:).md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/init(playerids:))*
# init(players:)

**Framework**: GameKit  
**Kind**: init

Initializes a leaderboard request to retrieve the scores of a specific group of players.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(players: [GKPlayer])
```

#### Return Value

An initialized leaderboard request.

#### Discussion

A leaderboard object that you initialize with this method ignores the [`playerScope`](gkleaderboard/playerscope-swift.property.md) and [`range`](gkleaderboard/range.md) properties. Instead, it retrieves scores for the specific list of players whose [`GKPlayer`](gkplayer.md) objects are in the `players` parameter.

## Parameters

- `players`: An array of   objects that holds the player identifiers to retrieve.

## See Also

- [init?(playerIDs: [String]?)](gkleaderboard/init(playerids:).md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/init(players:))*
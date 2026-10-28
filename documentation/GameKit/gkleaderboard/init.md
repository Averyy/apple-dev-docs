# init

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Initializes a default leaderboard request.

**Availability**:
- iOS 4.0+ - Deprecated in 14.0
- iPadOS 4.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

## Declaration

```objc
- (instancetype) init;
```

## Return Value

An initialized leaderboard request.

## Discussion

A leaderboard object that you initialize with this method uses the [`playerScope`](./playerscope-swift.property.md), [`timeScope`](./timescope-swift.property.md), and [`range`](./range.md) properties to search Game Center for scores.

## See Also

### Deprecated initializers
- [init?(playerIDs: [String]?)](./init%28playerids%29.md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.
- [init(players: [GKPlayer])](./init%28players%29.md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/init)*
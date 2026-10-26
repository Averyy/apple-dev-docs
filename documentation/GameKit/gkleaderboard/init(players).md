# init(players:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes a leaderboard request to retrieve the scores of a specific group of players.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:completionHandler:)`](./loadentries%28for,timescope,completionhandler%29.md) method instead.

## Declaration

```swift
init(players: [GKPlayer])
```

```objc
- (instancetype) initWithPlayers:(NSArray<GKPlayer *> *) players;
```

#### Return Value

An initialized leaderboard request.

#### Discussion

A leaderboard object that you initialize with this method ignores the [`playerScope`](./playerscope-swift.property.md) and [`range`](./range.md) properties. Instead, it retrieves scores for the specific list of players whose [`GKPlayer`](../gkplayer.md) objects are in the `players` parameter.

## Parameters

- `players`: An array of [`GKPlayer`](../gkplayer.md) objects that holds the player identifiers to retrieve.

## See Also

### Deprecated initializers
- [init?(playerIDs: [String]?)](./init%28playerids%29.md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.
- [- init](./init.md)
  Initializes a default leaderboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/init(players:))*
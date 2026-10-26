# init(playerIDs:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes a leaderboard request to retrieve the scores of a specific group of players.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`loadEntries(for:timeScope:completionHandler:)`](./loadentries%28for,timescope,completionhandler%29.md) method instead.

## Declaration

```swift
init?(playerIDs: [String]?)
```

```objc
- (instancetype) initWithPlayerIDs:(NSArray<NSString *> *) playerIDs;
```

#### Return Value

An initialized leaderboard request.

#### Discussion

A leaderboard object that you initialize with this method ignores the [`playerScope`](./playerscope-swift.property.md) and [`range`](./range.md) properties. Instead, it retrieves scores for the specific list of players whose identifiers are in the `playerIDs` parameter.

## Parameters

- `playerIDs`: An array of `NSString` objects that holds the player identifier strings of the players to retrieve.

## See Also

### Deprecated initializers
- [init(players: [GKPlayer])](./init%28players%29.md)
  Initializes a leaderboard request to retrieve the scores of a specific group of players.
- [- init](./init.md)
  Initializes a default leaderboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/init(playerids:))*
# match(_:shouldReinviteDisconnectedPlayer:)

**Framework**: GameKit  
**Kind**: method

Determines whether the local player should reinvite another player who disconnected from a two-player match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func match(_ match: GKMatch, shouldReinviteDisconnectedPlayer player: GKPlayer) -> Bool
```

## Mentions

- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if GameKit should reinvite the player when they disconnect; [`false`](https://developer.apple.com/documentation/Swift/false) if GameKit should end the match when the player disconnects.

#### Discussion

If the player successfully reconnects to the match, GameKit sends [`match(_:player:didChange:)`](gkmatchdelegate/match(_:player:didchange:)-8ohgr.md) to the match’s delegate.

## Parameters

- `match`: The match that the player disconnected from.
- `player`: The player who disconnected from the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/match(_:shouldreinvitedisconnectedplayer:))*
# submitScore(_:context:player:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Submits a score to the leaderboard.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func submitScore(_ score: Int, context: Int, player: GKPlayer) async throws
```

## Mentions

- [Creating recurring leaderboards](creating-recurring-leaderboards.md)
- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `score`: The score that the player earns.
- `context`: An integer value that your game uses.
- `player`: The player who earns the score.
- `completionHandler`: The block receives the following parameters:

## See Also

- [class func submitScore(Int, context: Int, player: GKPlayer, leaderboardIDs: [String], completionHandler: ((any Error)?) -> Void)](gkleaderboard/submitscore(_:context:player:leaderboardids:completionhandler:).md)
  Submits a score to multiple leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/submitscore(_:context:player:completionhandler:))*
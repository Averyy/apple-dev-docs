# submitScore(_:context:player:leaderboardIDs:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Submits a score to multiple leaderboards.

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
class func submitScore(_ score: Int, context: Int, player: GKPlayer, leaderboardIDs: [String]) async throws
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)
- [Creating recurring leaderboards](creating-recurring-leaderboards.md)

## Parameters

- `score`: The score that the player earns.
- `context`: An integer value that your game uses.
- `player`: The player who earns the score.
- `leaderboardIDs`: The IDs that Game Center uses for the leaderboards to submit the score to.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func submitScore(Int, context: Int, player: GKPlayer, completionHandler: ((any Error)?) -> Void)](gkleaderboard/submitscore(_:context:player:completionhandler:).md)
  Submits a score to the leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/submitscore(_:context:player:leaderboardids:completionhandler:))*
# setDefaultLeaderboardIdentifier(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sets the local player’s default leaderboard.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String) async throws
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

#### Discussion

Until you change the default leaderboard for a player, it is the same as the default leaderboard for your game that you set in App Store Connect.

## Parameters

- `leaderboardIdentifier`: The identifier of the leaderboard.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func loadDefaultLeaderboardIdentifier(completionHandler: ((String?, (any Error)?) -> Void)?)](gklocalplayer/loaddefaultleaderboardidentifier(completionhandler:).md)
  Loads the identifier for the local player’s default leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/setdefaultleaderboardidentifier(_:completionhandler:))*
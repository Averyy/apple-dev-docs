# findPlayersForHostedMatch(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Use information from the activity to find server hosted players for the local player.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func findPlayersForHostedMatch() async throws -> [GKPlayer]
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

GameKit creates a classic server hosted match making request with the activity’s party code and other information, and returns the players in the completion handler or any error that occurred. An error occurs if this activity doesn’t support party code, or has unsupported range of players, which is used to be configured as match request’s `minPlayers` and `maxPlayers`.

## See Also

- [func findMatch(completionHandler: (GKMatch?, (any Error)?) -> Void)](gkgameactivity/findmatch(completionhandler:).md)
  Use information from the activity to find matches for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/findplayersforhostedmatch(completionhandler:))*
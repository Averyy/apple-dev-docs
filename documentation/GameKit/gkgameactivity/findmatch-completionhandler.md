# findMatch(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Use information from the activity to find matches for the local player.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func findMatch() async throws -> GKMatch
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

GameKit will create a classic match making request with the activity’s party code and other information, and return the match object in the completion handler or any error that occurred. Error occurs if this activity doesn’t support party code, or has unsupported range of players, which is used to be configured as match request’s minPlayers and maxPlayers.

## See Also

- [func findPlayersForHostedMatch(completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](gkgameactivity/findplayersforhostedmatch(completionhandler:).md)
  Use information from the activity to find server hosted players for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/findmatch(completionhandler:))*
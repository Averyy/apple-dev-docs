# findPlayersForHostedMatch(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Use information from the activity to find server hosted players for the local player.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func findPlayersForHostedMatch() async throws -> [GKPlayer]
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

GameKit will create a classic server hosted match making request with the activity’s party code and other information, and return the players in the completion handler or any error that occurred. Error occurs if this activity doesn’t support party code, or has unsupported range of players, which is used to be configured as match request’s minPlayers and maxPlayers.

## See Also

- [func findMatch(completionHandler: (GKMatch?, (any Error)?) -> Void)](gkgameactivity/findmatch(completionhandler:).md)
  Use information from the activity to find matches for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/findplayersforhostedmatch(completionhandler:))*
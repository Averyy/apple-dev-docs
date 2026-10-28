# findMatch(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Use information from the activity to find matches for the local player.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func findMatch(completionHandler: @escaping @Sendable (GKMatch?, (any Error)?) -> Void)
```

```swift
func findMatch() async throws -> GKMatch
```

```objc
- (void) findMatchWithCompletionHandler:(void (^)(GKMatch *match, NSError *error)) completionHandler;
```

## Mentions

- [Creating activities for your game](../creating-activities-for-your-game.md)

## Discussion

GameKit creates a classic match making request with the activity’s party code and other information, and returns the match object in the completion handler or any error that occurred. An error occurs if this activity doesn’t support party code, or has an unsupported range of players, which is used to be configured as match request’s `minPlayers` and `maxPlayers`.

## See Also

### Performing a matchmaking request
- [func findPlayersForHostedMatch(completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](./findplayersforhostedmatch%28completionhandler%29.md)
  Use information from the activity to find server hosted players for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/findmatch(completionhandler:))*
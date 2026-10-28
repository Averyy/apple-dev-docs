# findPlayersForHostedMatch(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func findPlayersForHostedMatch(completionHandler: @escaping @Sendable ([GKPlayer]?, (any Error)?) -> Void)
```

```swift
func findPlayersForHostedMatch() async throws -> [GKPlayer]
```

```objc
- (void) findPlayersForHostedMatchWithCompletionHandler:(void (^)(NSArray<GKPlayer *> *players, NSError *error)) completionHandler;
```

## Mentions

- [Creating activities for your game](../creating-activities-for-your-game.md)

## Discussion

GameKit creates a classic server hosted match making request with the activity’s party code and other information, and returns the players in the completion handler or any error that occurred. An error occurs if this activity doesn’t support party code, or has unsupported range of players, which is used to be configured as match request’s `minPlayers` and `maxPlayers`.

## See Also

### Performing a matchmaking request
- [func findMatch(completionHandler: (GKMatch?, (any Error)?) -> Void)](./findmatch%28completionhandler%29.md)
  Use information from the activity to find matches for the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/findplayersforhostedmatch(completionhandler:))*
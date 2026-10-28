# finishMatchmaking(for:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Informs the server when programmatic matchmaking finishes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finishMatchmaking(for match: GKMatch)
```

```objc
- (void) finishMatchmakingForMatch:(GKMatch *) match;
```

## Mentions

- [Finding multiple players for a game](../finding-multiple-players-for-a-game.md)

## Discussion

If you need to call the [`addPlayers(to:matchRequest:completionHandler:)`](./addplayers%28to,matchrequest,completionhandler%29.md) method to fill the slots in an existing match, call the [`finishMatchmaking(for:)`](./finishmatchmaking%28for%29.md) method when you have enough players and before you begin the match.

## Parameters

- `match`: The match that you are ready to start.

## See Also

### Matching players
- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](./findmatch%28for,withcompletionhandler%29.md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./findplayers%28forhostedrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](./findmatchedplayers%28_,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [class GKMatchedPlayers](../gkmatchedplayers.md)
  An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.
- [func addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: (((any Error)?) -> Void)?)](./addplayers%28to,matchrequest,completionhandler%29.md)
  Invites additional players to an existing match.
- [func cancel()](./cancel%28%29.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](./cancelpendinginvite%28to%29.md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/finishmatchmaking(for:))*
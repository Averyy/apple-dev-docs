# cancel()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Cancels a matchmaking request.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

#### Discussion

GameKit sends a [`GKError.Code.cancelled`](../gkerror/code/cancelled.md) error to the completion handler of either the [`findMatch(for:withCompletionHandler:)`](./findmatch%28for,withcompletionhandler%29.md) or [`findPlayers(forHostedRequest:withCompletionHandler:)`](./findplayers%28forhostedrequest,withcompletionhandler%29.md) method.

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
- [func finishMatchmaking(for: GKMatch)](./finishmatchmaking%28for%29.md)
  Informs the server when programmatic matchmaking finishes.
- [func cancelPendingInvite(to: GKPlayer)](./cancelpendinginvite%28to%29.md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/cancel())*
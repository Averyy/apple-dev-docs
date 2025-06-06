# finishMatchmaking(for:)

**Framework**: GameKit  
**Kind**: method

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

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

If you need to call the [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) method to fill the slots in an existing match, call the [`finishMatchmaking(for:)`](gkmatchmaker/finishmatchmaking(for:).md) method when you have enough players and before you begin the match.

## Parameters

- `match`: The match that you are ready to start.

## See Also

- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/findmatch(for:withcompletionhandler:).md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [class GKMatchedPlayers](gkmatchedplayers.md)
  An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.
- [func addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: (((any Error)?) -> Void)?)](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md)
  Invites additional players to an existing match.
- [func cancel()](gkmatchmaker/cancel.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](gkmatchmaker/cancelpendinginvite(to:).md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/finishmatchmaking(for:))*
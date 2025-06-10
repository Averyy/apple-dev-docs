# addPlayers(to:matchRequest:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Invites additional players to an existing match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addPlayers(to match: GKMatch, matchRequest: GKMatchRequest) async throws
```

#### Discussion

Use this method to add more players to an existing match that doesn’t have enough players.

> ❗ **Important**:  Invoke this method for only one player connected to the match.

## Parameters

- `match`: The match to which GameKit adds the players.
- `matchRequest`: The configuration for the match.
- `completionHandler`: This block receives the following parameters:

## See Also

- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/findmatch(for:withcompletionhandler:).md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [class GKMatchedPlayers](gkmatchedplayers.md)
  An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.
- [func finishMatchmaking(for: GKMatch)](gkmatchmaker/finishmatchmaking(for:).md)
  Informs the server when programmatic matchmaking finishes.
- [func cancel()](gkmatchmaker/cancel.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](gkmatchmaker/cancelpendinginvite(to:).md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/addplayers(to:matchrequest:completionhandler:))*
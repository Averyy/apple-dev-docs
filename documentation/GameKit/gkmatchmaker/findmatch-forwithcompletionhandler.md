# findMatch(for:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Initiates a request to find players for a peer-to-peer match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func findMatch(for request: GKMatchRequest) async throws -> GKMatch
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](gkmatchrequest/queuename.md) and optionally, [`properties`](gkmatchrequest/properties.md)) before you call this method. For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: This block receives the following parameters:

## See Also

- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [class GKMatchedPlayers](gkmatchedplayers.md)
  An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.
- [func addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: (((any Error)?) -> Void)?)](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md)
  Invites additional players to an existing match.
- [func finishMatchmaking(for: GKMatch)](gkmatchmaker/finishmatchmaking(for:).md)
  Informs the server when programmatic matchmaking finishes.
- [func cancel()](gkmatchmaker/cancel.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](gkmatchmaker/cancelpendinginvite(to:).md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findmatch(for:withcompletionhandler:))*
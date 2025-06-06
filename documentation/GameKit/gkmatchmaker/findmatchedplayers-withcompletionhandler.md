# findMatchedPlayers(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Initiates a request to find players for a hosted match that uses matchmaking rules.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+

## Declaration

```swift
func findMatchedPlayers(_ request: GKMatchRequest) async throws -> GKMatchedPlayers
```

#### Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](gkmatchrequest/queuename.md) and optionally, [`properties`](gkmatchrequest/properties.md)) before you call this method. For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: This block receives the following parameters:

## See Also

- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/findmatch(for:withcompletionhandler:).md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findmatchedplayers(_:withcompletionhandler:))*
# findPlayers(forHostedRequest:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Initiates a request to find players for a hosted match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func findPlayers(forHostedRequest request: GKMatchRequest) async throws -> [GKPlayer]
```

#### Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](gkmatchrequest/queuename.md) and optionally, [`properties`](gkmatchrequest/properties.md)) before you call this method. To get the properties of all players who join the match, use the [`findMatchedPlayers(_:withCompletionHandler:)`](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md) method instead. For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: This block receives the following parameters:

## See Also

- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/findmatch(for:withcompletionhandler:).md)
  Initiates a request to find players for a peer-to-peer match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:))*
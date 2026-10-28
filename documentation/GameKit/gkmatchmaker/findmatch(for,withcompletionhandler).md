# findMatch(for:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func findMatch(for request: GKMatchRequest, withCompletionHandler completionHandler: (@Sendable (GKMatch?, (any Error)?) -> Void)? = nil)
```

```swift
func findMatch(for request: GKMatchRequest) async throws -> GKMatch
```

```objc
- (void) findMatchForRequest:(GKMatchRequest *) request withCompletionHandler:(void (^)(GKMatch *match, NSError *error)) completionHandler;
```

## Mentions

- [Finding multiple players for a game](../finding-multiple-players-for-a-game.md)
- [Finding players for custom server-based games](../finding-players-for-custom-server-based-games.md)

## Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](../gkmatchrequest/queuename.md) and optionally, [`properties`](../gkmatchrequest/properties.md)) before you call this method. For more information, see [Matchmaking rules](../matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`match`**: The match that the players join. If unsuccessful, this parameter is `nil`.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Matching players
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
- [func cancel()](./cancel%28%29.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](./cancelpendinginvite%28to%29.md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findmatch(for:withcompletionhandler:))*
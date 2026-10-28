# findPlayers(forHostedRequest:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func findPlayers(forHostedRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@Sendable ([GKPlayer]?, (any Error)?) -> Void)? = nil)
```

```swift
func findPlayers(forHostedRequest request: GKMatchRequest) async throws -> [GKPlayer]
```

```objc
- (void) findPlayersForHostedRequest:(GKMatchRequest *) request withCompletionHandler:(void (^)(NSArray<GKPlayer *> *players, NSError *error)) completionHandler;
```

## Mentions

- [Finding players for custom server-based games](../finding-players-for-custom-server-based-games.md)

## Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](../gkmatchrequest/queuename.md) and optionally, [`properties`](../gkmatchrequest/properties.md)) before you call this method. To get the properties of all players who join the match, use the [`findMatchedPlayers(_:withCompletionHandler:)`](./findmatchedplayers%28_,withcompletionhandler%29.md) method instead. For more information, see [Matchmaking rules](../matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`players`**: The players that join the match. If unsuccessful, this parameter is `nil`.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Matching players
- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](./findmatch%28for,withcompletionhandler%29.md)
  Initiates a request to find players for a peer-to-peer match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:))*
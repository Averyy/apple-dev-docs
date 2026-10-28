# findMatchedPlayers(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func findMatchedPlayers(_ request: GKMatchRequest, withCompletionHandler completionHandler: @escaping @Sendable (GKMatchedPlayers?, (any Error)?) -> Void)
```

```swift
func findMatchedPlayers(_ request: GKMatchRequest) async throws -> GKMatchedPlayers
```

```objc
- (void) findMatchedPlayers:(GKMatchRequest *) request withCompletionHandler:(void (^)(GKMatchedPlayers *matchedPlayers, NSError *error)) completionHandler;
```

## Mentions

- [Finding players for custom server-based games](../finding-players-for-custom-server-based-games.md)

## Discussion

To find players using matchmaking rules, set the rules-related properties in `request` ([`queueName`](../gkmatchrequest/queuename.md) and optionally, [`properties`](../gkmatchrequest/properties.md)) before you call this method. For more information, see [Matchmaking rules](../matchmaking-rules.md).

## Parameters

- `request`: The configuration for the match.
- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`matchedPlayers`**: The players that join the match, including their properties that matchmaking rules uses. If unsuccessful, this parameter is `nil`.
  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Matching players
- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](./findmatch%28for,withcompletionhandler%29.md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](./findplayers%28forhostedrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findmatchedplayers(_:withcompletionhandler:))*
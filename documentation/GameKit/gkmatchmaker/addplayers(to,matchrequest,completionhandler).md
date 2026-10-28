# addPlayers(to:matchRequest:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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
func addPlayers(to match: GKMatch, matchRequest: GKMatchRequest, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func addPlayers(to match: GKMatch, matchRequest: GKMatchRequest) async throws
```

```objc
- (void) addPlayersToMatch:(GKMatch *) match matchRequest:(GKMatchRequest *) matchRequest completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Finding players for custom server-based games](../finding-players-for-custom-server-based-games.md)

## Discussion

Use this method to add more players to an existing match that doesn’t have enough players.

> ❗ **Important**:  Invoke this method for only one player connected to the match.

## Parameters

- `match`: The match to which GameKit adds the players.
- `matchRequest`: The configuration for the match.
- `completionHandler`: The block that GameKit calls when it completes the request.

  This block receives the following parameters:

  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

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
- [func finishMatchmaking(for: GKMatch)](./finishmatchmaking%28for%29.md)
  Informs the server when programmatic matchmaking finishes.
- [func cancel()](./cancel%28%29.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](./cancelpendinginvite%28to%29.md)
  Cancels a pending invitation to another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/addplayers(to:matchrequest:completionhandler:))*
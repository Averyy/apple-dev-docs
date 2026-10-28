# startBrowsingForNearbyPlayers(reachableHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`startBrowsingForNearbyPlayers(handler:)`](./startbrowsingfornearbyplayers%28handler%29.md) method instead.

## Declaration

```swift
func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)? = nil)
```

```objc
- (void) startBrowsingForNearbyPlayersWithReachableHandler:(void (^)(NSString *playerID, BOOL reachable)) reachableHandler;
```

## Discussion

Use this method only when you are implementing programmatic matchmaking. After enabling browsing for nearby players, use the responses to populate your user interface with information about nearby players. If a player wants to invite a player to a game, add that player’s player identifier to a match request and call either the [`findMatch(for:withCompletionHandler:)`](./findmatch%28for,withcompletionhandler%29.md) to create a match or [`addPlayers(to:matchRequest:completionHandler:)`](./addplayers%28to,matchrequest,completionhandler%29.md) method to update a match.

## Parameters

- `reachableHandler`: A block to call when the reachability for a player changes. The block takes the following parameters:

  - ***playerID***: The player identifier for the player whose reachability status has changed.
  - ***reachable***: [`true`](../../Swift/true.md) if GameKit discovers a new player locally, [`false`](../../Swift/false.md) if a previously discovered player disappears.

## See Also

### Deprecated Methods
- [func cancelInvite(toPlayer: String)](./cancelinvite%28toplayer%29.md)
  Cancels a pending invitation to another player.
- [func findPlayers(forHostedMatchRequest: GKMatchRequest, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](./findplayers%28forhostedmatchrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/startbrowsingfornearbyplayers(reachablehandler:))*
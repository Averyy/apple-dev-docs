# startBrowsingForNearbyPlayers(reachableHandler:)

**Framework**: GameKit  
**Kind**: method

Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)? = nil)
```

#### Discussion

Use this method only when you are implementing programmatic matchmaking. After enabling browsing for nearby players, use the responses to populate your user interface with information about nearby players. If a player wants to invite a player to a game, add that player’s player identifier to a match request and call either the [`findMatch(for:withCompletionHandler:)`](gkmatchmaker/findmatch(for:withcompletionhandler:).md) to create a match or [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) method to update a match.

## Parameters

- `reachableHandler`: A block to call when the reachability for a player changes. The block takes the following parameters:

## See Also

- [func cancelInvite(toPlayer: String)](gkmatchmaker/cancelinvite(toplayer:).md)
  Cancels a pending invitation to another player.
- [func findPlayers(forHostedMatchRequest: GKMatchRequest, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedmatchrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/startbrowsingfornearbyplayers(reachablehandler:))*
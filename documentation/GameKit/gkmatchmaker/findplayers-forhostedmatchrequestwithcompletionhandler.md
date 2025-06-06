# findPlayers(forHostedMatchRequest:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Initiates a request to find players for a hosted match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func findPlayers(forHostedMatchRequest request: GKMatchRequest) async throws -> [String]
```

#### Discussion

When GameKit calls this completion handler, your game needs to connect those players to your own server.

On iOS 6, if the match request’s [`playersToInvite`](gkmatchrequest/playerstoinvite.md) property is non-`NIL`, Game Center only sends invitations out to the players listed in the property. If the [`playersToInvite`](gkmatchrequest/playerstoinvite.md) property is `NIL`, Game Center then searches for any waiting players that match the request. Prior to iOS 6, GameKit ignores the match request’s [`playersToInvite`](gkmatchrequest/playerstoinvite.md) property and this method only searches for available players.

## Parameters

- `request`: The configuration for the desired match.
- `completionHandler`: A block to call when GameKit creates the match. This block receives the following parameters:

## See Also

- [func cancel()](gkmatchmaker/cancel.md)
  Cancels a matchmaking request.
- [func cancelInvite(toPlayer: String)](gkmatchmaker/cancelinvite(toplayer:).md)
  Cancels a pending invitation to another player.
- [func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)?)](gkmatchmaker/startbrowsingfornearbyplayers(reachablehandler:).md)
  Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findplayers(forhostedmatchrequest:withcompletionhandler:))*
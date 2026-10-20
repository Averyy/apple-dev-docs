# cancelInvite(toPlayer:)

**Framework**: GameKit  
**Kind**: method

Cancels a pending invitation to another player.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
func cancelInvite(toPlayer playerID: String)
```

## Parameters

- `playerID`: The player identifier for a player that GameKit previously invited to the match.

## See Also

- [func findPlayers(forHostedMatchRequest: GKMatchRequest, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedmatchrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
- [func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)?)](gkmatchmaker/startbrowsingfornearbyplayers(reachablehandler:).md)
  Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/cancelinvite(toplayer:))*
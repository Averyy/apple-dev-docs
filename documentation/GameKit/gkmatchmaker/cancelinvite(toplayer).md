# cancelInvite(toPlayer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Cancels a pending invitation to another player.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`cancelPendingInvite(to:)`](./cancelpendinginvite%28to%29.md) method instead.

## Declaration

```swift
func cancelInvite(toPlayer playerID: String)
```

```objc
- (void) cancelInviteToPlayer:(NSString *) playerID;
```

## Parameters

- `playerID`: The player identifier for a player that GameKit previously invited to the match.

## See Also

### Deprecated Methods
- [func findPlayers(forHostedMatchRequest: GKMatchRequest, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](./findplayers%28forhostedmatchrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.
- [func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)?)](./startbrowsingfornearbyplayers%28reachablehandler%29.md)
  Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/cancelinvite(toplayer:))*
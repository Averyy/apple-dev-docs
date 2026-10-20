# findPlayers(forHostedMatchRequest:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Initiates a request to find players for a hosted match.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`findPlayers(forHostedRequest:withCompletionHandler:)`](./findplayers%28forhostedrequest,withcompletionhandler%29.md) method instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
func findPlayers(forHostedMatchRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@Sendable ([String]?, (any Error)?) -> Void)? = nil)
```

*Mac Catalyst, visionOS*

```swift
func findPlayers(forHostedMatchRequest request: GKMatchRequest) async throws -> [String]
```

```objc
- (void) findPlayersForHostedMatchRequest:(GKMatchRequest *) request withCompletionHandler:(void (^)(NSArray<NSString *> *playerIDs, NSError *error)) completionHandler;
```

#### Discussion

When GameKit calls this completion handler, your game needs to connect those players to your own server.

On iOS 6, if the match request’s [`playersToInvite`](../gkmatchrequest/playerstoinvite.md) property is non-`NIL`, Game Center only sends invitations out to the players listed in the property. If the [`playersToInvite`](../gkmatchrequest/playerstoinvite.md) property is `NIL`, Game Center then searches for any waiting players that match the request. Prior to iOS 6, GameKit ignores the match request’s [`playersToInvite`](../gkmatchrequest/playerstoinvite.md) property and this method only searches for available players.

## Parameters

- `request`: The configuration for the desired match.
- `completionHandler`: A block to call when GameKit creates the match. This block receives the following parameters:

  - ***playerIDs***: If matchmaking was successful, this parameter contains an array of `NSString` objects containing the players to connect into the match. Otherwise, this parameter is `nil`.
  - ***error***: If matchmaking was successful, this parameter contains `nil`. Otherwise, this parameter holds an error object that describes the error that occurred.

## See Also

### Related Documentation
- [func cancel()](./cancel%28%29.md)
  Cancels a matchmaking request.
### Deprecated Methods
- [func cancelInvite(toPlayer: String)](./cancelinvite%28toplayer%29.md)
  Cancels a pending invitation to another player.
- [func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)?)](./startbrowsingfornearbyplayers%28reachablehandler%29.md)
  Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/findplayers(forhostedmatchrequest:withcompletionhandler:))*
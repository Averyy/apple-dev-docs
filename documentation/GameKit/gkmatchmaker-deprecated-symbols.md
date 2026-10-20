# Deprecated Symbols

**Framework**: GameKit  
**Role**: API Collection

## Topics

### Deprecated Properties
- [var inviteHandler: ((GKInvite, [Any]?) -> Void)?](./gkmatchmaker/invitehandler.md)
  A block that GameKit calls when an invitation to join a match is accepted by the local player.
### Deprecated Methods
- [func cancelInvite(toPlayer: String)](./gkmatchmaker/cancelinvite%28toplayer%29.md)
  Cancels a pending invitation to another player.
- [func findPlayers(forHostedMatchRequest: GKMatchRequest, withCompletionHandler: (([String]?, (any Error)?) -> Void)?)](./gkmatchmaker/findplayers%28forhostedmatchrequest,withcompletionhandler%29.md)
  Initiates a request to find players for a hosted match.
- [func startBrowsingForNearbyPlayers(reachableHandler: ((String, Bool) -> Void)?)](./gkmatchmaker/startbrowsingfornearbyplayers%28reachablehandler%29.md)
  Enables the matchmaking process to find nearby players through Bluetooth or WiFi, but only on the same subnet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker-deprecated-symbols)*
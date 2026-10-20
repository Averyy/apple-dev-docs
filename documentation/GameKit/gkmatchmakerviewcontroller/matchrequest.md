# matchRequest

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The configuration for the desired match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var matchRequest: GKMatchRequest { get }
```

```objc
@property (nonatomic, strong, readonly) GKMatchRequest * matchRequest;
```

## See Also

### Creating and configuring the view controller
- [init?(matchRequest: GKMatchRequest)](./init%28matchrequest%29.md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](./init%28invite%29.md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var canStartWithMinimumPlayers: Bool](./canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [var matchmakingMode: GKMatchmakingMode](./matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](../gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/matchrequest)*
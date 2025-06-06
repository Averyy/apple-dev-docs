# matchRequest

**Framework**: GameKit  
**Kind**: property

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
@MainActor
var matchRequest: GKMatchRequest { get }
```

## See Also

- [init?(matchRequest: GKMatchRequest)](gkmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](gkmatchmakerviewcontroller/init(invite:).md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var canStartWithMinimumPlayers: Bool](gkmatchmakerviewcontroller/canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [var matchmakingMode: GKMatchmakingMode](gkmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/matchrequest)*
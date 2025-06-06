# matchmakingMode

**Framework**: GameKit  
**Kind**: property

The mode that a multiplayer game uses to find players.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var matchmakingMode: GKMatchmakingMode { get set }
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

This method throws an exception if the mode isn’t possible due to restrictions.

## See Also

- [init?(matchRequest: GKMatchRequest)](gkmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](gkmatchmakerviewcontroller/init(invite:).md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](gkmatchmakerviewcontroller/matchrequest.md)
  The configuration for the desired match.
- [var canStartWithMinimumPlayers: Bool](gkmatchmakerviewcontroller/canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/matchmakingmode)*
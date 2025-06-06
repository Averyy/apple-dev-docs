# canStartWithMinimumPlayers

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether your game can start after a minimum number of players join a match.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canStartWithMinimumPlayers: Bool { get set }
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

If you set this property to [`true`](https://developer.apple.com/documentation/swift/true), players can optionally start a multiplayer game when the minimum number of players accept their invitations. Design your game to progressively add additional players up to the maximum number of players. The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

To set the minimum and maximum number of players, see [`Create a match request`](finding-multiple-players-for-a-game#Create-a-match-request.md).

## See Also

- [init?(matchRequest: GKMatchRequest)](gkmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](gkmatchmakerviewcontroller/init(invite:).md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](gkmatchmakerviewcontroller/matchrequest.md)
  The configuration for the desired match.
- [var matchmakingMode: GKMatchmakingMode](gkmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/canstartwithminimumplayers)*
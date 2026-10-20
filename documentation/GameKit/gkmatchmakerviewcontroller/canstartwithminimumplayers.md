# canStartWithMinimumPlayers

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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
var canStartWithMinimumPlayers: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL canStartWithMinimumPlayers;
```

## Mentions

- [Finding multiple players for a game](../finding-multiple-players-for-a-game.md)

#### Discussion

If you set this property to [`true`](../../Swift/true.md), players can optionally start a multiplayer game when the minimum number of players accept their invitations. Design your game to progressively add additional players up to the maximum number of players. The default value for this property is [`false`](../../Swift/false.md).

To set the minimum and maximum number of players, see [Create a match request](../finding-multiple-players-for-a-game.md#Create-a-match-request).

## See Also

### Creating and configuring the view controller
- [init?(matchRequest: GKMatchRequest)](./init%28matchrequest%29.md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](./init%28invite%29.md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](./matchrequest.md)
  The configuration for the desired match.
- [var matchmakingMode: GKMatchmakingMode](./matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](../gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/canstartwithminimumplayers)*
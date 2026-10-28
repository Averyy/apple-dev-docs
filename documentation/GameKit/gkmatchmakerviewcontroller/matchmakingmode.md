# matchmakingMode

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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
var matchmakingMode: GKMatchmakingMode { get set }
```

```objc
@property (nonatomic, assign) GKMatchmakingMode matchmakingMode;
```

## Mentions

- [Finding multiple players for a game](../finding-multiple-players-for-a-game.md)

## Discussion

This method throws an exception if the mode isn’t possible due to restrictions.

## See Also

### Creating and configuring the view controller
- [init?(matchRequest: GKMatchRequest)](./init%28matchrequest%29.md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](./init%28invite%29.md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](./matchrequest.md)
  The configuration for the desired match.
- [var canStartWithMinimumPlayers: Bool](./canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [enum GKMatchmakingMode](../gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/matchmakingmode)*
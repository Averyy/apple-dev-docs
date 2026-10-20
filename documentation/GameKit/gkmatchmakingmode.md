# GKMatchmakingMode

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Possible modes that a multiplayer game uses to find matches.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum GKMatchmakingMode
```

```c
enum GKMatchmakingMode : NSInteger;
```

## Topics

### Modes
- [GKMatchmakingMode.default](./gkmatchmakingmode/default.md)
  The default matchmaking mode.
- [GKMatchmakingMode.nearbyOnly](./gkmatchmakingmode/nearbyonly.md)
  A mode that matches the local player only with nearby players.
- [GKMatchmakingMode.automatchOnly](./gkmatchmakingmode/automatchonly.md)
  A mode that matches the local player only with players who are also actively looking for a match.
- [GKMatchmakingMode.inviteOnly](./gkmatchmakingmode/inviteonly.md)
  A mode that matches the local player only with players who they invite, and doesn’t use automatch to fill empty slots.
### Initializers
- [init?(rawValue: Int)](./gkmatchmakingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating and configuring the view controller
- [init?(matchRequest: GKMatchRequest)](./gkmatchmakerviewcontroller/init%28matchrequest%29.md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](./gkmatchmakerviewcontroller/init%28invite%29.md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](./gkmatchmakerviewcontroller/matchrequest.md)
  The configuration for the desired match.
- [var canStartWithMinimumPlayers: Bool](./gkmatchmakerviewcontroller/canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [var matchmakingMode: GKMatchmakingMode](./gkmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakingmode)*
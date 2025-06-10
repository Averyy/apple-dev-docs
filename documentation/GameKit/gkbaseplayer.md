# GKBasePlayer

**Framework**: GameKit  
**Kind**: class

A class that provides common data and methods for the different player objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKBasePlayer
```

#### Overview

[`GKBasePlayer`](gkbaseplayer.md) is the abstract superclass for the classes that represent the local player running your app and remote players who may join their games. Use the [`GKLocalPlayer`](gklocalplayer.md) subclass to initialize the local player who runs your app on their device. Then you can access the local player’s nickname, avatar, leaderboards, and achievements. You can also invite other players ([`GKPlayer`](gkplayer.md) objects), and send information between players.

## Topics

### Identifying a Player
- [var displayName: String?](gkbaseplayer/displayname.md)
  The Game Center profile name for a player.
- [var playerID: String?](gkbaseplayer/playerid.md)
  A unique identifier for a player.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKCloudPlayer](gkcloudplayer.md)
- [GKPlayer](gkplayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)
  Give players the ability to connect and interact with friends in your game.
- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md)
  Use the scoped identifiers that GameKit provides you as player IDs when transmitting or saving player data.
- [class GKLocalPlayer](gklocalplayer.md)
  The local player who signs in to Game Center on the device running the game.
- [class GKPlayer](gkplayer.md)
  A remote player who the local player running your game can invite and communicate with through Game Center.
- [protocol GKLocalPlayerListener](gklocalplayerlistener.md)
  A protocol that handles events for Game Center players.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerAuthenticationDidChangeNotificationName.md)
  A notification that posts after GameKit authenticates the local player.
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerDidChangeNotificationName.md)
  A notification that posts when a player object’s data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkbaseplayer)*
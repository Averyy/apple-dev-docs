# GKLocalPlayerListener

**Framework**: GameKit  
**Kind**: protocol

A protocol that handles events for Game Center players.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKLocalPlayerListener : GKChallengeListener, GKInviteEventListener, GKTurnBasedEventListener
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Overview

Adopt the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol to listen for and handle a variety of Game Center events for player accounts instead of the individual [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocols.

## Relationships

### Inherits From
- [GKChallengeListener](gkchallengelistener.md)
- [GKGameActivityListener](gkgameactivitylistener.md)
- [GKInviteEventListener](gkinviteeventlistener.md)
- [GKSavedGameListener](gksavedgamelistener.md)
- [GKTurnBasedEventListener](gkturnbasedeventlistener.md)
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
- [class GKBasePlayer](gkbaseplayer.md)
  A class that provides common data and methods for the different player objects.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerAuthenticationDidChangeNotificationName.md)
  A notification that posts after GameKit authenticates the local player.
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerDidChangeNotificationName.md)
  A notification that posts when a player object’s data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener)*
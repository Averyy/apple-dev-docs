# GKPlayer

**Framework**: GameKit  
**Kind**: class

A remote player who the local player running your game can invite and communicate with through Game Center.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKPlayer
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md)
- [Authenticating a player](authenticating-a-player.md)

#### Overview

Before using Game Center for the first time, players create a single account that identifies them across all Game Center games. The player only needs to sign in to Game Center once per device to start using GameKit features in your game. A player sets a nickname and avatar in their account that provide a consistent and familiar look in your game. Game Center then uses the account to record leaderboard scores and achievements, and to start games with other players.

In your code, [`GKPlayer`](gkplayer.md) represents remote or other players who the local player running your app can invite and communicate with. [`GKPlayer`](gkplayer.md) is also the superclass for the local player [`GKLocalPlayer`](gklocalplayer.md) class that provides common data and methods for all players. For example, use the [`alias`](gkplayer/alias.md) property to get the nickname for a player. To load the player avatars, use the [`loadPhoto(for:withCompletionHandler:)`](gkplayer/loadphoto(for:withcompletionhandler:).md) method.

To create a guest player who doesn’t have a Game Center account, use the [`anonymousGuestPlayer(withIdentifier:)`](gkplayer/anonymousguestplayer(withidentifier:).md) method. GameKit treats guest players similar to Game Center players except they can’t earn achievements, post to leaderboards, or participate in challenges.

Use the [`gamePlayerID`](gkplayer/gameplayerid.md) property as a unique identifier for just your game, and the [`teamPlayerID`](gkplayer/teamplayerid.md) property as a unique identifier for all games that you offer through your developer account. For more information, see [`Protecting the player’s privacy using scoped identifiers`](protecting-the-player-s-privacy-using-scoped-identifiers.md).

## Topics

### Identifying the player
- [var gamePlayerID: String](gkplayer/gameplayerid.md)
  A unique identifier for a player of the game.
- [var teamPlayerID: String](gkplayer/teamplayerid.md)
  A unique identifier for a player of all the games that you distribute using your developer account.
- [func scopedIDsArePersistent() -> Bool](gkplayer/scopedidsarepersistent.md)
  Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.
- [let GKPlayerIDNoLongerAvailable: String](gkplayeridnolongeravailable.md)
  A constant for a player ID that’s no longer available.
- [var playerID: String](gkplayer/playerid.md)
  A unique identifier for a player of the game.
### Accessing player details
- [var alias: String](gkplayer/alias.md)
  A string the player chooses to identify themself to other players.
- [var displayName: String](gkplayer/displayname.md)
  A string to display for the player.
- [var isInvitable: Bool](gkplayer/isinvitable.md)
  A Boolean value that indicates whether the local player can send an invitation to the player.
- [var isFriend: Bool](gkplayer/isfriend.md)
  A Boolean value that indicates whether the player is a friend of the local player.
### Loading player photos
- [func loadPhoto(for: GKPlayer.PhotoSize, withCompletionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkplayer/loadphoto(for:withcompletionhandler:).md)
  Loads a photo of the player from Game Center.
- [GKPlayer.PhotoSize](gkplayer/photosize.md)
  The size of a photo that Game Center loads.
### Creating a guest player
- [class func anonymousGuestPlayer(withIdentifier: String) -> Self](gkplayer/anonymousguestplayer(withidentifier:).md)
  Creates a guest player with the specified identifier.
- [var guestIdentifier: String?](gkplayer/guestidentifier.md)
  A developer-created string that identifies a guest player.
### Observing notifications
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerDidChangeNotificationName.md)
  A notification that posts when a player object’s data changes.
### Loading player details
- [class func loadPlayers(forIdentifiers: [String], withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkplayer/loadplayers(foridentifiers:withcompletionhandler:).md)
  Loads information about a list of players from Game Center.

## Relationships

### Inherits From
- [GKBasePlayer](gkbaseplayer.md)
### Inherited By
- [GKLocalPlayer](gklocalplayer.md)
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
- [class GKBasePlayer](gkbaseplayer.md)
  A class that provides common data and methods for the different player objects.
- [protocol GKLocalPlayerListener](gklocalplayerlistener.md)
  A protocol that handles events for Game Center players.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerAuthenticationDidChangeNotificationName.md)
  A notification that posts after GameKit authenticates the local player.
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GKPlayerDidChangeNotificationName.md)
  A notification that posts when a player object’s data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer)*
# Protecting the player’s privacy using scoped identifiers

**Framework**: GameKit

Use the scoped identifiers that GameKit provides you as player IDs when transmitting or saving player data.

#### Overview

If you store player data outside of Game Center, use the scoped player identifiers that GameKit provides for you to identify the local player’s data — not their name and avatar, which may change, or other personal information that’s private. The identifiers that Game Center provides are persistent and scoped to your game instances.

GameKit scopes the identifiers of other players in the game instance to each leaderboard object or to each multiplayer match object, not your game instances (except for friend identifiers as described below). Therefore, in a multiplayer game, save the game data for the local player only, not the data for the other players in the match.

For design guidance on protecting the player’s privacy, see [`Human Interface Guidelines > Privacy`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/privacy).

##### Authenticate the Local Player

Before you can get a scoped identifier, authenticate the local player who is running your game on the device. During the authentication process, the player signs in to their Game Center account if they haven’t already done so. Identifiers for an authenticated player are persistent; that is, the values are the same across all instances of your game. For more information, see [`Authenticating a player`](authenticating-a-player.md).

##### Get the Local Players Scoped Identifier

After authentication, you can get a unique identifier for the local player from the [`GKLocalPlayer`](gklocalplayer.md) shared object using the [`gamePlayerID`](gkplayer/gameplayerid.md) property:

```swift
// Get the scoped local player identifier.
let identifier = GKLocalPlayer.local.gamePlayerID
```

If you need to track a player across multiple games belonging to your developer team, you can use the [`teamPlayerID`](gkplayer/teamplayerid.md) property instead. Game Center scopes this property to instances of all games that use the same Team ID. But if you transfer your game to another team, the value of the [`teamPlayerID`](gkplayer/teamplayerid.md) property changes.

If you use either the [`teamPlayerID`](gkplayer/teamplayerid.md) or the deprecated, non-scoped [`playerID`](gkplayer/playerid.md) property, you need to provide details on your game’s privacy practices in App Store Connect. To learn more, see [`App privacy details on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/#data-type).

If authentication fails, the [`gamePlayerID`](gkplayer/gameplayerid.md) and [`teamPlayerID`](gkplayer/teamplayerid.md) properties return a temporary identifier that’s not persistent. If you need unique and persistent identifiers, use the [`scopedIDsArePersistent()`](gkplayer/scopedidsarepersistent().md) method before accessing the properties. Don’t rely on the format of the identifiers to determine whether they’re persistent.

Later, you can use either the [`gamePlayerID`](gkplayer/gameplayerid.md) or the [`teamPlayerID`](gkplayer/teamplayerid.md) values in GameKit calls to identify the player.

##### Get Scoped Identifiers for Friends of the Local Player

If you have permission from the local player to access their friends list, you can also get scoped identifiers for their friends. The friend identifiers are persistent and scoped to game instances the local player and their friends run.

You get the scoped identifiers for the friends from the [`GKPlayer`](gkplayer.md) objects that the [`loadFriends(_:)`](gklocalplayer/loadfriends(_:).md) method returns using the [`gamePlayerID`](gkplayer/gameplayerid.md) property. In the game instances that mutual friends run, the identifiers for the [`GKPlayer`](gkplayer.md) objects that the [`loadFriends(_:)`](gklocalplayer/loadfriends(_:).md) method returns are the same:

```swift
// Load the local player's friends.
let players = try await GKLocalPlayer.local.loadFriends()

// Get scoped identifiers for the mutual friends.
for player in players {
    let let identifier = player.gamePlayerID
    // Save or use the scoped identifiers.
}
```

For details on loading the local player’s friends, see [`Providing a reason to access the friends list`](connecting-players-with-their-friends-in-your-game#Providing-a-reason-to-access-the-friends-list.md) and [`Accessing the player’s friends`](connecting-players-with-their-friends-in-your-game#Accessing-the-players-friends.md).

## See Also

- [Connecting players with their friends in your game](connecting-players-with-their-friends-in-your-game.md)
  Give players the ability to connect and interact with friends in your game.
- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [class GKLocalPlayer](gklocalplayer.md)
  The local player who signs in to Game Center on the device running the game.
- [class GKPlayer](gkplayer.md)
  A remote player who the local player running your game can invite and communicate with through Game Center.
- [class GKBasePlayer](gkbaseplayer.md)
  A class that provides common data and methods for the different player objects.
- [protocol GKLocalPlayerListener](gklocalplayerlistener.md)
  A protocol that handles events for Game Center players.
- [static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name](../foundation/nsnotification/name/1515396-gkplayerauthenticationdidchangen.md)
  A notification that posts after GameKit authenticates the local player. 
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](../foundation/nsnotification/name/1520710-gkplayerdidchangenotificationnam.md)
  A notification that posts when a player object’s data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/protecting-the-player-s-privacy-using-scoped-identifiers)*
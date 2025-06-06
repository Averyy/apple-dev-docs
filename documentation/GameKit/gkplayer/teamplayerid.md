# teamPlayerID

**Framework**: GameKit  
**Kind**: property

A unique identifier for a player of all the games that you distribute using your developer account.

**Availability**:
- iOS 12.4+
- iPadOS 12.4+
- Mac Catalyst 13.1+
- macOS 10.14.6+
- tvOS 12.4+
- visionOS 1.0+

## Declaration

```swift
var teamPlayerID: String { get }
```

## Mentions

- [Protecting the player’s privacy using scoped identifiers](protecting-the-player-s-privacy-using-scoped-identifiers.md)

#### Discussion

This identifier is unique to this game instance if the [`scopedIDsArePersistent()`](gkplayer/scopedidsarepersistent().md) method returns [`false`](https://developer.apple.com/documentation/swift/false). Otherwise, this identifier is the same across all game instances of your games that use the same developer Team ID. An instance is the time between when the game launches and when the game terminates. For more information about the Team ID, see [`Locate your Team ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

For the local player (a [`GKLocalPlayer`](gklocalplayer.md) object), this identifier is the same across all local player instances of your games. If the player is friends with the local player, this identifier is the same across all local player and friend game instances. To determine whether the player is a friend, use the [`loadFriends(_:)`](gklocalplayer/loadfriends(_:).md) method.

To protect the player’s privacy, use the [`gamePlayerID`](gkplayer/gameplayerid.md) property instead of the [`teamPlayerID`](gkplayer/teamplayerid.md) property. If you need to use the [`teamPlayerID`](gkplayer/teamplayerid.md) for tracking players across multiple games, also store the [`gamePlayerID`](gkplayer/gameplayerid.md) property. For more information, see [`Protecting the player’s privacy using scoped identifiers`](protecting-the-player-s-privacy-using-scoped-identifiers.md).

If you transfer your game to another developer, the [`teamPlayerID`](gkplayer/teamplayerid.md) property isn’t the same for the new developer. For more information, see [`Overview of app transfer`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/transfer-an-app/overview-of-app-transfer).

## See Also

- [var gamePlayerID: String](gkplayer/gameplayerid.md)
  A unique identifier for a player of the game.
- [func scopedIDsArePersistent() -> Bool](gkplayer/scopedidsarepersistent.md)
  Returns a Boolean value depending on whether the player identifiers are persistent across game instances or unique to the game instance.
- [let GKPlayerIDNoLongerAvailable: String](gkplayeridnolongeravailable.md)
  A constant for a player ID that’s no longer available.
- [var playerID: String](gkplayer/playerid.md)
  A unique identifier for a player of the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/teamplayerid)*
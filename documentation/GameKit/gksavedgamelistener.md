# GKSavedGameListener

**Framework**: GameKit  
**Kind**: protocol

A protocol that handles events related to saving game data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
protocol GKSavedGameListener : NSObjectProtocol
```

#### Overview

Implement the methods in the this protocol to manage conflicts or track changes when saving game data.

Adopt the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol to listen for and handle a variety of Game Center events for player accounts instead of the individual [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocols.

## Topics

### Handling Saved Game Conflicts
- [func player(GKPlayer, hasConflictingSavedGames: [GKSavedGame])](gksavedgamelistener/player(_:hasconflictingsavedgames:).md)
  Chooses the correct game data from the saved games that contain conflicts.
### Handling Saved Game Changes
- [func player(GKPlayer, didModifySavedGame: GKSavedGame)](gksavedgamelistener/player(_:didmodifysavedgame:).md)
  Handles when data changes in a saved game file.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)
### Conforming Types
- [GKLocalPlayer](gklocalplayer.md)

## See Also

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func saveGameData(Data, withName: String, completionHandler: ((GKSavedGame?, (any Error)?) -> Void)?)](gklocalplayer/savegamedata(_:withname:completionhandler:).md)
  Saves game data with the specified name.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/fetchsavedgames(completionhandler:).md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/resolveconflictingsavedgames(_:with:completionhandler:).md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [func deleteSavedGames(withName: String, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/deletesavedgames(withname:completionhandler:).md)
  Deletes saved games with the specified filename.
- [class GKSavedGame](gksavedgame.md)
  An object that represents a file containing saved game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgamelistener)*
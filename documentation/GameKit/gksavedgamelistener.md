# GKSavedGameListener

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol GKSavedGameListener <NSObject>
```

#### Overview

Implement the methods in the this protocol to manage conflicts or track changes when saving game data.

Adopt the [`GKLocalPlayerListener`](./gklocalplayerlistener.md) protocol to listen for and handle a variety of Game Center events for player accounts instead of the individual [`GKChallengeListener`](./gkchallengelistener.md), [`GKInviteEventListener`](./gkinviteeventlistener.md), [`GKSavedGameListener`](./gksavedgamelistener.md), and [`GKTurnBasedEventListener`](./gkturnbasedeventlistener.md) protocols.

## Topics

### Handling Saved Game Conflicts
- [func player(GKPlayer, hasConflictingSavedGames: [GKSavedGame])](./gksavedgamelistener/player%28_,hasconflictingsavedgames%29.md)
  Chooses the correct game data from the saved games that contain conflicts.
### Handling Saved Game Changes
- [func player(GKPlayer, didModifySavedGame: GKSavedGame)](./gksavedgamelistener/player%28_,didmodifysavedgame%29.md)
  Handles when data changes in a saved game file.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [GKLocalPlayerListener](./gklocalplayerlistener.md)
### Conforming Types
- [GKLocalPlayer](./gklocalplayer.md)

## See Also

### Saving Game Data
- [Saving the player’s game data to an iCloud account](./saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func saveGameData(Data, withName: String, completionHandler: ((GKSavedGame?, (any Error)?) -> Void)?)](./gklocalplayer/savegamedata%28_,withname,completionhandler%29.md)
  Saves game data with the specified name.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./gklocalplayer/fetchsavedgames%28completionhandler%29.md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./gklocalplayer/resolveconflictingsavedgames%28_,with,completionhandler%29.md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [func deleteSavedGames(withName: String, completionHandler: (((any Error)?) -> Void)?)](./gklocalplayer/deletesavedgames%28withname,completionhandler%29.md)
  Deletes saved games with the specified filename.
- [class GKSavedGame](./gksavedgame.md)
  An object that represents a file containing saved game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgamelistener)*
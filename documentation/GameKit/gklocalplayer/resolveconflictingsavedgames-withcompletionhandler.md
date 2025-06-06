# resolveConflictingSavedGames(_:with:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Replaces duplicate saved games that use the same filename with one file containing the specified game data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], with data: Data) async throws -> [GKSavedGame]
```

## Mentions

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)

#### Discussion

Implement the [`player(_:hasConflictingSavedGames:)`](gksavedgamelistener/player(_:hasconflictingsavedgames:).md) protocol method to choose the correct game data when there’s a conflict. Then call this method separately for each set of saved games that contain file conflicts. For example, if multiple saved games use the `savedgame1` and `savedgame2` filenames, call this method once for the saved games that use the `savedgame1` filename, and once for the saved games that use the `savedgame2` filename.

## Parameters

- `conflictingSavedGames`: The saved games that contain the conflicts.
- `data`: The correct game data to save.
- `handler`: For example, if there are five saved game files with the same filename, but only three are in  , this parameter contains the three saved games you provide and the two saved games GameKit finds.

## See Also

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func saveGameData(Data, withName: String, completionHandler: ((GKSavedGame?, (any Error)?) -> Void)?)](gklocalplayer/savegamedata(_:withname:completionhandler:).md)
  Saves game data with the specified name.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/fetchsavedgames(completionhandler:).md)
  Retrieves all available saved games.
- [func deleteSavedGames(withName: String, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/deletesavedgames(withname:completionhandler:).md)
  Deletes saved games with the specified filename.
- [class GKSavedGame](gksavedgame.md)
  An object that represents a file containing saved game data.
- [protocol GKSavedGameListener](gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/resolveconflictingsavedgames(_:with:completionhandler:))*
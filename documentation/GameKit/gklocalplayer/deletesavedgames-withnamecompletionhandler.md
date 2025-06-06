# deleteSavedGames(withName:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Deletes saved games with the specified filename.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func deleteSavedGames(withName name: String) async throws
```

## Mentions

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)

#### Discussion

Alternatively, use the [`resolveConflictingSavedGames(_:with:completionHandler:)`](gklocalplayer/resolveconflictingsavedgames(_:with:completionhandler:).md) method to keep one of the saved games that use the same filename.

## Parameters

- `name`: A string that identifies the saved game data to delete.
- `handler`: The block receives the following parameters:

## See Also

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func saveGameData(Data, withName: String, completionHandler: ((GKSavedGame?, (any Error)?) -> Void)?)](gklocalplayer/savegamedata(_:withname:completionhandler:).md)
  Saves game data with the specified name.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/fetchsavedgames(completionhandler:).md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/resolveconflictingsavedgames(_:with:completionhandler:).md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [class GKSavedGame](gksavedgame.md)
  An object that represents a file containing saved game data.
- [protocol GKSavedGameListener](gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/deletesavedgames(withname:completionhandler:))*
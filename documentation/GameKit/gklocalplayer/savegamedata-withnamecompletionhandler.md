# saveGameData(_:withName:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Saves game data with the specified name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func saveGameData(_ data: Data, withName name: String) async throws -> GKSavedGame
```

## Mentions

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)

#### Discussion

If the `name` parameter is an existing filename, GameKit overwrites the file with the new game data.

> ❗ **Important**:  You must provide an iCloud container ID in your project to save game data to the player’s iCloud account. Add the [`iCloud Container Identifiers Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.icloud-container-identifiers) key to your project containing a unique identifier for your game.

 You must provide an iCloud container ID in your project to save game data to the player’s iCloud account. Add the [`iCloud Container Identifiers Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.icloud-container-identifiers) key to your project containing a unique identifier for your game.

## Parameters

- `data`: An object that contains the saved game data.
- `name`: A unique filename for the saved game data.
- `handler`: The block receives the following parameters:

## See Also

- [Saving the player’s game data to an iCloud account](saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/fetchsavedgames(completionhandler:).md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](gklocalplayer/resolveconflictingsavedgames(_:with:completionhandler:).md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [func deleteSavedGames(withName: String, completionHandler: (((any Error)?) -> Void)?)](gklocalplayer/deletesavedgames(withname:completionhandler:).md)
  Deletes saved games with the specified filename.
- [class GKSavedGame](gksavedgame.md)
  An object that represents a file containing saved game data.
- [protocol GKSavedGameListener](gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/savegamedata(_:withname:completionhandler:))*
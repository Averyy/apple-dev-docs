# saveGameData(_:withName:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Saves game data with the specified name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func saveGameData(_ data: Data, withName name: String, completionHandler handler: (@Sendable (GKSavedGame?, (any Error)?) -> Void)? = nil)
```

```swift
func saveGameData(_ data: Data, withName name: String) async throws -> GKSavedGame
```

```objc
- (void) saveGameData:(NSData *) data withName:(NSString *) name completionHandler:(void (^)(GKSavedGame *savedGame, NSError *error)) handler;
```

## Mentions

- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)

## Discussion

If the `name` parameter is an existing filename, GameKit overwrites the file with the new game data.

> ❗ **Important**:  You must provide an iCloud container ID in your project to save game data to the player’s iCloud account. Add the [`iCloud Container Identifiers Entitlement`](../../BundleResources/entitlements/com.apple.developer.icloud-container-identifiers.md) key to your project containing a unique identifier for your game.

## Parameters

- `data`: An object that contains the saved game data.
- `name`: A unique filename for the saved game data.
- `handler`: The block that this method calls when it completes the request.

  The block receives the following parameters:

  - **savedGame**: The saved game.
  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Saving Game Data
- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./fetchsavedgames%28completionhandler%29.md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./resolveconflictingsavedgames%28_,with,completionhandler%29.md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [func deleteSavedGames(withName: String, completionHandler: (((any Error)?) -> Void)?)](./deletesavedgames%28withname,completionhandler%29.md)
  Deletes saved games with the specified filename.
- [class GKSavedGame](../gksavedgame.md)
  An object that represents a file containing saved game data.
- [protocol GKSavedGameListener](../gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/savegamedata(_:withname:completionhandler:))*
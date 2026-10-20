# deleteSavedGames(withName:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Deletes saved games with the specified filename.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func deleteSavedGames(withName name: String, completionHandler handler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func deleteSavedGames(withName name: String) async throws
```

```objc
- (void) deleteSavedGamesWithName:(NSString *) name completionHandler:(void (^)(NSError *error)) handler;
```

## Mentions

- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)

#### Discussion

Alternatively, use the [`resolveConflictingSavedGames(_:with:completionHandler:)`](./resolveconflictingsavedgames%28_,with,completionhandler%29.md) method to keep one of the saved games that use the same filename.

## Parameters

- `name`: A string that identifies the saved game data to delete.
- `handler`: The block that this method calls when it completes the request.

  The block receives the following parameters:

  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Saving Game Data
- [Saving the player’s game data to an iCloud account](../saving-the-player-s-game-data-to-an-icloud-account.md)
  Save game data during play or after a game in the player’s iCloud account that’s accessible from any device.
- [func saveGameData(Data, withName: String, completionHandler: ((GKSavedGame?, (any Error)?) -> Void)?)](./savegamedata%28_,withname,completionhandler%29.md)
  Saves game data with the specified name.
- [func fetchSavedGames(completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./fetchsavedgames%28completionhandler%29.md)
  Retrieves all available saved games.
- [func resolveConflictingSavedGames([GKSavedGame], with: Data, completionHandler: (([GKSavedGame]?, (any Error)?) -> Void)?)](./resolveconflictingsavedgames%28_,with,completionhandler%29.md)
  Replaces duplicate saved games that use the same filename with one file containing the specified game data.
- [class GKSavedGame](../gksavedgame.md)
  An object that represents a file containing saved game data.
- [protocol GKSavedGameListener](../gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/deletesavedgames(withname:completionhandler:))*
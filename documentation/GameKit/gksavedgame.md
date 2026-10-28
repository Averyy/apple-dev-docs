# GKSavedGame

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

An object that represents a file containing saved game data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
class GKSavedGame
```

```objc
@interface GKSavedGame : NSObject
```

## Mentions

- [Saving the player’s game data to an iCloud account](./saving-the-player-s-game-data-to-an-icloud-account.md)

## Overview

A `GKSavedGame` object represents the file that contains game data you saved using the `GKLocalPlayer` [`saveGameData(_:withName:completionHandler:)`](./gklocalplayer/savegamedata%28_,withname,completionhandler%29.md) method.

You don’t create `GKSavedGame` objects directly. Instead use the [`fetchSavedGames(completionHandler:)`](./gklocalplayer/fetchsavedgames%28completionhandler%29.md) method to get the games you saved. Then get the filename, its modification date, and the name of the device the player used to save the game from the returned objects.

Use the [`loadData(completionHandler:)`](./gksavedgame/loaddata%28completionhandler%29.md) method to get the actual game data you saved in the file. To delete saved games, use the [`deleteSavedGames(withName:completionHandler:)`](./gklocalplayer/deletesavedgames%28withname,completionhandler%29.md) method.

## Topics

### Loading Saved Game Data
- [func loadData(completionHandler: ((Data?, (any Error)?) -> Void)?)](./gksavedgame/loaddata%28completionhandler%29.md)
  Loads the game data from the file.
### Retrieving Information About a Saved Game File
- [var name: String?](./gksavedgame/name.md)
  The name of the saved game.
- [var modificationDate: Date?](./gksavedgame/modificationdate.md)
  The date when you saved the game data or modified it.
- [var deviceName: String?](./gksavedgame/devicename.md)
  The name of the device that the player uses to save the game.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [protocol GKSavedGameListener](./gksavedgamelistener.md)
  A protocol that handles events related to saving game data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgame)*
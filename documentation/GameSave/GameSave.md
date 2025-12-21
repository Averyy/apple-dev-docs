# GameSave

**Framework**: GameSave  
**Kind**: module

Store and sync your application’s save files in iCloud.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

#### Overview

GameSave uses iCloud Drive to synchronize your application’s save data across devices. The framework provides a set of APIs for reading and writing one or more files to a directory, while abstracting away iCloud concepts. It handles common save syncing scenarios like conflict resolution and offline play. Additionally, it provides a set of convenience UI alerts for these typical scenarios. GameSave also supports local saving for when the device isn’t signed into iCloud Drive.

> ❗ **Important**:  For GameSave to store the game data in the player’s iCloud account, you need to provide an identifier for the iCloud container that stores the data. Add the iCloud capability to your project and select the iCloud Documents checkbox. For more information, see [`Configuring iCloud services`](https://developer.apple.com/documentation/Xcode/configuring-icloud-services).

## Topics

### Synced directory
- [class GameSaveSyncedDirectory](gamesavesynceddirectory.md)
  A cloud-synced directory for game-save data.
### Error domain
- [let GameSaveErrorDomain: String](gamesaveerrordomain.md)
  The error domain name for GameSave errors.
### Synced directory (Objective-C)
- [class GSSyncedDirectory](gssynceddirectory.md)
  A cloud-synced directory for game-save data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/GameSave)*
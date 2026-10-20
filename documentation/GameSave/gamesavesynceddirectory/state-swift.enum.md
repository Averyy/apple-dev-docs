# GameSaveSyncedDirectory.State

**Framework**: GameSave  
**Kind**: enum  
**Role**: Enumeration

The state of the directory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum State
```

## Topics

### Directory states
- [GameSaveSyncedDirectory.State.closed](./state-swift.enum/closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSaveSyncedDirectory.Version])](./state-swift.enum/conflicted%28versions%29.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSaveSyncedDirectory.State.error(_:)](./state-swift.enum/error%28_%29.md)
  The directory is in error state and can’t be used.
- [GameSaveSyncedDirectory.State.local(_:)](./state-swift.enum/local%28_%29.md)
  The directory is local-only and not synced to iCloud.
- [GameSaveSyncedDirectory.State.offline(_:)](./state-swift.enum/offline%28_%29.md)
  The directory is available locally, but not fully synced because the device is offline.
- [GameSaveSyncedDirectory.State.ready(_:)](./state-swift.enum/ready%28_%29.md)
  The directory is fully synced and ready to use.
- [GameSaveSyncedDirectory.State.syncing](./state-swift.enum/syncing.md)
  The directory is currently syncing and is not ready yet.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)

## See Also

### Accessing a directory
- [class func openDirectory(containerIdentifier: String?) -> GameSaveSyncedDirectory](./opendirectory%28containeridentifier%29.md)
  Requests an instance of the game-save directory.
- [var state: GameSaveSyncedDirectory.State](./state-swift.property.md)
  The state that the game-save directory is in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum)*
# GameSaveSyncedDirectory.State

**Framework**: GameSave  
**Kind**: enum

The state of the directory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum State
```

## Topics

### Enumeration Cases
- [GameSaveSyncedDirectory.State.closed](gamesavesynceddirectory/state-swift.enum/closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSaveSyncedDirectory.Version])](gamesavesynceddirectory/state-swift.enum/conflicted(versions:).md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSaveSyncedDirectory.State.error(_:)](gamesavesynceddirectory/state-swift.enum/error(_:).md)
  The directory is in error state and can’t be used.
- [GameSaveSyncedDirectory.State.local(_:)](gamesavesynceddirectory/state-swift.enum/local(_:).md)
  The directory is local-only and not synced to iCloud.
- [GameSaveSyncedDirectory.State.offline(_:)](gamesavesynceddirectory/state-swift.enum/offline(_:).md)
  The directory is available locally, but not fully synced because the device is offline.
- [GameSaveSyncedDirectory.State.ready(_:)](gamesavesynceddirectory/state-swift.enum/ready(_:).md)
  The directory is fully synced and ready to use.
- [GameSaveSyncedDirectory.State.syncing](gamesavesynceddirectory/state-swift.enum/syncing.md)
  The directory is currently syncing and is not ready yet.
### Instance Properties
- [var description: String](gamesavesynceddirectory/state-swift.enum/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum)*
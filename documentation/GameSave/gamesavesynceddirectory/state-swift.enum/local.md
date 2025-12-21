# GameSaveSyncedDirectory.State.local(_:)

**Framework**: GameSave  
**Kind**: case

The directory is local-only and not synced to iCloud.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case local(URL)
```

## Parameters

- `URL`: The URL of a directory to read and write game-save data in.

## See Also

- [GameSaveSyncedDirectory.State.closed](gamesavesynceddirectory/state-swift.enum/closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSaveSyncedDirectory.Version])](gamesavesynceddirectory/state-swift.enum/conflicted(versions:).md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSaveSyncedDirectory.State.error(_:)](gamesavesynceddirectory/state-swift.enum/error(_:).md)
  The directory is in error state and can’t be used.
- [GameSaveSyncedDirectory.State.offline(_:)](gamesavesynceddirectory/state-swift.enum/offline(_:).md)
  The directory is available locally, but not fully synced because the device is offline.
- [GameSaveSyncedDirectory.State.ready(_:)](gamesavesynceddirectory/state-swift.enum/ready(_:).md)
  The directory is fully synced and ready to use.
- [GameSaveSyncedDirectory.State.syncing](gamesavesynceddirectory/state-swift.enum/syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum/local(_:))*
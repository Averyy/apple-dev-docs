# GameSaveSyncedDirectory.State.conflicted(versions:)

**Framework**: GameSave  
**Kind**: case

The directory has conflicts with the cloud, which the game needs to resolve.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case conflicted(versions: [GameSaveSyncedDirectory.Version])
```

## See Also

- [GameSaveSyncedDirectory.State.closed](gamesavesynceddirectory/state-swift.enum/closed.md)
  The directory is closed.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum/conflicted(versions:))*
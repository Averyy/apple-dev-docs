# GameSaveSyncedDirectory.State.offline(_:)

**Framework**: GameSave  
**Kind**: case  
**Role**: Case

The directory is available locally, but not fully synced because the device is offline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case offline(URL)
```

## Parameters

- `URL`: The URL of a directory to read and write game-save data in.

## See Also

### Directory states
- [GameSaveSyncedDirectory.State.closed](./closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSaveSyncedDirectory.Version])](./conflicted%28versions%29.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSaveSyncedDirectory.State.error(_:)](./error%28_%29.md)
  The directory is in error state and can’t be used.
- [GameSaveSyncedDirectory.State.local(_:)](./local%28_%29.md)
  The directory is local-only and not synced to iCloud.
- [GameSaveSyncedDirectory.State.ready(_:)](./ready%28_%29.md)
  The directory is fully synced and ready to use.
- [GameSaveSyncedDirectory.State.syncing](./syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum/offline(_:))*
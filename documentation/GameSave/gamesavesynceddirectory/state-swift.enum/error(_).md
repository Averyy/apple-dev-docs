# GameSaveSyncedDirectory.State.error(_:)

**Framework**: GameSave  
**Kind**: case  
**Role**: Case

The directory is in error state and can’t be used.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case error(any Error)
```

## See Also

### Directory states
- [GameSaveSyncedDirectory.State.closed](./closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSaveSyncedDirectory.Version])](./conflicted%28versions%29.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSaveSyncedDirectory.State.local(_:)](./local%28_%29.md)
  The directory is local-only and not synced to iCloud.
- [GameSaveSyncedDirectory.State.offline(_:)](./offline%28_%29.md)
  The directory is available locally, but not fully synced because the device is offline.
- [GameSaveSyncedDirectory.State.ready(_:)](./ready%28_%29.md)
  The directory is fully synced and ready to use.
- [GameSaveSyncedDirectory.State.syncing](./syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/state-swift.enum/error(_:))*
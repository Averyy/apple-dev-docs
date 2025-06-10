# GameSyncedDirectory.State

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

### Directory states
- [GameSyncedDirectory.State.closed](gamesynceddirectory/state-swift.enum/closed.md)
  The directory is closed.
- [case conflicted(versions: [GameSyncedDirectory.Version])](gamesynceddirectory/state-swift.enum/conflicted(versions:).md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GameSyncedDirectory.State.error(_:)](gamesynceddirectory/state-swift.enum/error(_:).md)
  The directory is in error state and can’t be used.
- [GameSyncedDirectory.State.local(_:)](gamesynceddirectory/state-swift.enum/local(_:).md)
  The directory is local-only and not synced to iCloud.
- [GameSyncedDirectory.State.offline(_:)](gamesynceddirectory/state-swift.enum/offline(_:).md)
  The directory is available locally, but not fully synced because the device is offline.
- [GameSyncedDirectory.State.ready(_:)](gamesynceddirectory/state-swift.enum/ready(_:).md)
  The directory is fully synced and ready to use.
- [GameSyncedDirectory.State.syncing](gamesynceddirectory/state-swift.enum/syncing.md)
  The directory is currently syncing and is not ready yet.
### Describing states
- [var description: String](gamesynceddirectory/state-swift.enum/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [class func openDirectory(containerIdentifier: String?) -> GameSyncedDirectory](gamesynceddirectory/opendirectory(containeridentifier:).md)
  Requests an instance of the game-save directory.
- [var state: GameSyncedDirectory.State](gamesynceddirectory/state-swift.property.md)
  The state that the game-save directory is in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/state-swift.enum)*
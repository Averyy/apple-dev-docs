# GSSyncState

**Framework**: GameSave  
**Kind**: enum

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum GSSyncState
```

## Topics

### Directory states
- [GSSyncState.closed](gssyncstate/closed.md)
  The directory is closed.
- [GSSyncState.conflicted](gssyncstate/conflicted.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GSSyncState.error](gssyncstate/error.md)
  The directory is in error state and can’t be used.
- [GSSyncState.local](gssyncstate/local.md)
  The directory is local-only and not synced to iCloud.
- [GSSyncState.offline](gssyncstate/offline.md)
  The directory is available locally, but not fully synced because the device is offline.
- [GSSyncState.ready](gssyncstate/ready.md)
  The directory is fully synced and ready to use.
- [GSSyncState.syncing](gssyncstate/syncing.md)
  The directory is currently syncing and is not ready yet.
### Creating a directory state
- [init?(rawValue: Int)](gssyncstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: GSSyncState](gssynceddirectorystate/state.md)
  Specifies the current state of the directory
- [var conflictedVersions: [GSSyncedDirectoryVersion]?](gssynceddirectorystate/conflictedversions.md)
  The conflicting versions.
- [var error: (any Error)?](gssynceddirectorystate/error.md)
  The error preventing you from using the directory.
- [var url: URL?](gssynceddirectorystate/url.md)
  The URL of a directory to read and write game-save data in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssyncstate)*
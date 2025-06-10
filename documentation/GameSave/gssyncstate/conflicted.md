# GSSyncState.conflicted

**Framework**: GameSave  
**Kind**: case

The directory has conflicts with the cloud, which the game needs to resolve.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case conflicted
```

#### Discussion

In this state, the value of [`conflictedVersions`](gssynceddirectorystate/conflictedversions.md) is nonnull.

## See Also

- [GSSyncState.closed](gssyncstate/closed.md)
  The directory is closed.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssyncstate/conflicted)*
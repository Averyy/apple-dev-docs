# GSSyncState.offline

**Framework**: GameSave  
**Kind**: case

The directory is available locally, but not fully synced because the device is offline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case offline
```

#### Discussion

In this state, the value of [`url`](gssynceddirectorystate/url.md) is nonnull.

## See Also

- [GSSyncState.closed](gssyncstate/closed.md)
  The directory is closed.
- [GSSyncState.conflicted](gssyncstate/conflicted.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GSSyncState.error](gssyncstate/error.md)
  The directory is in error state and can’t be used.
- [GSSyncState.local](gssyncstate/local.md)
  The directory is local-only and not synced to iCloud.
- [GSSyncState.ready](gssyncstate/ready.md)
  The directory is fully synced and ready to use.
- [GSSyncState.syncing](gssyncstate/syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssyncstate/offline)*
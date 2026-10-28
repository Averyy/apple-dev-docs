# GSSyncState.ready

**Framework**: GameSave  
**Kind**: case  
**Role**: Case

The directory is fully synced and ready to use.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case ready
```

```c
GSSyncStateReady
```

## Discussion

In this state, the value of [`url`](../gssynceddirectorystate/url.md) is nonnull.

## See Also

### Directory states
- [GSSyncState.closed](./closed.md)
  The directory is closed.
- [GSSyncState.conflicted](./conflicted.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GSSyncState.error](./error.md)
  The directory is in error state and can’t be used.
- [GSSyncState.local](./local.md)
  The directory is local-only and not synced to iCloud.
- [GSSyncState.offline](./offline.md)
  The directory is available locally, but not fully synced because the device is offline.
- [GSSyncState.syncing](./syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssyncstate/ready)*
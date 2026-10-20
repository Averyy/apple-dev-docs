# GSSyncState.closed

**Framework**: GameSave  
**Kind**: case  
**Role**: Case

The directory is closed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case closed
```

```c
GSSyncStateClosed
```

## See Also

### Directory states
- [GSSyncState.conflicted](./conflicted.md)
  The directory has conflicts with the cloud, which the game needs to resolve.
- [GSSyncState.error](./error.md)
  The directory is in error state and can’t be used.
- [GSSyncState.local](./local.md)
  The directory is local-only and not synced to iCloud.
- [GSSyncState.offline](./offline.md)
  The directory is available locally, but not fully synced because the device is offline.
- [GSSyncState.ready](./ready.md)
  The directory is fully synced and ready to use.
- [GSSyncState.syncing](./syncing.md)
  The directory is currently syncing and is not ready yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssyncstate/closed)*
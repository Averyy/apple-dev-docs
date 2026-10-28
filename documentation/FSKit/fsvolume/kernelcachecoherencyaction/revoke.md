# FSVolume.KernelCacheCoherencyAction.revoke

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case revoke
```

```c
FSKernelCacheCoherencyActionRevoke
```

## Discussion

Use this action when the module determines that an item no longer exists or is no longer accessible. Common scenarios include:

- Another client deleted the item, as detected via server notification.
- The module received a server callback indicating the file’s absence.

## See Also

### Coherency actions
- [FSVolume.KernelCacheCoherencyAction.push](./push.md)
  An action to flush dirty data from cache to storage, preserving cache contents.
- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](./pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.invalidate](./invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.update](./update.md)
  An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction/revoke)*
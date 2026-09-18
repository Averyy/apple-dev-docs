# FSVolume.KernelCacheCoherencyAction.push

**Framework**: FSKit  
**Kind**: case

An action to flush dirty data from cache to storage, preserving cache contents.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case push
```

## See Also

- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](fsvolume/kernelcachecoherencyaction/pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.invalidate](fsvolume/kernelcachecoherencyaction/invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.update](fsvolume/kernelcachecoherencyaction/update.md)
  An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.
- [FSVolume.KernelCacheCoherencyAction.revoke](fsvolume/kernelcachecoherencyaction/revoke.md)
  An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction/push)*
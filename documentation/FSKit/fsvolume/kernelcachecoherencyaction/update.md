# FSVolume.KernelCacheCoherencyAction.update

**Framework**: FSKit  
**Kind**: case

An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case update
```

## See Also

- [FSVolume.KernelCacheCoherencyAction.push](fsvolume/kernelcachecoherencyaction/push.md)
  An action to flush dirty data from cache to storage, preserving cache contents.
- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](fsvolume/kernelcachecoherencyaction/pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache.
- [FSVolume.KernelCacheCoherencyAction.invalidate](fsvolume/kernelcachecoherencyaction/invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage.
- [FSVolume.KernelCacheCoherencyAction.revoke](fsvolume/kernelcachecoherencyaction/revoke.md)
  An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction/update)*
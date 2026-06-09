# FSVolume.KernelCacheCoherencyAction.revoke

**Framework**: FSKit  
**Kind**: case

An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case revoke
```

#### Discussion

Use this action when the module determines that an item no longer exists or is no longer accessible. Common scenarios include:

- Another client deleted the item, as detected via server notification.
- The module received a server callback indicating the file’s absence.

## See Also

- [FSVolume.KernelCacheCoherencyAction.push](fsvolume/kernelcachecoherencyaction/push.md)
  An action to flush dirty data from cache to storage, preserving cache contents.
- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](fsvolume/kernelcachecoherencyaction/pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache.
- [FSVolume.KernelCacheCoherencyAction.invalidate](fsvolume/kernelcachecoherencyaction/invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage.
- [FSVolume.KernelCacheCoherencyAction.update](fsvolume/kernelcachecoherencyaction/update.md)
  An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction/revoke)*
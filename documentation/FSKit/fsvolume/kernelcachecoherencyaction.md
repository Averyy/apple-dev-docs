# FSVolume.KernelCacheCoherencyAction

**Framework**: FSKit  
**Kind**: enum

A type that defines actions for cache state changes.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum KernelCacheCoherencyAction
```

## Topics

### Coherency actions
- [FSVolume.KernelCacheCoherencyAction.push](fsvolume/kernelcachecoherencyaction/push.md)
  An action to flush dirty data from cache to storage, preserving cache contents.
- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](fsvolume/kernelcachecoherencyaction/pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache.
- [FSVolume.KernelCacheCoherencyAction.invalidate](fsvolume/kernelcachecoherencyaction/invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage.
- [FSVolume.KernelCacheCoherencyAction.update](fsvolume/kernelcachecoherencyaction/update.md)
  An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.
- [FSVolume.KernelCacheCoherencyAction.revoke](fsvolume/kernelcachecoherencyaction/revoke.md)
  An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.
### Initializers - generated
- [init?(rawValue: Int)](fsvolume/kernelcachecoherencyaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setCacheState(for: FSItem, cacheMode: FSVolume.DataCacheMode, coherencyType: FSVolume.KernelCacheCoherencyType, action: FSVolume.KernelCacheCoherencyAction) -> (any Error)?](fsvolume/setcachestate(for:cachemode:coherencytype:action:).md)
  Sends a synchronous cache state update request from the module to the kernel.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction)*
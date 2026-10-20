# FSVolume.KernelCacheCoherencyAction

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

A type that defines actions for cache state changes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum KernelCacheCoherencyAction
```

```c
enum FSKernelCacheCoherencyAction : NSInteger;
```

## Topics

### Coherency actions
- [FSVolume.KernelCacheCoherencyAction.push](./kernelcachecoherencyaction/push.md)
  An action to flush dirty data from cache to storage, preserving cache contents.
- [FSVolume.KernelCacheCoherencyAction.pushInvalidate](./kernelcachecoherencyaction/pushinvalidate.md)
  An action to flush dirty data to storage and invalidate (clear) the cache. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.invalidate](./kernelcachecoherencyaction/invalidate.md)
  An action to invalidate (clear) the cache, discarding any dirty data without writing to storage. This also invalidates the item’s cached attributes, so the next request for attributes fetches them from your module.
- [FSVolume.KernelCacheCoherencyAction.update](./kernelcachecoherencyaction/update.md)
  An action to update the coherency mode while keeping the cache valid, requiring no push or invalidation.
- [FSVolume.KernelCacheCoherencyAction.revoke](./kernelcachecoherencyaction/revoke.md)
  An action to invalidate all caches, revoke all access to the item, and trigger vnode reclamation.
### Initializers
- [init?(rawValue: Int)](./kernelcachecoherencyaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing caching behavior
- [func setCacheState(for: FSItem, cacheMode: FSVolume.DataCacheMode, coherencyType: FSVolume.KernelCacheCoherencyType, action: FSVolume.KernelCacheCoherencyAction) -> (any Error)?](./setcachestate%28for,cachemode,coherencytype,action%29.md)
  Sends a synchronous cache state update request from the module to the kernel.
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.DataCacheMode](./datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [FSVolume.KernelCacheCoherencyType](./kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencyaction)*
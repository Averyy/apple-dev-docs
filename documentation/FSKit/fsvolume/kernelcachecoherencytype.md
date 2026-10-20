# FSVolume.KernelCacheCoherencyType

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

A type that defines how the kernel caches data.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum KernelCacheCoherencyType
```

```c
enum FSKernelCacheCoherencyType : NSInteger;
```

## Topics

### Coherency types
- [FSVolume.KernelCacheCoherencyType.noCache](./kernelcachecoherencytype/nocache.md)
  A type that indicates all I/O goes directly to storage, without caching.
- [FSVolume.KernelCacheCoherencyType.readCache](./kernelcachecoherencytype/readcache.md)
  A type that indicates that writes bypass the cache and go directly to storage.
- [FSVolume.KernelCacheCoherencyType.writeBack](./kernelcachecoherencytype/writeback.md)
  A type that indicates writes immediately update the cache only, followed by a deferred write to storage.
- [FSVolume.KernelCacheCoherencyType.writeThrough](./kernelcachecoherencytype/writethrough.md)
  A type that indicates writes update cache and storage synchronously.
### Initializers
- [init?(rawValue: Int)](./kernelcachecoherencytype/init%28rawvalue%29.md)

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
- [FSVolume.KernelCacheCoherencyAction](./kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencytype)*
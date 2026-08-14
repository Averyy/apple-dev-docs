# FSVolume.KernelCacheCoherencyType

**Framework**: FSKit  
**Kind**: enum

A type that defines how the kernel caches data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum KernelCacheCoherencyType
```

## Topics

### Coherency types
- [FSVolume.KernelCacheCoherencyType.noCache](fsvolume/kernelcachecoherencytype/nocache.md)
  A type that indicates all I/O goes directly to storage, without caching.
- [FSVolume.KernelCacheCoherencyType.readCache](fsvolume/kernelcachecoherencytype/readcache.md)
  A type that indicates that writes bypass the cache and go directly to storage.
- [FSVolume.KernelCacheCoherencyType.writeBack](fsvolume/kernelcachecoherencytype/writeback.md)
  A type that indicates writes immediately update the cache only, followed by a deferred write to storage.
- [FSVolume.KernelCacheCoherencyType.writeThrough](fsvolume/kernelcachecoherencytype/writethrough.md)
  A type that indicates writes update cache and storage synchronously.
### Initializers
- [init?(rawValue: Int)](fsvolume/kernelcachecoherencytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func setCacheState(for: FSItem, cacheMode: FSVolume.DataCacheMode, coherencyType: FSVolume.KernelCacheCoherencyType, action: FSVolume.KernelCacheCoherencyAction) -> (any Error)?](fsvolume/setcachestate(for:cachemode:coherencytype:action:).md)
  Sends a synchronous cache state update request from the module to the kernel.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [FSVolume.KernelCacheCoherencyAction](fsvolume/kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencytype)*
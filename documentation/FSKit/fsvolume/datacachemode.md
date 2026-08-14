# FSVolume.DataCacheMode

**Framework**: FSKit  
**Kind**: enum

A type that defines the cache mode requested by the kernel for data operations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum DataCacheMode
```

## Topics

### Data cache modes
- [FSVolume.DataCacheMode.none](fsvolume/datacachemode/none.md)
  A mode that indicates no active caching.
- [FSVolume.DataCacheMode.readWithCache](fsvolume/datacachemode/readwithcache.md)
  A mode that indicates read access with caching enabled.
- [FSVolume.DataCacheMode.readWriteWithCache](fsvolume/datacachemode/readwritewithcache.md)
  A mode that indicates read-write access with caching enabled.
### Initializers
- [init?(rawValue: Int)](fsvolume/datacachemode/init(rawvalue:).md)

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
- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.
- [FSVolume.KernelCacheCoherencyAction](fsvolume/kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachemode)*
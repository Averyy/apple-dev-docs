# FSVolume.DataCacheMode

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

A type that defines the cache mode requested by the kernel for data operations.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum DataCacheMode
```

```c
enum FSDataCacheMode : NSInteger;
```

## Topics

### Data cache modes
- [FSVolume.DataCacheMode.none](./datacachemode/none.md)
  A mode that indicates no active caching.
- [FSVolume.DataCacheMode.readWithCache](./datacachemode/readwithcache.md)
  A mode that indicates read access with caching enabled.
- [FSVolume.DataCacheMode.readWriteWithCache](./datacachemode/readwritewithcache.md)
  A mode that indicates read-write access with caching enabled.
### Initializers
- [init?(rawValue: Int)](./datacachemode/init%28rawvalue%29.md)

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
- [FSVolume.KernelCacheCoherencyType](./kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.
- [FSVolume.KernelCacheCoherencyAction](./kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachemode)*
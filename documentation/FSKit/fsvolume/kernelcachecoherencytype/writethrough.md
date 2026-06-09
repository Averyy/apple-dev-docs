# FSVolume.KernelCacheCoherencyType.writeThrough

**Framework**: FSKit  
**Kind**: case

A type that indicates writes update cache and storage synchronously.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case writeThrough
```

## See Also

- [FSVolume.KernelCacheCoherencyType.noCache](fsvolume/kernelcachecoherencytype/nocache.md)
  A type that indicates all I/O goes directly to storage, without caching.
- [FSVolume.KernelCacheCoherencyType.readCache](fsvolume/kernelcachecoherencytype/readcache.md)
  A type that indicates that writes bypass the cache and go directly to storage.
- [FSVolume.KernelCacheCoherencyType.writeBack](fsvolume/kernelcachecoherencytype/writeback.md)
  A type that indicates writes immediately update the cache only, followed by a deferred write to storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencytype/writethrough)*
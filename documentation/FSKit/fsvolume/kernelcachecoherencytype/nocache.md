# FSVolume.KernelCacheCoherencyType.noCache

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

A type that indicates all I/O goes directly to storage, without caching.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case noCache
```

```c
FSKernelCacheCoherencyTypeNoCache
```

## See Also

### Coherency types
- [FSVolume.KernelCacheCoherencyType.readCache](./readcache.md)
  A type that indicates that writes bypass the cache and go directly to storage.
- [FSVolume.KernelCacheCoherencyType.writeBack](./writeback.md)
  A type that indicates writes immediately update the cache only, followed by a deferred write to storage.
- [FSVolume.KernelCacheCoherencyType.writeThrough](./writethrough.md)
  A type that indicates writes update cache and storage synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/kernelcachecoherencytype/nocache)*
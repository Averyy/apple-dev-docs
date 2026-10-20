# URLCache.StoragePolicy.allowedInMemoryOnly

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Storage in [`URLCache`](../../urlcache.md) is allowed; however storage should be restricted to memory only.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case allowedInMemoryOnly
```

```c
NSURLCacheStorageAllowedInMemoryOnly
```

## See Also

### Policies
- [URLCache.StoragePolicy.allowed](./allowed.md)
  Storage in [`URLCache`](../../urlcache.md) is allowed without restriction.
- [URLCache.StoragePolicy.notAllowed](./notallowed.md)
  Storage in [`URLCache`](../../urlcache.md) is not allowed in any fashion, either in memory or on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy/allowedinmemoryonly)*
# URLCache.StoragePolicy.allowed

**Framework**: Foundation  
**Kind**: case

Storage in [`URLCache`](urlcache.md) is allowed without restriction.

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
case allowed
```

#### Discussion

> ❗ **Important**:  iOS prior to version 5 ignores this cache policy, and instead treats it as [`URLCache.StoragePolicy.allowedInMemoryOnly`](urlcache/storagepolicy/allowedinmemoryonly.md).

## See Also

- [URLCache.StoragePolicy.allowedInMemoryOnly](urlcache/storagepolicy/allowedinmemoryonly.md)
  Storage in [`URLCache`](urlcache.md) is allowed; however storage should be restricted to memory only.
- [URLCache.StoragePolicy.notAllowed](urlcache/storagepolicy/notallowed.md)
  Storage in [`URLCache`](urlcache.md) is not allowed in any fashion, either in memory or on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy/allowed)*
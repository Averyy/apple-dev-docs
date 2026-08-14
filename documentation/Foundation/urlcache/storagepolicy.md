# URLCache.StoragePolicy

**Framework**: Foundation  
**Kind**: enum

These constants specify the caching strategy used by an [`CachedURLResponse`](cachedurlresponse.md) object.

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
enum StoragePolicy
```

## Topics

### Policies
- [URLCache.StoragePolicy.allowed](urlcache/storagepolicy/allowed.md)
  Storage in [`URLCache`](urlcache.md) is allowed without restriction.
- [URLCache.StoragePolicy.allowedInMemoryOnly](urlcache/storagepolicy/allowedinmemoryonly.md)
  Storage in [`URLCache`](urlcache.md) is allowed; however storage should be restricted to memory only.
- [URLCache.StoragePolicy.notAllowed](urlcache/storagepolicy/notallowed.md)
  Storage in [`URLCache`](urlcache.md) is not allowed in any fashion, either in memory or on disk.
### Initializers
- [init?(rawValue: UInt)](urlcache/storagepolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy)*
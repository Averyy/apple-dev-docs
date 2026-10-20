# URLCache.StoragePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants specify the caching strategy used by an [`CachedURLResponse`](../cachedurlresponse.md) object.

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

```c
enum NSURLCacheStoragePolicy : NSUInteger;
```

## Topics

### Policies
- [URLCache.StoragePolicy.allowed](./storagepolicy/allowed.md)
  Storage in [`URLCache`](../urlcache.md) is allowed without restriction.
- [URLCache.StoragePolicy.allowedInMemoryOnly](./storagepolicy/allowedinmemoryonly.md)
  Storage in [`URLCache`](../urlcache.md) is allowed; however storage should be restricted to memory only.
- [URLCache.StoragePolicy.notAllowed](./storagepolicy/notallowed.md)
  Storage in [`URLCache`](../urlcache.md) is not allowed in any fashion, either in memory or on disk.
### Initializers
- [init?(rawValue: UInt)](./storagepolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy)*
# NSURLRequest.CachePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The constants used to specify interaction with the cached responses.

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
enum CachePolicy
```

```c
enum NSURLRequestCachePolicy : NSUInteger;
```

## Mentions

- [Accessing cached data](../accessing-cached-data.md)

#### Overview

The default policy is [`NSURLRequest.CachePolicy.useProtocolCachePolicy`](./cachepolicy-swift.enum/useprotocolcachepolicy.md).

## Topics

### Policies
- [NSURLRequest.CachePolicy.useProtocolCachePolicy](./cachepolicy-swift.enum/useprotocolcachepolicy.md)
  Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData](./cachepolicy-swift.enum/reloadignoringlocalcachedata.md)
  The URL load should be loaded only from the originating source.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData](./cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md)
  Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.
- [static var reloadIgnoringCacheData: NSURLRequest.CachePolicy](./cachepolicy-swift.enum/reloadignoringcachedata.md)
  Replaced by [`NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData`](./cachepolicy-swift.enum/reloadignoringlocalcachedata.md).
- [NSURLRequest.CachePolicy.returnCacheDataElseLoad](./cachepolicy-swift.enum/returncachedataelseload.md)
  Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequest.CachePolicy.returnCacheDataDontLoad](./cachepolicy-swift.enum/returncachedatadontload.md)
  Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.
- [NSURLRequest.CachePolicy.reloadRevalidatingCacheData](./cachepolicy-swift.enum/reloadrevalidatingcachedata.md)
  Use cache data if the origin source can validate it; otherwise, load from the origin.
### Initializers
- [init?(rawValue: UInt)](./cachepolicy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with a cache policy
- [var cachePolicy: NSURLRequest.CachePolicy](../nsmutableurlrequest/cachepolicy.md)
  The request’s cache policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum)*
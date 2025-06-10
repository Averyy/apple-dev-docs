# NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData

**Framework**: Foundation  
**Kind**: case

The URL load should be loaded only from the originating source.

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
case reloadIgnoringLocalCacheData
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

This policy specifies that no existing cache data should be used to satisfy a URL load request.

> ❗ **Important**:  Always use this policy if you are making HTTP or HTTPS byte-range requests.

## See Also

- [NSURLRequest.CachePolicy.useProtocolCachePolicy](nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md)
  Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData](nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md)
  Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.
- [static var reloadIgnoringCacheData: NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum/reloadignoringcachedata.md)
  Replaced by [`NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData`](nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalcachedata.md).
- [NSURLRequest.CachePolicy.returnCacheDataElseLoad](nsurlrequest/cachepolicy-swift.enum/returncachedataelseload.md)
  Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequest.CachePolicy.returnCacheDataDontLoad](nsurlrequest/cachepolicy-swift.enum/returncachedatadontload.md)
  Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.
- [NSURLRequest.CachePolicy.reloadRevalidatingCacheData](nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata.md)
  Use cache data if the origin source can validate it; otherwise, load from the origin.
- [NSURLRequest.CachePolicy.useProtocolCachePolicy](nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md)
  Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData](nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md)
  Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.
- [static var reloadIgnoringCacheData: NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum/reloadignoringcachedata.md)
  Replaced by [`NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData`](nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalcachedata.md).
- [NSURLRequest.CachePolicy.returnCacheDataElseLoad](nsurlrequest/cachepolicy-swift.enum/returncachedataelseload.md)
  Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequest.CachePolicy.returnCacheDataDontLoad](nsurlrequest/cachepolicy-swift.enum/returncachedatadontload.md)
  Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.
- [NSURLRequest.CachePolicy.reloadRevalidatingCacheData](nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata.md)
  Use cache data if the origin source can validate it; otherwise, load from the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalcachedata)*
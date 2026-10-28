# NSURLRequest.CachePolicy.reloadRevalidatingCacheData

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Use cache data if the origin source can validate it; otherwise, load from the origin.

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
case reloadRevalidatingCacheData
```

```c
NSURLRequestReloadRevalidatingCacheData
```

## Discussion

> ❗ **Important**:  Versions earlier than macOS 10.15, iOS 13, watchOS 6, and tvOS 13 don’t implement this constant.

## See Also

### Policies
- [NSURLRequest.CachePolicy.useProtocolCachePolicy](./useprotocolcachepolicy.md)
  Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData](./reloadignoringlocalcachedata.md)
  The URL load should be loaded only from the originating source.
- [NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData](./reloadignoringlocalandremotecachedata.md)
  Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.
- [static var reloadIgnoringCacheData: NSURLRequest.CachePolicy](./reloadignoringcachedata.md)
  Replaced by [`NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData`](./reloadignoringlocalcachedata.md).
- [NSURLRequest.CachePolicy.returnCacheDataElseLoad](./returncachedataelseload.md)
  Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequest.CachePolicy.returnCacheDataDontLoad](./returncachedatadontload.md)
  Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum/reloadrevalidatingcachedata)*
# NSURLRequest.CachePolicy.useProtocolCachePolicy

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.

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
case useProtocolCachePolicy
```

```c
NSURLRequestUseProtocolCachePolicy
```

## Mentions

- [Accessing cached data](../../accessing-cached-data.md)

#### Discussion

This is the default policy for URL load requests.

##### HTTP caching behavior

For the HTTP and HTTPS protocols, [`NSURLRequest.CachePolicy.useProtocolCachePolicy`](./useprotocolcachepolicy.md) performs the following behavior:

1. If a cached response does not exist for the request, the URL loading system fetches the data from the originating source.
2. Otherwise, if the cached response does not indicate that it must be revalidated every time, and if the cached response is not stale (past its expiration date), the URL loading system returns the cached response.
3. If the cached response is stale or requires revalidation, the URL loading system makes a HEAD request to the originating source to see if the resource has changed. If so, the URL loading system fetches the data from the originating source. Otherwise, it returns the cached response.

This behavior is illustrated in the figure below.

![Flow chart starting with “need to determine whether to return a cached response”, and then considering various factors to determine whether to return a cached response or to fetch it anew.](https://developer.apple.com/tutorials/images/com.apple.foundation/media-2994170@2x.png)

> **Note**:  For the formal definition of these semantics, see [RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13).

> ❗ **Important**:  If you are making HTTP or HTTPS byte-range requests, always use the [`NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData`](./reloadignoringlocalcachedata.md) policy instead.

## See Also

### Policies
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
- [NSURLRequest.CachePolicy.reloadRevalidatingCacheData](./reloadrevalidatingcachedata.md)
  Use cache data if the origin source can validate it; otherwise, load from the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy)*
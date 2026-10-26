# initWithURL:cached:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a newly created URL handle with the specified URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (id) initWithURL:(NSURL *) anURL cached:(BOOL) willCache;
```

#### Discussion

Subclasses of `NSURLHandle` must override this method.

## Parameters

- `anURL`: The URL for the new handle.
- `willCache`: [`true`](../../Swift/true.md) if the URL handle should cache its data and respond to requests from equivalent URLs for the cached data, [`false`](../../Swift/false.md) otherwise.

## See Also

### Constructing NSURLHandles
- [+ cachedHandleForURL:](./cachedhandleforurl_.md)
  Returns the URL handle from the cache that has serviced the specified URL or another identical URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/initwithurl:cached:)*
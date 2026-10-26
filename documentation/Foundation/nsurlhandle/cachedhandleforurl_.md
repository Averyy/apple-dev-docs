# cachedHandleForURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the URL handle from the cache that has serviced the specified URL or another identical URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
+ (NSURLHandle *) cachedHandleForURL:(NSURL *) anURL;
```

#### Return Value

The URL handle from the cache that has serviced `aURL` or another identical URL. Returns `nil` if there is no such handle.

#### Discussion

Subclasses of `NSURLHandle` must override this method.

## Parameters

- `anURL`: The URL whose cached URL handle is desired.

## See Also

### Constructing NSURLHandles
- [- initWithURL:cached:](./initwithurl_cached_.md)
  Initializes a newly created URL handle with the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/cachedhandleforurl:)*
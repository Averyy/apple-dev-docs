# canInitWithURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns whether a URL handle can be initialized with a given URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
+ (BOOL) canInitWithURL:(NSURL *) anURL;
```

## Return Value

[`true`](../../Swift/true.md) if a URL handle can be initialized with `aURL`, [`false`](../../Swift/false.md) otherwise.

## Discussion

Subclasses of `NSURLHandle` must override this method to identify which URLs they can service.

## Parameters

- `anURL`: The URL in question.

## See Also

### Managing subclasses
- [+ URLHandleClassForURL:](./urlhandleclassforurl_.md)
  Returns the class of the URL handle that will be used for a specified URL.
- [+ registerURLHandleClass:](./registerurlhandleclass_.md)
  Registers a subclass of `NSURLHandle` as an available subclass for handling URLs


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/caninitwithurl:)*
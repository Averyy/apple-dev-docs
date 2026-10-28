# URLHandleClassForURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the class of the URL handle that will be used for a specified URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
+ (Class) URLHandleClassForURL:(NSURL *) anURL;
```

## Return Value

The class of the URL handle that will be used for `aURL`.

## Discussion

Subclasses of `NSURLHandle` must be registered via the [`registerURLHandleClass:`](./registerurlhandleclass_.md) method. The subclass is determined by asking the list of registered subclasses if it [`canInitWithURL:`](./caninitwithurl_.md); the first class to respond [`true`](../../Swift/true.md) is selected.

## Parameters

- `anURL`: The URL in question.

## See Also

### Managing subclasses
- [+ canInitWithURL:](./caninitwithurl_.md)
  Returns whether a URL handle can be initialized with a given URL.
- [+ registerURLHandleClass:](./registerurlhandleclass_.md)
  Registers a subclass of `NSURLHandle` as an available subclass for handling URLs


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/urlhandleclassforurl:)*
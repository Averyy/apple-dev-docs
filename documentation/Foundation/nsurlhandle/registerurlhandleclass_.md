# registerURLHandleClass:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Registers a subclass of `NSURLHandle` as an available subclass for handling URLs

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
+ (void) registerURLHandleClass:(Class) anURLHandleSubclass;
```

## Parameters

- `anURLHandleSubclass`: The new subclass to register as an available subclass.

## See Also

### Managing subclasses
- [+ URLHandleClassForURL:](./urlhandleclassforurl_.md)
  Returns the class of the URL handle that will be used for a specified URL.
- [+ canInitWithURL:](./caninitwithurl_.md)
  Returns whether a URL handle can be initialized with a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/registerurlhandleclass:)*
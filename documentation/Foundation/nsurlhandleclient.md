# NSURLHandleClient

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

The interface implemented by URL handle clients.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
@protocol NSURLHandleClient
```

#### Overview

[`NSURLHandleClient`](./nsurlhandleclient.md) is deprecated in macOS 10.4 and later. Applications that are intended for deployment in macOS 10.3 or later should use [`NSURLConnection`](./nsurlconnection.md) or [`NSURLDownload`](./nsurldownload.md) instead; see [URL Loading System](./url-loading-system.md).

## Topics

### Notification methods
- [- URLHandleResourceDidBeginLoading:](./nsurlhandleclient/urlhandleresourcedidbeginloading_.md)
  Sent when an URL handle begins loading resource data.
- [- URLHandleResourceDidCancelLoading:](./nsurlhandleclient/urlhandleresourcedidcancelloading_.md)
  Sent when an URL handle has canceled loading resource data in response to a programmatic request.
- [- URLHandleResourceDidFinishLoading:](./nsurlhandleclient/urlhandleresourcedidfinishloading_.md)
  Sent when an URL handle finishes loading resource data.
- [- URLHandle:resourceDataDidBecomeAvailable:](./nsurlhandleclient/urlhandle_resourcedatadidbecomeavailable_.md)
  Sent periodically by an URL handle when new resource data becomes available.
- [- URLHandle:resourceDidFailLoadingWithReason:](./nsurlhandleclient/urlhandle_resourcedidfailloadingwithreason_.md)
  Sent when the URL handle failed to load resource data for some reason other than being canceled.

## See Also

### URL Handle
- [class NSURLHandle](./nsurlhandle.md)
  An object that accesses and manages resource data indicated by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandleclient)*
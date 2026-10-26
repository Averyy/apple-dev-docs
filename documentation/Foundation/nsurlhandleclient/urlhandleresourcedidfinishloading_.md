# URLHandleResourceDidFinishLoading:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when an URL handle finishes loading resource data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (void) URLHandleResourceDidFinishLoading:(NSURLHandle *) sender;
```

## Parameters

- `sender`: The URL handle sending the message.

## See Also

### Notification methods
- [- URLHandleResourceDidBeginLoading:](./urlhandleresourcedidbeginloading_.md)
  Sent when an URL handle begins loading resource data.
- [- URLHandleResourceDidCancelLoading:](./urlhandleresourcedidcancelloading_.md)
  Sent when an URL handle has canceled loading resource data in response to a programmatic request.
- [- URLHandle:resourceDataDidBecomeAvailable:](./urlhandle_resourcedatadidbecomeavailable_.md)
  Sent periodically by an URL handle when new resource data becomes available.
- [- URLHandle:resourceDidFailLoadingWithReason:](./urlhandle_resourcedidfailloadingwithreason_.md)
  Sent when the URL handle failed to load resource data for some reason other than being canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandleclient/urlhandleresourcedidfinishloading:)*
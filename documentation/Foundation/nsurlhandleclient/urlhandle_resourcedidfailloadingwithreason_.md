# URLHandle:resourceDidFailLoadingWithReason:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when the URL handle failed to load resource data for some reason other than being canceled.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (void) URLHandle:(NSURLHandle *) sender resourceDidFailLoadingWithReason:(NSString *) reason;
```

## Parameters

- `sender`: The URL handle sending the message.
- `reason`: A human-readable, localized string describing why the load failed.

## See Also

### Notification methods
- [- URLHandleResourceDidBeginLoading:](./urlhandleresourcedidbeginloading_.md)
  Sent when an URL handle begins loading resource data.
- [- URLHandleResourceDidCancelLoading:](./urlhandleresourcedidcancelloading_.md)
  Sent when an URL handle has canceled loading resource data in response to a programmatic request.
- [- URLHandleResourceDidFinishLoading:](./urlhandleresourcedidfinishloading_.md)
  Sent when an URL handle finishes loading resource data.
- [- URLHandle:resourceDataDidBecomeAvailable:](./urlhandle_resourcedatadidbecomeavailable_.md)
  Sent periodically by an URL handle when new resource data becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandleclient/urlhandle:resourcedidfailloadingwithreason:)*
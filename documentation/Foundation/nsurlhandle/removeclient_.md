# removeClient:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes `client` as an `NSURLHandleClient` of the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (void) removeClient:(id<NSURLHandleClient>) client;
```

## Parameters

- `client`: An object conforming to the `NSURLHandleClient` protocol.

## See Also

### Managing clients
- [- addClient:](./addclient_.md)
  Adds a client of the URL handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/removeclient:)*
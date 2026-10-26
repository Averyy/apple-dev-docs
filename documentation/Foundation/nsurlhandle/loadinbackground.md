# loadInBackground

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Loads the receiver’s data in the background.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (void) loadInBackground;
```

#### Discussion

Each subclass determines its own loading policy. Clients should not assume that multiple background loads can proceed simultaneously. For example, a subclass may maintain only one thread for background loading, so only one background loading operation can be in progress at a time. If multiple background loads are requested, the later requests will wait in a queue until earlier requests are handled.

## See Also

### Loading resource data
- [- availableResourceData](./availableresourcedata.md)
  Immediately returns the currently available resource data managed by the URL handle.
- [- backgroundLoadDidFailWithReason:](./backgroundloaddidfailwithreason_.md)
  Called when a background load fails.
- [- beginLoadInBackground](./beginloadinbackground.md)
  Called when a background load begins.
- [- cancelLoadInBackground](./cancelloadinbackground.md)
  Called to cancel a load currently in progress.
- [- didLoadBytes:loadComplete:](./didloadbytes_loadcomplete_.md)
  Appends new data to the receiver’s resource data.
- [- endLoadInBackground](./endloadinbackground.md)
  Halts any background loading.
- [- expectedResourceDataSize](./expectedresourcedatasize.md)
  Returns the expected length of the resource data if it is provided by the server.
- [- failureReason](./failurereason.md)
  Returns a string describing the reason a load failed.
- [- flushCachedData](./flushcacheddata.md)
  Flushes any cached data for the URL served by this URL handle.
- [- loadInForeground](./loadinforeground.md)
  Loads the receiver’s data synchronously.
- [- resourceData](./resourcedata.md)
  Returns the resource data managed by the receiver, loading it if necessary.
- [- status](./status-c.method.md)
  Returns the status of the receiver.
- [NSURLHandle.Status](./status-swift.enum.md)
  These following constants are defined by `NSURLHandle` and are returned by [`status`](./status-c.method.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/loadinbackground)*
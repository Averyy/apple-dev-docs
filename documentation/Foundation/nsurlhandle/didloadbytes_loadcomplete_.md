# didLoadBytes:loadComplete:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends new data to the receiver’s resource data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (void) didLoadBytes:(NSData *) newBytes loadComplete:(BOOL) yorn;
```

#### Discussion

You should call this method when loading the resource data in the background.

## Parameters

- `newBytes`: The newly loaded bytes.
- `yorn`: [`true`](../../Swift/true.md) if newBytes contains the last piece of data for the URL, [`false`](../../Swift/false.md) otherwise.

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
- [- endLoadInBackground](./endloadinbackground.md)
  Halts any background loading.
- [- expectedResourceDataSize](./expectedresourcedatasize.md)
  Returns the expected length of the resource data if it is provided by the server.
- [- failureReason](./failurereason.md)
  Returns a string describing the reason a load failed.
- [- flushCachedData](./flushcacheddata.md)
  Flushes any cached data for the URL served by this URL handle.
- [- loadInBackground](./loadinbackground.md)
  Loads the receiver’s data in the background.
- [- loadInForeground](./loadinforeground.md)
  Loads the receiver’s data synchronously.
- [- resourceData](./resourcedata.md)
  Returns the resource data managed by the receiver, loading it if necessary.
- [- status](./status-c.method.md)
  Returns the status of the receiver.
- [NSURLHandle.Status](./status-swift.enum.md)
  These following constants are defined by `NSURLHandle` and are returned by [`status`](./status-c.method.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/didloadbytes:loadcomplete:)*
# NSURLHandle.Status

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These following constants are defined by `NSURLHandle` and are returned by [`status`](./status-c.method.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum Status
```

```c
enum NSURLHandleStatus : NSUInteger;
```

## Topics

### Constants
- [NSURLHandle.Status.notLoaded](./status-swift.enum/notloaded.md)
  The resource data has not been loaded.
- [NSURLHandle.Status.loadSucceeded](./status-swift.enum/loadsucceeded.md)
  The resource data was successfully loaded.
- [NSURLHandle.Status.loadInProgress](./status-swift.enum/loadinprogress.md)
  The resource data is in the process of loading.
- [NSURLHandle.Status.loadFailed](./status-swift.enum/loadfailed.md)
  The resource data failed to load.
### Initializers
- [init?(rawValue: UInt)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [- loadInBackground](./loadinbackground.md)
  Loads the receiver’s data in the background.
- [- loadInForeground](./loadinforeground.md)
  Loads the receiver’s data synchronously.
- [- resourceData](./resourcedata.md)
  Returns the resource data managed by the receiver, loading it if necessary.
- [- status](./status-c.method.md)
  Returns the status of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/status-swift.enum)*
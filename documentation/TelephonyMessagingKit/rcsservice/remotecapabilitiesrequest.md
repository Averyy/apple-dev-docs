# RCSService.RemoteCapabilitiesRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure representing a request to retrieve the capabilities of a remote handle.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RemoteCapabilitiesRequest
```

## Topics

### Creating a remote capabilities request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle, cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy)](./remotecapabilitiesrequest/init%28cellularserviceid,handle,cachepolicy%29.md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](./remotecapabilitiesrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](./remotecapabilitiesrequest/handle.md)
  The RCS handle, typically a phone number.
- [var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy](./remotecapabilitiesrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy](./remotecapabilitiesrequest/cachepolicy-swift.enum.md)
  Enumeration representing the cache policy to use in requests.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Discovering remote capabilities
- [func remoteCapabilities(for: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?](./remotecapabilities%28for%29.md)
  Requests remote capability discovery for a given handle
- [RCSService.RemoteCapabilities](./remotecapabilities.md)
  Structure representing the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest)*
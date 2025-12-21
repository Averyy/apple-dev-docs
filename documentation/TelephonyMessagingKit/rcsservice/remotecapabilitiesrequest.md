# RCSService.RemoteCapabilitiesRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure representing a request to retrieve the capabilities of a remote handle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct RemoteCapabilitiesRequest
```

## Topics

### Creating a remote capabilities request
- [init(cellularServiceID: CellularServiceID, handle: RCSHandle, cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy)](rcsservice/remotecapabilitiesrequest/init(cellularserviceid:handle:cachepolicy:).md)
### Accessing request properties
- [var cellularServiceID: CellularServiceID](rcsservice/remotecapabilitiesrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](rcsservice/remotecapabilitiesrequest/handle.md)
  The RCS handle, typically a phone number.
- [var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum.md)
  Enumeration representing the cache policy to use in requests.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func remoteCapabilities(for: RCSService.RemoteCapabilitiesRequest) async throws -> RCSService.RemoteCapabilities?](rcsservice/remotecapabilities(for:).md)
  Requests remote capability discovery for a given handle
- [RCSService.RemoteCapabilities](rcsservice/remotecapabilities.md)
  Structure representing the capabilities of a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest)*
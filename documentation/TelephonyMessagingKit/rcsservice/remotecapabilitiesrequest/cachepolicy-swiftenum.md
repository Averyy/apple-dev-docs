# RCSService.RemoteCapabilitiesRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the cache policy to use in requests.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum CachePolicy
```

## Topics

### Accessing cache policies
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOnly](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/cacheonly.md)
  Load from local cache.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOrRemote](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/cacheorremote.md)
  Load from local cache if available, otherwise load from remote.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/remotecapabilitiesrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](rcsservice/remotecapabilitiesrequest/handle.md)
  The RCS handle, typically a phone number.
- [var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum)*
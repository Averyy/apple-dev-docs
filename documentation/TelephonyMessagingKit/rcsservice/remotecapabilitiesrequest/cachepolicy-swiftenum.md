# RCSService.RemoteCapabilitiesRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the cache policy to use in requests.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

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
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/remotecapabilitiesrequest/cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](rcsservice/remotecapabilitiesrequest/handle.md)
  The RCS handle, typically a phone number.
- [var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.property.md)
  Cache policy to use for request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum)*
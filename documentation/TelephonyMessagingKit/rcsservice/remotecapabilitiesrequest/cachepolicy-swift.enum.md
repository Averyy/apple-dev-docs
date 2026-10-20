# RCSService.RemoteCapabilitiesRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration representing the cache policy to use in requests.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum CachePolicy
```

## Topics

### Accessing cache policies
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOnly](./cachepolicy-swift.enum/cacheonly.md)
  Load from local cache.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOrRemote](./cachepolicy-swift.enum/cacheorremote.md)
  Load from local cache if available, otherwise load from remote.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing request properties
- [var cellularServiceID: CellularServiceID](./cellularserviceid.md)
  Service identifier to use for this request.
- [var handle: RCSHandle](./handle.md)
  The RCS handle, typically a phone number.
- [var cachePolicy: RCSService.RemoteCapabilitiesRequest.CachePolicy](./cachepolicy-swift.property.md)
  Cache policy to use for request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum)*
# RCSService.RemoteCapabilitiesRequest.CachePolicy

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the cache policy to use in requests.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum CachePolicy
```

## Topics

### Accessing cache policies
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOnly](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/cacheonly.md)
  Load from local cache.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.remoteOnly](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/remoteonly.md)
  Load from remote.
- [RCSService.RemoteCapabilitiesRequest.CachePolicy.cacheOrRemote](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/cacheorremote.md)
  Load from local cache if available, otherwise load from remote.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.RemoteCapabilitiesRequest.CachePolicy, RCSService.RemoteCapabilitiesRequest.CachePolicy) -> Bool](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomStringConvertible Implementations](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/customstringconvertible-implementations.md)
- [Equatable Implementations](rcsservice/remotecapabilitiesrequest/cachepolicy-swift.enum/equatable-implementations.md)

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
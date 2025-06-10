# RCSService.RemoteCapabilities.Availability

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration indicating the availability of the remote end.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Availability
```

## Topics

### Determining availability
- [RCSService.RemoteCapabilities.Availability.available](rcsservice/remotecapabilities/availability-swift.enum/available.md)
  Remote end is available.
- [RCSService.RemoteCapabilities.Availability.unavailable](rcsservice/remotecapabilities/availability-swift.enum/unavailable.md)
  Remote end is not available.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/remotecapabilities/availability-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.RemoteCapabilities.Availability, RCSService.RemoteCapabilities.Availability) -> Bool](rcsservice/remotecapabilities/availability-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/remotecapabilities/availability-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/remotecapabilities/availability-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/remotecapabilities/availability-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/remotecapabilities/availability-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let availability: RCSService.RemoteCapabilities.Availability?](rcsservice/remotecapabilities/availability-swift.property.md)
  Availability of remote end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities/availability-swift.enum)*
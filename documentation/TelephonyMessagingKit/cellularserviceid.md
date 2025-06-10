# CellularServiceID

**Framework**: TelephonyMessagingKit  
**Kind**: struct

An opaque identifier that represents the cellular service for which to provide operations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CellularServiceID
```

#### Overview

The number of cellular services may vary across device types.

## Topics

### Encoding and decoding
- [init(from: any Decoder) throws](cellularserviceid/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](cellularserviceid/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](cellularserviceid/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](cellularserviceid/hashvalue.md)
  The hash value.
### Comparing cellular service IDs
- [static func == (CellularServiceID, CellularServiceID) -> Bool](cellularserviceid/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomStringConvertible Implementations](cellularserviceid/customstringconvertible-implementations.md)
- [Equatable Implementations](cellularserviceid/equatable-implementations.md)

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

- [let id: CellularServiceID](cellularservicestate/id-swift.property.md)
  The cellular service identifier associated with this instance.
- [let label: String](cellularservicestate/label.md)
  The label for a service, as set by the person using the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/cellularserviceid)*
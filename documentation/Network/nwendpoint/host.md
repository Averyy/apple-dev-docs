# NWEndpoint.Host

**Framework**: Network  
**Kind**: enum

A name or address that identifies a network endpoint.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum Host
```

## Topics

### Creating Hosts
- [init(String)](nwendpoint/host/init(_:).md)
  Initializes a host with a string.
### Accessing Host Types
- [case name(String, NWInterface?)](nwendpoint/host/name(_:_:).md)
  A host represented as a name.
- [NWEndpoint.Host.ipv4(_:)](nwendpoint/host/ipv4(_:).md)
  A host represented as an IPv4 address.
- [NWEndpoint.Host.ipv6(_:)](nwendpoint/host/ipv6(_:).md)
  A host represented as an IPv6 address.
### Requiring Interfaces
- [var interface: NWInterface?](nwendpoint/host/interface.md)
  The interface associated with this host, such as the interface scope stored in an IPv6 address.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NWEndpoint.Port](nwendpoint/port.md)
  A port number you use along with a host to identify a network endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/host)*
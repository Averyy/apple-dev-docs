# NWEndpoint.Host

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [init(String)](./host/init%28_%29.md)
  Initializes a host with a string.
### Accessing Host Types
- [case name(String, NWInterface?)](./host/name%28_,_%29.md)
  A host represented as a name.
- [NWEndpoint.Host.ipv4(_:)](./host/ipv4%28_%29.md)
  A host represented as an IPv4 address.
- [NWEndpoint.Host.ipv6(_:)](./host/ipv6%28_%29.md)
  A host represented as an IPv6 address.
### Requiring Interfaces
- [var interface: NWInterface?](./host/interface.md)
  The interface associated with this host, such as the interface scope stored in an IPv6 address.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Host and Ports
- [NWEndpoint.Port](./port.md)
  A port number you use along with a host to identify a network endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/host)*
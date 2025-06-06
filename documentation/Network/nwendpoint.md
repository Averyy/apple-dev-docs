# NWEndpoint

**Framework**: Network  
**Kind**: enum

A local or remote endpoint in a network connection.

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
enum NWEndpoint
```

## Topics

### Endpoint Types
- [case hostPort(host: NWEndpoint.Host, port: NWEndpoint.Port)](nwendpoint/hostport(host:port:).md)
  An endpoint represented as a host and port, with the host including both names and addresses.
- [case service(name: String, type: String, domain: String, interface: NWInterface?)](nwendpoint/service(name:type:domain:interface:).md)
  An endpoint represented as a Bonjour service.
- [NWEndpoint.url(_:)](nwendpoint/url(_:).md)
  An endpoint represented as a URL, with host and port values inferred from the URL.
- [case unix(path: String)](nwendpoint/unix(path:).md)
  An endpoint represented as a UNIX domain path.
### Host and Ports
- [NWEndpoint.Host](nwendpoint/host.md)
  A name or address that identifies a network endpoint.
- [NWEndpoint.Port](nwendpoint/port.md)
  A port number you use along with a host to identify a network endpoint.
### Internet Addresses
- [protocol IPAddress](ipaddress.md)
  An abstract protocol you use to interact with IP addresses.
- [struct IPv4Address](ipv4address.md)
  A structure containing an IPv4 address.
- [struct IPv6Address](ipv6address.md)
  A structure containing an IPv6 address.
### Endpoint Properties
- [var interface: NWInterface?](nwendpoint/interface.md)
  The optional interface associated with this endpoint, such as the interface on which it was discovered.
### Enumeration Cases
- [case opaque(nw_endpoint_t)](nwendpoint/opaque(_:).md)
### Instance Properties
- [var txtRecord: NWTXTRecord?](nwendpoint/txtrecord.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NWParameters](nwparameters.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint)*
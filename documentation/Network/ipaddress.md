# IPAddress

**Framework**: Network  
**Kind**: protocol

An abstract protocol you use to interact with IP addresses.

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
protocol IPAddress : Sendable
```

## Topics

### Creating Addresses
- [init?(String)](ipaddress/init(_:).md)
  Initializes an IP address with a string.
- [init?(Data, NWInterface?)](ipaddress/init(_:_:).md)
  Initializes an IP address with data.
### Inspecting Address Properties
- [var rawValue: Data](ipaddress/rawvalue.md)
  The raw data of an IP address.
- [var interface: NWInterface?](ipaddress/interface.md)
  The interface associated with this address, such as the IPv6 scoped interface.
- [var isLinkLocal: Bool](ipaddress/islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isLoopback: Bool](ipaddress/isloopback.md)
  A Boolean indicating whether this address is a loopback address for the local device.
- [var isMulticast: Bool](ipaddress/ismulticast.md)
  A Boolean indicating whether this address is a multicast address.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [IPv4Address](ipv4address.md)
- [IPv6Address](ipv6address.md)

## See Also

- [struct IPv4Address](ipv4address.md)
  A structure containing an IPv4 address.
- [struct IPv6Address](ipv6address.md)
  A structure containing an IPv6 address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipaddress)*
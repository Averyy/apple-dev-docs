# IPv4Address

**Framework**: Network  
**Kind**: struct

A structure containing an IPv4 address.

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
struct IPv4Address
```

## Topics

### Creating Addresses
- [init?(String)](ipv4address/init(_:).md)
  Initializes an IPv4 address with a string.
- [init?(Data, NWInterface?)](ipv4address/init(_:_:).md)
  Initializes an IPv4 address with data.
### Inspecting Address Properties
- [var rawValue: Data](ipv4address/rawvalue.md)
  The raw data of an IPv4 address.
- [let interface: NWInterface?](ipv4address/interface.md)
  The interface associated with this address.
- [var isLinkLocal: Bool](ipv4address/islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isLoopback: Bool](ipv4address/isloopback.md)
  A Boolean indicating whether this address is a loopback address for the local device.
- [var isMulticast: Bool](ipv4address/ismulticast.md)
  A Boolean indicating whether this address is a multicast address.
### Setting Well-Known Addresses
- [static let any: IPv4Address](ipv4address/any.md)
  The unspecified address (0.0.0.0).
- [static let broadcast: IPv4Address](ipv4address/broadcast.md)
  The local broadcast address (255.255.255.255).
- [static let loopback: IPv4Address](ipv4address/loopback.md)
  The device’s loopback address (127.0.0.1).
- [static let allHostsGroup: IPv4Address](ipv4address/allhostsgroup.md)
  The multicast group for all hosts on the network segment (224.0.0.1).
- [static let allRoutersGroup: IPv4Address](ipv4address/allroutersgroup.md)
  The multicast group for all routers on the network segment (224.0.0.2).
- [static let allReportsGroup: IPv4Address](ipv4address/allreportsgroup.md)
  The multicast group for all IGMPv3 reports (224.0.0.22).
- [static let mdnsGroup: IPv4Address](ipv4address/mdnsgroup.md)
  The multicast group for multicast DNS (224.0.0.251).

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [IPAddress](ipaddress.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol IPAddress](ipaddress.md)
  An abstract protocol you use to interact with IP addresses.
- [struct IPv6Address](ipv6address.md)
  A structure containing an IPv6 address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv4address)*
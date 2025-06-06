# IPv6Address

**Framework**: Network  
**Kind**: struct

A structure containing an IPv6 address.

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
struct IPv6Address
```

## Topics

### Creating Addresses
- [init?(String)](ipv6address/init(_:).md)
  Initializes an IPv6 address with a string.
- [init?(Data, NWInterface?)](ipv6address/init(_:_:).md)
  Initializes an IPv6 address with data.
- [var asIPv4: IPv4Address?](ipv6address/asipv4.md)
  Extracts the IPv4 address contained within the IPv6 address, if the IPv6 address is an IPv4-mapped or IPv4-compatible address.
### Inspecting Address Properties
- [var rawValue: Data](ipv6address/rawvalue.md)
  The raw data of an IPv6 address.
- [let interface: NWInterface?](ipv6address/interface.md)
  The IPv6 scoped interface associated with this address.
- [var multicastScope: IPv6Address.Scope?](ipv6address/multicastscope.md)
  The IPv6 multicast scope of the address.
- [IPv6Address.Scope](ipv6address/scope.md)
  An IPv6 multicast scope.
- [var isAny: Bool](ipv6address/isany.md)
  A Boolean indicating whether the address is the unspecified address (::).
- [var is6to4: Bool](ipv6address/is6to4.md)
  A Boolean indicating whether the address is a 6to4 address.
- [var isIPv4Compatabile: Bool](ipv6address/isipv4compatabile.md)
  A Boolean indicating whether the address is IPv4-compatible.
- [var isIPv4Mapped: Bool](ipv6address/isipv4mapped.md)
  A Boolean indicating whether the address is an IPv4-mapped address.
- [var isLinkLocal: Bool](ipv6address/islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isLoopback: Bool](ipv6address/isloopback.md)
  A Boolean indicating whether this address is a loopback address for the local device.
- [var isMulticast: Bool](ipv6address/ismulticast.md)
  A Boolean indicating whether this address is a multicast address.
### Setting Well-Known Addresses
- [static let any: IPv6Address](ipv6address/any.md)
  The unspecified address (::).
- [static let broadcast: IPv6Address](ipv6address/broadcast.md)
  The unspecified broadcast address (::).
- [static let loopback: IPv6Address](ipv6address/loopback.md)
  The device’s loopback address (::1).
- [static let nodeLocalNodes: IPv6Address](ipv6address/nodelocalnodes.md)
  The multicast address for all local nodes (ff01::1).
- [static let linkLocalNodes: IPv6Address](ipv6address/linklocalnodes.md)
  The multicast address for all link-local nodes (ff02::1).
- [static let linkLocalRouters: IPv6Address](ipv6address/linklocalrouters.md)
  The multicast address for all link-local routers (ff02::2).
### Instance Properties
- [var isUniqueLocal: Bool](ipv6address/isuniquelocal.md)

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
- [struct IPv4Address](ipv4address.md)
  A structure containing an IPv4 address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv6address)*
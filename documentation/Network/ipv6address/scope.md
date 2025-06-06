# IPv6Address.Scope

**Framework**: Network  
**Kind**: enum

An IPv6 multicast scope.

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
enum Scope
```

## Topics

### Scope Values
- [IPv6Address.Scope.nodeLocal](ipv6address/scope/nodelocal.md)
  The node-local multicast scope.
- [IPv6Address.Scope.linkLocal](ipv6address/scope/linklocal.md)
  The link-local multicast scope.
- [IPv6Address.Scope.siteLocal](ipv6address/scope/sitelocal.md)
  The site-local multicast scope.
- [IPv6Address.Scope.organizationLocal](ipv6address/scope/organizationlocal.md)
  The organization-local multicast scope.
- [IPv6Address.Scope.global](ipv6address/scope/global.md)
  The global multicast scope.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var rawValue: Data](ipv6address/rawvalue.md)
  The raw data of an IPv6 address.
- [let interface: NWInterface?](ipv6address/interface.md)
  The IPv6 scoped interface associated with this address.
- [var multicastScope: IPv6Address.Scope?](ipv6address/multicastscope.md)
  The IPv6 multicast scope of the address.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv6address/scope)*
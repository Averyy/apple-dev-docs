# IPv6Address.Scope

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [IPv6Address.Scope.nodeLocal](./scope/nodelocal.md)
  The node-local multicast scope.
- [IPv6Address.Scope.linkLocal](./scope/linklocal.md)
  The link-local multicast scope.
- [IPv6Address.Scope.siteLocal](./scope/sitelocal.md)
  The site-local multicast scope.
- [IPv6Address.Scope.organizationLocal](./scope/organizationlocal.md)
  The organization-local multicast scope.
- [IPv6Address.Scope.global](./scope/global.md)
  The global multicast scope.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Inspecting Address Properties
- [var rawValue: Data](./rawvalue.md)
  The raw data of an IPv6 address.
- [let interface: NWInterface?](./interface.md)
  The IPv6 scoped interface associated with this address.
- [var multicastScope: IPv6Address.Scope?](./multicastscope.md)
  The IPv6 multicast scope of the address.
- [var isAny: Bool](./isany.md)
  A Boolean indicating whether the address is the unspecified address (::).
- [var is6to4: Bool](./is6to4.md)
  A Boolean indicating whether the address is a 6to4 address.
- [var isIPv4Compatabile: Bool](./isipv4compatabile.md)
  A Boolean indicating whether the address is IPv4-compatible.
- [var isIPv4Mapped: Bool](./isipv4mapped.md)
  A Boolean indicating whether the address is an IPv4-mapped address.
- [var isLinkLocal: Bool](./islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isLoopback: Bool](./isloopback.md)
  A Boolean indicating whether this address is a loopback address for the local device.
- [var isMulticast: Bool](./ismulticast.md)
  A Boolean indicating whether this address is a multicast address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipv6address/scope)*
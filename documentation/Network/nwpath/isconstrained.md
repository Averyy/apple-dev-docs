# isConstrained

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the path uses an interface in Low Data Mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isConstrained: Bool { get }
```

## See Also

### Checking Path Capabilities
- [let supportsIPv4: Bool](./supportsipv4.md)
  A Boolean indicating whether the path can route IPv4 traffic.
- [let supportsIPv6: Bool](./supportsipv6.md)
  A Boolean indicating whether the path can route IPv6 traffic.
- [let supportsDNS: Bool](./supportsdns.md)
  A Boolean indicating whether the path has a DNS server configured.
- [let isExpensive: Bool](./isexpensive.md)
  A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/isconstrained)*
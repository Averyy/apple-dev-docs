# NEIPv4Settings

**Framework**: Network Extension  
**Kind**: class

The IPv4 settings of an IP layer network tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEIPv4Settings
```

#### Overview

To specify the IPv4 settings of a packet tunnel, set its [`NEPacketTunnelNetworkSettings`](nepackettunnelnetworksettings.md).[`ipv4Settings`](nepackettunnelnetworksettings/ipv4settings.md) property to an instance of this class.

## Topics

### Initializing IPv4 settings
- [init(addresses: [String], subnetMasks: [String])](neipv4settings/init(addresses:subnetmasks:).md)
  Initializes an IPv4 settings object.
### Accessing IPv4 properties
- [var addresses: [String]](neipv4settings/addresses.md)
  The IPv4 addresses to assign to the TUN interface.
- [var subnetMasks: [String]](neipv4settings/subnetmasks.md)
  The IPv4 network masks to assign to the TUN interface.
- [var router: String?](neipv4settings/router.md)
  The address of the next-hop gateway router represented as a dotted decimal string.
### Routing network traffic
- [var includedRoutes: [NEIPv4Route]?](neipv4settings/includedroutes.md)
  The IPv4 network traffic that the system routes to the TUN interface.
- [var excludedRoutes: [NEIPv4Route]?](neipv4settings/excludedroutes.md)
  The IPv4 network traffic that the system routes to the primary physical interface, not the TUN interface.
- [class NEIPv4Route](neipv4route.md)
  The settings for an IPv4 route.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var ipv4Settings: NEIPv4Settings?](nepackettunnelnetworksettings/ipv4settings.md)
  The tunnel IP version 4 settings.
- [var ipv6Settings: NEIPv6Settings?](nepackettunnelnetworksettings/ipv6settings.md)
  The tunnel IP version 6 settings.
- [class NEIPv6Settings](neipv6settings.md)
  The IPv6 settings of an IP layer network tunnel.
- [var tunnelOverheadBytes: NSNumber?](nepackettunnelnetworksettings/tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.
- [var mtu: NSNumber?](nepackettunnelnetworksettings/mtu.md)
  The size of the maximum trasnmission unit, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4settings)*
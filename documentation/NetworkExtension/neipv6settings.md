# NEIPv6Settings

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The IPv6 settings of an IP layer network tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEIPv6Settings
```

```objc
@interface NEIPv6Settings : NSObject
```

#### Overview

To specify the IPv6 settings of a packet tunnel, set its [`NEPacketTunnelNetworkSettings`](./nepackettunnelnetworksettings.md).[`ipv6Settings`](./nepackettunnelnetworksettings/ipv6settings.md) property to an instance of this class.

## Topics

### Initializing IPv6 settings
- [init(addresses: [String], networkPrefixLengths: [NSNumber])](./neipv6settings/init%28addresses,networkprefixlengths%29.md)
  Initializes the IPv6 settings object.
### Accessing IPv6 properties
- [var addresses: [String]](./neipv6settings/addresses.md)
  The IPv6 addresses to assign to the TUN interface.
- [var networkPrefixLengths: [NSNumber]](./neipv6settings/networkprefixlengths.md)
  The IPv6 network prefix lengths to assign to the TUN interface.
### Routing network traffic
- [var includedRoutes: [NEIPv6Route]?](./neipv6settings/includedroutes.md)
  The IPv6 network traffic that the system routes to the TUN interface.
- [var excludedRoutes: [NEIPv6Route]?](./neipv6settings/excludedroutes.md)
  The IPv6 network traffic that the system routes to the primary physical interface, not the TUN interface.
- [class NEIPv6Route](./neipv6route.md)
  The settings for an IPv6 route.
### Type Methods
- [+ settingsWithAutomaticAddressing](./neipv6settings/settingswithautomaticaddressing.md)
- [+ settingsWithLinkLocalAddressing](./neipv6settings/settingswithlinklocaladdressing.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Accessing network properties
- [var ipv4Settings: NEIPv4Settings?](./nepackettunnelnetworksettings/ipv4settings.md)
  The tunnel IP version 4 settings.
- [class NEIPv4Settings](./neipv4settings.md)
  The IPv4 settings of an IP layer network tunnel.
- [var ipv6Settings: NEIPv6Settings?](./nepackettunnelnetworksettings/ipv6settings.md)
  The tunnel IP version 6 settings.
- [var tunnelOverheadBytes: NSNumber?](./nepackettunnelnetworksettings/tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.
- [var mtu: NSNumber?](./nepackettunnelnetworksettings/mtu.md)
  The size of the maximum trasnmission unit, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6settings)*
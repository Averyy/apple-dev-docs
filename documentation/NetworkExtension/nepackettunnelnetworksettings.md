# NEPacketTunnelNetworkSettings

**Framework**: Network Extension  
**Kind**: class

The configuration for a packet tunnel provider’s virtual interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEPacketTunnelNetworkSettings
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

## Topics

### Accessing network properties
- [var ipv4Settings: NEIPv4Settings?](nepackettunnelnetworksettings/ipv4settings.md)
  The tunnel IP version 4 settings.
- [class NEIPv4Settings](neipv4settings.md)
  The IPv4 settings of an IP layer network tunnel.
- [var ipv6Settings: NEIPv6Settings?](nepackettunnelnetworksettings/ipv6settings.md)
  The tunnel IP version 6 settings.
- [class NEIPv6Settings](neipv6settings.md)
  The IPv6 settings of an IP layer network tunnel.
- [var tunnelOverheadBytes: NSNumber?](nepackettunnelnetworksettings/tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.
- [var mtu: NSNumber?](nepackettunnelnetworksettings/mtu.md)
  The size of the maximum trasnmission unit, in bytes.

## Relationships

### Inherits From
- [NETunnelNetworkSettings](netunnelnetworksettings.md)
### Inherited By
- [NEEthernetTunnelNetworkSettings](neethernettunnelnetworksettings.md)
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

- [class NEPacketTunnelProvider](nepackettunnelprovider.md)
  The principal class for a packet tunnel provider app extension.
- [class NETunnelProvider](netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NEProvider](neprovider.md)
  An abstract base class for all NetworkExtension providers.
- [class NETunnelNetworkSettings](netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.
- [class NEEthernetTunnelProvider](neethernettunnelprovider.md)
  A type that implements the client side of a custom link-layer packet tunneling protocol.
- [class NEEthernetTunnelNetworkSettings](neethernettunnelnetworksettings.md)
  The network settings for an ethernet-based VPN tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings)*
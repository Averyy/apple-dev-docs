# NEEthernetTunnelNetworkSettings

**Framework**: Network Extension  
**Kind**: class

The network settings for an ethernet-based VPN tunnel.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class NEEthernetTunnelNetworkSettings
```

#### Overview

You use this type with [`NEEthernetTunnelProvider`](neethernettunnelprovider.md) instances to communicate the desired network settings for the packet tunnel to the framework. The framework takes care of applying the contained settings to the system.

Instances of this class are thread-safe.

## Topics

### Creating a settings instance
- [init(tunnelRemoteAddress: String, ethernetAddress: String, mtu: Int)](neethernettunnelnetworksettings/init(tunnelremoteaddress:ethernetaddress:mtu:).md)
  Creates a settings object with a given tunnel remote address and MAC address.
### Inspecting settings properties
- [var ethernetAddress: String](neethernettunnelnetworksettings/ethernetaddress.md)
  The ethernet address of the tunnel interface, as a string.

## Relationships

### Inherits From
- [NEPacketTunnelNetworkSettings](nepackettunnelnetworksettings.md)
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
- [class NEPacketTunnelNetworkSettings](nepackettunnelnetworksettings.md)
  The configuration for a packet tunnel provider’s virtual interface.
- [class NETunnelNetworkSettings](netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.
- [class NEEthernetTunnelProvider](neethernettunnelprovider.md)
  A type that implements the client side of a custom link-layer packet tunneling protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neethernettunnelnetworksettings)*
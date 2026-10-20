# NETunnelNetworkSettings

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The configuration for a tunnel provider’s virtual interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NETunnelNetworkSettings
```

```objc
@interface NETunnelNetworkSettings : NSObject
```

## Topics

### Initializing tunnel network settings
- [init(tunnelRemoteAddress: String)](./netunnelnetworksettings/init%28tunnelremoteaddress%29.md)
  Initialize a `NETunnelNetworkSettings` object.
### Accessing tunnel network settings
- [var tunnelRemoteAddress: String](./netunnelnetworksettings/tunnelremoteaddress.md)
  The IP address of the tunnel server.
- [var dnsSettings: NEDNSSettings?](./netunnelnetworksettings/dnssettings.md)
  The tunnel DNS settings.
- [class NEDNSSettings](./nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
- [var proxySettings: NEProxySettings?](./netunnelnetworksettings/proxysettings.md)
  The tunnel HTTP proxy settings.
- [class NEProxySettings](./neproxysettings.md)
  `NEProxySettings` contains HTTP proxy settings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NEPacketTunnelNetworkSettings](./nepackettunnelnetworksettings.md)
- [NETransparentProxyNetworkSettings](./netransparentproxynetworksettings.md)
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

### App proxy provider
- [class NEAppProxyProvider](./neappproxyprovider.md)
  The principal class for an app proxy provider app extension.
- [class NETunnelProvider](./netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NEProvider](./neprovider.md)
  An abstract base class for all NetworkExtension providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings)*
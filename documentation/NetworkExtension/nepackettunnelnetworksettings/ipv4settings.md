# ipv4Settings

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The tunnel IP version 4 settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var ipv4Settings: NEIPv4Settings? { get set }
```

```objc
@property (copy, nullable) NEIPv4Settings * IPv4Settings;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

#### Discussion

This property contains the IPv4 routes specifying what IPv4 traffic to route to the tunnel, as well as the IPv4 address and netmask to assign to the TUN interface.

## See Also

### Accessing network properties
- [class NEIPv4Settings](../neipv4settings.md)
  The IPv4 settings of an IP layer network tunnel.
- [var ipv6Settings: NEIPv6Settings?](./ipv6settings.md)
  The tunnel IP version 6 settings.
- [class NEIPv6Settings](../neipv6settings.md)
  The IPv6 settings of an IP layer network tunnel.
- [var tunnelOverheadBytes: NSNumber?](./tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.
- [var mtu: NSNumber?](./mtu.md)
  The size of the maximum trasnmission unit, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/ipv4settings)*
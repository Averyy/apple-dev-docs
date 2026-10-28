# ipv6Settings

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The tunnel IP version 6 settings.

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
var ipv6Settings: NEIPv6Settings? { get set }
```

```objc
@property (copy, nullable) NEIPv6Settings * IPv6Settings;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

## Discussion

This property contains the IPv6 routes specifying what IPv6 traffic to route to the tunnel, as well as the IPv6 address and network prefix to assign to the TUN interface.

## See Also

### Accessing network properties
- [var ipv4Settings: NEIPv4Settings?](./ipv4settings.md)
  The tunnel IP version 4 settings.
- [class NEIPv4Settings](../neipv4settings.md)
  The IPv4 settings of an IP layer network tunnel.
- [class NEIPv6Settings](../neipv6settings.md)
  The IPv6 settings of an IP layer network tunnel.
- [var tunnelOverheadBytes: NSNumber?](./tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.
- [var mtu: NSNumber?](./mtu.md)
  The size of the maximum trasnmission unit, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/ipv6settings)*
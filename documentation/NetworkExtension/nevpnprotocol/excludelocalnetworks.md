# excludeLocalNetworks

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var excludeLocalNetworks: Bool { get set }
```

```objc
@property BOOL excludeLocalNetworks;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

#### Discussion

If this property is [`true`](../../Swift/true.md), the system excludes network connections to hosts on the local network — such as AirPlay, AirDrop, and CarPlay — but only when the [`includeAllNetworks`](./includeallnetworks.md) or [`enforceRoutes`](./enforceroutes.md) property is also [`true`](../../Swift/true.md). [`NETransparentProxyManager`](../netransparentproxymanager.md) doesn’t support this property.

The default value for this property is [`false`](../../Swift/false.md) in macOS and [`true`](../../Swift/true.md) in iOS`.`

## See Also

### Routing network traffic
- [var includeAllNetworks: Bool](./includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeAPNs: Bool](./excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](./excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var enforceRoutes: Bool](./enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/excludelocalnetworks)*
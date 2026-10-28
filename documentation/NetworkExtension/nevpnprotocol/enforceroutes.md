# enforceRoutes

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var enforceRoutes: Bool { get set }
```

```objc
@property BOOL enforceRoutes;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

## Discussion

If this property is [`true`](../../Swift/true.md) when the [`includeAllNetworks`](./includeallnetworks.md) property is [`false`](../../Swift/false.md), the system scopes the included routes to the VPN and the excluded routes to the current primary network interface. This property supersedes the system routing table and scoping operations by apps.

If you set both the [`enforceRoutes`](./enforceroutes.md) and [`excludeLocalNetworks`](./excludelocalnetworks.md) properties to [`true`](../../Swift/true.md), the system excludes network connections to hosts on the local network.

[`NETransparentProxyManager`](../netransparentproxymanager.md) doesn’t support this property. The default value for this property is [`false`](../../Swift/false.md).

> **Note**:  You specify the included and excluded routes using the respective `includedRoutes` and `excludedRoutes` properties in the [`NEIPv4Settings`](../neipv4settings.md) and [`NEIPv6Settings`](../neipv6settings.md) objects that you provide in the [`NEPacketTunnelProvider`](../nepackettunnelprovider.md) settings.

## See Also

### Routing network traffic
- [var includeAllNetworks: Bool](./includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeAPNs: Bool](./excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](./excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](./excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/enforceroutes)*
# enforceRoutes

**Framework**: Network Extension  
**Kind**: property

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

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true) when the [`includeAllNetworks`](nevpnprotocol/includeallnetworks.md) property is [`false`](https://developer.apple.com/documentation/swift/false), the system scopes the included routes to the VPN and the excluded routes to the current primary network interface. This property supersedes the system routing table and scoping operations by apps.

If you set both the [`enforceRoutes`](nevpnprotocol/enforceroutes.md) and [`excludeLocalNetworks`](nevpnprotocol/excludelocalnetworks.md) properties to [`true`](https://developer.apple.com/documentation/swift/true), the system excludes network connections to hosts on the local network.

[`NETransparentProxyManager`](netransparentproxymanager.md) doesn’t support this property. The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  You specify the included and excluded routes using the respective `includedRoutes` and `excludedRoutes` properties in the [`NEIPv4Settings`](neipv4settings.md) and [`NEIPv6Settings`](neipv6settings.md) objects that you provide in the [`NEPacketTunnelProvider`](nepackettunnelprovider.md) settings.

## See Also

- [var includeAllNetworks: Bool](nevpnprotocol/includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeAPNs: Bool](nevpnprotocol/excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](nevpnprotocol/excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](nevpnprotocol/excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/enforceroutes)*
# excludeAPNs

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var excludeAPNs: Bool { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system excludes Apple Push Notification services (APNs) traffic, but only when the [`includeAllNetworks`](nevpnprotocol/includeallnetworks.md) property is also [`true`](https://developer.apple.com/documentation/Swift/true). [`NETransparentProxyManager`](netransparentproxymanager.md) doesn’t support this property.

The default value for this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var includeAllNetworks: Bool](nevpnprotocol/includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeCellularServices: Bool](nevpnprotocol/excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](nevpnprotocol/excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.
- [var enforceRoutes: Bool](nevpnprotocol/enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/excludeapns)*
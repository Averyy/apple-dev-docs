# excludeLocalNetworks

**Framework**: Network Extension  
**Kind**: property

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

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system excludes network connections to hosts on the local network — such as AirPlay, AirDrop, and CarPlay — but only when the [`includeAllNetworks`](nevpnprotocol/includeallnetworks.md) or [`enforceRoutes`](nevpnprotocol/enforceroutes.md) property is also [`true`](https://developer.apple.com/documentation/Swift/true). [`NETransparentProxyManager`](netransparentproxymanager.md) doesn’t support this property.

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false) in macOS and [`true`](https://developer.apple.com/documentation/Swift/true) in iOS`.`

## See Also

- [var includeAllNetworks: Bool](nevpnprotocol/includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeAPNs: Bool](nevpnprotocol/excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](nevpnprotocol/excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var enforceRoutes: Bool](nevpnprotocol/enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/excludelocalnetworks)*
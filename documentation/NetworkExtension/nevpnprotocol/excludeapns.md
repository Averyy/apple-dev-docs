# excludeAPNs

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL excludeAPNs;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

## Discussion

If this property is [`true`](../../Swift/true.md), the system excludes Apple Push Notification services (APNs) traffic, but only when the [`includeAllNetworks`](./includeallnetworks.md) property is also [`true`](../../Swift/true.md). [`NETransparentProxyManager`](../netransparentproxymanager.md) doesn’t support this property.

The default value for this property is [`true`](../../Swift/true.md).

## See Also

### Routing network traffic
- [var includeAllNetworks: Bool](./includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeCellularServices: Bool](./excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](./excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.
- [var enforceRoutes: Bool](./enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/excludeapns)*
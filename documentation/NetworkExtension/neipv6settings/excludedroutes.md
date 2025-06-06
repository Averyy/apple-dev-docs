# excludedRoutes

**Framework**: Network Extension  
**Kind**: property

The IPv6 network traffic that the system routes to the primary physical interface, not the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var excludedRoutes: [NEIPv6Route]? { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

This property excludes routes that the system might otherwise include from the [`includedRoutes`](neipv6settings/includedroutes.md) property. The system automatically excludes the IP address of the tunnel server.

## See Also

- [var includedRoutes: [NEIPv6Route]?](neipv6settings/includedroutes.md)
  The IPv6 network traffic that the system routes to the TUN interface.
- [class NEIPv6Route](neipv6route.md)
  The settings for an IPv6 route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6settings/excludedroutes)*
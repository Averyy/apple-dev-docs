# includedRoutes

**Framework**: Network Extension  
**Kind**: property

The IPv6 network traffic that the system routes to the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var includedRoutes: [NEIPv6Route]? { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If you include the default route (`0.0.0.0/0` or `::/0`) in this property, the system routes traffic that doesn’t match a specific rule in the system routing table through the VPN.

## See Also

- [var excludedRoutes: [NEIPv6Route]?](neipv6settings/excludedroutes.md)
  The IPv6 network traffic that the system routes to the primary physical interface, not the TUN interface.
- [class NEIPv6Route](neipv6route.md)
  The settings for an IPv6 route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6settings/includedroutes)*
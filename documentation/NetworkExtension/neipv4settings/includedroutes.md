# includedRoutes

**Framework**: Network Extension  
**Kind**: property

The IPv4 network traffic that the system routes to the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var includedRoutes: [NEIPv4Route]? { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If you include the default route (`0.0.0.0/0` or `::/0`) in this property, the system routes traffic that doesn’t match a specific rule in the system routing table through the VPN.

## See Also

- [var excludedRoutes: [NEIPv4Route]?](neipv4settings/excludedroutes.md)
  The IPv4 network traffic that the system routes to the primary physical interface, not the TUN interface.
- [class NEIPv4Route](neipv4route.md)
  The settings for an IPv4 route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4settings/includedroutes)*
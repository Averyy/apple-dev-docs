# includeAllNetworks

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether the system sends most network traffic over the tunnel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var includeAllNetworks: Bool { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), the system routes network traffic through the tunnel except traffic for designated system services necessary for maintaining expected device functionality.

You can exclude some types of traffic using the [`excludeAPNs`](nevpnprotocol/excludeapns.md), [`excludeLocalNetworks`](nevpnprotocol/excludelocalnetworks.md), and [`excludeCellularServices`](nevpnprotocol/excludecellularservices.md) properties in combination with this property. The system always excludes the following network traffic from the tunnel regardless of this property value:

- Network control plane traffic that maintains a device’s connection to the local network, such as DHCP.
- Captive portal negotiation traffic that authorizes a device with a Wi-Fi hotspot.
- Certain cellular services traffic that uses the cellular network only, such as VoLTE.
- Traffic that communicates with a companion device, such as an Apple Watch.

[`NETransparentProxyManager`](netransparentproxymanager.md) doesn’t support this property. The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var excludeAPNs: Bool](nevpnprotocol/excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](nevpnprotocol/excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](nevpnprotocol/excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.
- [var enforceRoutes: Bool](nevpnprotocol/enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/includeallnetworks)*
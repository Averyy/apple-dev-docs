# excludeLocalNetworks

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var excludeLocalNetworks: NEPacketTunnelNetworkSettings.IPFamily { get set }
```

#### Discussion

If this property is set, traffic destined for local networks will be excluded from the tunnel. The set value of NEPacketTunnelNetworkSettingsIPFamily type indicates if excludeLocalNetworks should be applied to all traffic, IPv4 only or IPv6 only. The default is NEPacketTunnelNetworkSettingsIPFamilyNone on macOS and NEPacketTunnelNetworkSettingsIPFamilyAny on iOS. If either the includeAllNetworks or the enforceRoutes property in NEVPNProtocol class is set, then the excludeLocalNetworks property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludelocalnetworks)*
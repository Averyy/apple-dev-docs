# excludeLocalNetworks

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

## Declaration

```objc
@property NEPacketTunnelNetworkSettingsIPFamily excludeLocalNetworks;
```

#### Discussion

If this property is set, traffic destined for local networks will be excluded from the tunnel. The set value of NEPacketTunnelNetworkSettingsIPFamily type indicates if excludeLocalNetworks should be applied to all traffic, IPv4 only or IPv6 only. The default is NEPacketTunnelNetworkSettingsIPFamilyNone on macOS and NEPacketTunnelNetworkSettingsIPFamilyAny on iOS. If either the includeAllNetworks or the enforceRoutes property in NEVPNProtocol class is set, then the excludeLocalNetworks property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludelocalnetworks)*
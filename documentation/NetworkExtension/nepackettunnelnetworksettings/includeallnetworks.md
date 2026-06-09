# includeAllNetworks

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
var includeAllNetworks: NEPacketTunnelNetworkSettings.IPFamily { get set }
```

#### Discussion

If this property is set then all network traffic is routed through the tunnel, with some exclusions. Several of the exclusions can be controlled with the excludeLocalNetworks, excludeCellularServices, excludeAPNs and excludeDeviceCommunication properties. See the documentation for those properties. The set value of NEPacketTunnelNetworkSettingsIPFamily type indicates if includeAllNetworks should be applied to all traffic, IPv4 only or IPv6 only. The following traffic is always excluded from the tunnel:

- Traffic necessary for connecting and maintaining the device’s network connection, such as DHCP.
- Traffic necessary for connecting to captive networks.
- Certain cellular services traffic that is not routable over the internet and is instead directly routed to the cellular network. See the excludeCellularServices property for more details.
- Network communication with a companion device such as a watchOS device. The default value of this property is NEPacketTunnelNetworkSettingsIPFamilyNone, disabling includeAllNetworks. The includeAllNetworks property in NEVPNProtocol class takes precedence if set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/includeallnetworks)*
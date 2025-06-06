# NEHotspotNetworkSecurityType

**Framework**: Network Extension  
**Kind**: enum

An enumeration of constants that define Wi-Fi hotspot network security types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum NEHotspotNetworkSecurityType
```

## Topics

### Security types
- [NEHotspotNetworkSecurityType.open](nehotspotnetworksecuritytype/open.md)
  A security type to represent an open network with no security protocol.
- [NEHotspotNetworkSecurityType.WEP](nehotspotnetworksecuritytype/wep.md)
  A security type to represent use of Wired Equivalent Privacy (WEP).
- [NEHotspotNetworkSecurityType.personal](nehotspotnetworksecuritytype/personal.md)
  A security type to represent use of Wi-Fi protected access (WPA), WPA2, and WPA3 standards using a pre-shared secret.
- [NEHotspotNetworkSecurityType.enterprise](nehotspotnetworksecuritytype/enterprise.md)
  A security type to represent use of Wi-Fi protected access (WPA), WPA2, and WPA3 standards using enterprise-level seciurity.
- [NEHotspotNetworkSecurityType.unknown](nehotspotnetworksecuritytype/unknown.md)
  A value that represents an unknown security type.
### Initializers
- [init?(rawValue: Int)](nehotspotnetworksecuritytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var ssid: String](nehotspotnetwork/ssid.md)
  The SSID for the Wi-Fi network.
- [var bssid: String](nehotspotnetwork/bssid.md)
  The BSSID for the Wi-Fi network.
- [var signalStrength: Double](nehotspotnetwork/signalstrength.md)
  The recent signal strength for the Wi-Fi network.
- [var isSecure: Bool](nehotspotnetwork/issecure.md)
  Indicates whether the network is secure
- [var didAutoJoin: Bool](nehotspotnetwork/didautojoin.md)
  Indicates whether the network was joined automatically or was joined explicitly by the user.
- [var didJustJoin: Bool](nehotspotnetwork/didjustjoin.md)
  Indicates whether the network was just joined.
- [var isChosenHelper: Bool](nehotspotnetwork/ischosenhelper.md)
  Indicates whether the calling Hotspot Helper is the chosen helper for this network.
- [var securityType: NEHotspotNetworkSecurityType](nehotspotnetwork/securitytype.md)
  The type of security used by the Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetworksecuritytype)*
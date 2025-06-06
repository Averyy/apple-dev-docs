# securityType

**Framework**: Network Extension  
**Kind**: property

The type of security used by the Wi-Fi network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var securityType: NEHotspotNetworkSecurityType { get }
```

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
- [enum NEHotspotNetworkSecurityType](nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/securitytype)*
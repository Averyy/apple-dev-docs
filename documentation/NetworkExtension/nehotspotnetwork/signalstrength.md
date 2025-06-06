# signalStrength

**Framework**: Network Extension  
**Kind**: property

The recent signal strength for the Wi-Fi network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var signalStrength: Double { get }
```

#### Discussion

The value of this property lies within the range 0.0 (weak/no signal) to 1.0 (strong signal).

## See Also

- [var ssid: String](nehotspotnetwork/ssid.md)
  The SSID for the Wi-Fi network.
- [var bssid: String](nehotspotnetwork/bssid.md)
  The BSSID for the Wi-Fi network.
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
- [enum NEHotspotNetworkSecurityType](nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/signalstrength)*
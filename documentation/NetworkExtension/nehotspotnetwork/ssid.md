# ssid

**Framework**: Network Extension  
**Kind**: property

The SSID for the Wi-Fi network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var ssid: String { get }
```

## See Also

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
- [enum NEHotspotNetworkSecurityType](nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/ssid)*
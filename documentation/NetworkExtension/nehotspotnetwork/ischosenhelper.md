# isChosenHelper

**Framework**: Network Extension  
**Kind**: property

Indicates whether the calling Hotspot Helper is the chosen helper for this network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isChosenHelper: Bool { get }
```

#### Discussion

The `NEHotspotNetwork` class must have been instantiated via a call to the `supportedNetworkInterfaces` method in the [`NEHotspotHelper`](nehotspothelper.md) object. This property is useful for restoring state after the Hotspot Helper application has quit and restarted.

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
- [var securityType: NEHotspotNetworkSecurityType](nehotspotnetwork/securitytype.md)
  The type of security used by the Wi-Fi network.
- [enum NEHotspotNetworkSecurityType](nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/ischosenhelper)*
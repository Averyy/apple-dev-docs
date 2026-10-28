# didJustJoin

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

Indicates whether the network was just joined.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var didJustJoin: Bool { get }
```

```objc
@property (readonly, getter=didJustJoin) BOOL justJoined;
```

## Discussion

This property is useful in the Maintaining state to differentiate whether the Maintain command is for the initial join, or the subsequent periodic callback.

## See Also

### Network information
- [var ssid: String](./ssid.md)
  The SSID for the Wi-Fi network.
- [var bssid: String](./bssid.md)
  The BSSID for the Wi-Fi network.
- [var signalStrength: Double](./signalstrength.md)
  The recent signal strength for the Wi-Fi network.
- [var isSecure: Bool](./issecure.md)
  Indicates whether the network is secure
- [var didAutoJoin: Bool](./didautojoin.md)
  Indicates whether the network was joined automatically or was joined explicitly by the user.
- [var isChosenHelper: Bool](./ischosenhelper.md)
  Indicates whether the calling Hotspot Helper is the chosen helper for this network.
- [var securityType: NEHotspotNetworkSecurityType](./securitytype.md)
  The type of security used by the Wi-Fi network.
- [enum NEHotspotNetworkSecurityType](../nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/didjustjoin)*
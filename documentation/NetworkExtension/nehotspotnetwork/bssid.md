# bssid

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The BSSID for the Wi-Fi network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var bssid: String { get }
```

```objc
@property (readonly) NSString * BSSID;
```

## See Also

### Network information
- [var ssid: String](./ssid.md)
  The SSID for the Wi-Fi network.
- [var signalStrength: Double](./signalstrength.md)
  The recent signal strength for the Wi-Fi network.
- [var isSecure: Bool](./issecure.md)
  Indicates whether the network is secure
- [var didAutoJoin: Bool](./didautojoin.md)
  Indicates whether the network was joined automatically or was joined explicitly by the user.
- [var didJustJoin: Bool](./didjustjoin.md)
  Indicates whether the network was just joined.
- [var isChosenHelper: Bool](./ischosenhelper.md)
  Indicates whether the calling Hotspot Helper is the chosen helper for this network.
- [var securityType: NEHotspotNetworkSecurityType](./securitytype.md)
  The type of security used by the Wi-Fi network.
- [enum NEHotspotNetworkSecurityType](../nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/bssid)*
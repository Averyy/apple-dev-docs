# NEHotspotNetwork

**Framework**: Network Extension  
**Kind**: class

Information about a Wi-Fi network associated with a command or a response.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class NEHotspotNetwork
```

#### Overview

When the Hotspot Helper app is asked to evaluate the a network or filter the Wi-Fi scan list, it annotates the  `NEHotspotNetwork` object via the `setConfidence:` method.

## Topics

### Network information
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
- [enum NEHotspotNetworkSecurityType](nehotspotnetworksecuritytype.md)
  An enumeration of constants that define Wi-Fi hotspot network security types.
### Network annotation
- [func setConfidence(NEHotspotHelperConfidence)](nehotspotnetwork/setconfidence(_:).md)
  Indicate the level of confidence in being able to handle the network.
- [enum NEHotspotHelperConfidence](nehotspothelperconfidence.md)
  A type that indicates the hotspot helper’s confidence in its ability to handle the network.
- [func setPassword(String)](nehotspotnetwork/setpassword(_:).md)
  Provide the password for a protected network.
### Fetching VPN network information
- [class func fetchCurrent(completionHandler: (NEHotspotNetwork?) -> Void)](nehotspotnetwork/fetchcurrent(completionhandler:).md)
  Fetches information about the current Wi-Fi network.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEHotspotHelperCommand](nehotspothelpercommand.md)
  A command for the hotspot helper to handle.
- [class NEHotspotHelperResponse](nehotspothelperresponse.md)
  The hotspot helper’s response to a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork)*
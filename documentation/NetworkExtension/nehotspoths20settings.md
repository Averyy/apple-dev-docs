# NEHotspotHS20Settings

**Framework**: Network Extension  
**Kind**: class

Settings for configuring Hotspot 2.0 Wi-Fi networks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEHotspotHS20Settings
```

## Topics

### Initializing Hotspot 2.0 settings
- [init(domainName: String, roamingEnabled: Bool)](nehotspoths20settings/init(domainname:roamingenabled:).md)
  Creates a new hotspot configuration of a legacy Hotspot or HS 2.0 Wi-Fi network. with optional roaming enabled.
### Accessing Hotspot 2.0 properties
- [var domainName: String](nehotspoths20settings/domainname.md)
  The domain name of a Hotspot 2.0 Wi-Fi Network.
- [var isRoamingEnabled: Bool](nehotspoths20settings/isroamingenabled.md)
  A Boolean value indicating whether or not roaming is enabled on a Hotspot 2.0 Wi-Fi network.
- [var mccAndMNCs: [String]](nehotspoths20settings/mccandmncs.md)
  An array of Mobile Country Code (MCC) and Mobile Network Code  (MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation.
- [var naiRealmNames: [String]](nehotspoths20settings/nairealmnames.md)
  An array of Network Access Identifier (NAI) realm name strings used for Wi-Fi Hotspot 2.0 negotiation.
- [var roamingConsortiumOIs: [String]](nehotspoths20settings/roamingconsortiumois.md)
  An array of Roaming Consortium Organization (RCO) identifiers used for Wi-Fi Hotspot 2.0 negotiation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEHotspotConfigurationManager](nehotspotconfigurationmanager.md)
  A manager that applies and removes hotspot configurations of Wi-Fi networks.
- [class NEHotspotConfiguration](nehotspotconfiguration.md)
  Configuration settings for a Wi-Fi network.
- [class NEHotspotEAPSettings](nehotspoteapsettings.md)
  Extensible Authentication Protocol settings for configuring WPA and WPA2 enterprise Wi-Fi networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoths20settings)*
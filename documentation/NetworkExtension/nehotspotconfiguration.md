# NEHotspotConfiguration

**Framework**: Network Extension  
**Kind**: class

Configuration settings for a Wi-Fi network.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class NEHotspotConfiguration
```

#### Overview

The `NEHotspotConfiguration` class contains configuration properties and credentials required to connect to Wi-Fi networks.

## Topics

### Initializing a configuration
- [init(ssid: String)](nehotspotconfiguration/init(ssid:).md)
  Creates a new hotspot configuration, identified by an SSID, for an open Wi-Fi network.
- [init(ssid: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssid:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID, for a protected WEP or WPA/WPA2 personal Wi-Fi network.
- [init(ssid: String, eapSettings: NEHotspotEAPSettings)](nehotspotconfiguration/init(ssid:eapsettings:).md)
  Creates a new hotspot configuration, identified by an SSID, for a WPA/WPA2 enterprise Wi-Fi network with EAP settings.
- [init(hs20Settings: NEHotspotHS20Settings, eapSettings: NEHotspotEAPSettings)](nehotspotconfiguration/init(hs20settings:eapsettings:).md)
  Creates a new hotspot configuration, identified by a domain name, for a Hotspot 2.0 Wi-Fi network with HS 2.0 and EAP settings.
- [init(ssidPrefix: String)](nehotspotconfiguration/init(ssidprefix:).md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for an open Wi-Fi network.
- [init(ssidPrefix: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssidprefix:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for a protected WEP or WPA/WPA2 personal Wi-Fi network.
### Accessing configuration properties
- [var ssid: String](nehotspotconfiguration/ssid.md)
  The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.
- [var ssidPrefix: String](nehotspotconfiguration/ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var lifeTimeInDays: NSNumber](nehotspotconfiguration/lifetimeindays.md)
  The number of days the network retains the associated configuration.
- [var joinOnce: Bool](nehotspotconfiguration/joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](nehotspotconfiguration/hidden.md)
  A Boolean value that indicates the visibility of the SSID.

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
- [class NEHotspotEAPSettings](nehotspoteapsettings.md)
  Extensible Authentication Protocol settings for configuring WPA and WPA2 enterprise Wi-Fi networks.
- [class NEHotspotHS20Settings](nehotspoths20settings.md)
  Settings for configuring Hotspot 2.0 Wi-Fi networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration)*
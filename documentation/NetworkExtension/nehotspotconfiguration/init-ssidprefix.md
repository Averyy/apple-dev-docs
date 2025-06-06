# init(ssidPrefix:)

**Framework**: Network Extension  
**Kind**: init

Creates a new hotspot configuration, identified by an SSID prefix string, for an open Wi-Fi network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(ssidPrefix SSIDPrefix: String)
```

#### Discussion

Use this initializer when you want to match a known SSID prefix, but don’t have a full SSID. If the system finds multiple Wi-Fi networks whose SSID string matches the given prefix, it selects the network with the greatest signal strength.

## Parameters

- `SSIDPrefix`: A prefix string to match the SSID of an open Wi-Fi Network. This value must be between 3 and 32 characters.

## See Also

- [init(ssid: String)](nehotspotconfiguration/init(ssid:).md)
  Creates a new hotspot configuration, identified by an SSID, for an open Wi-Fi network.
- [init(ssid: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssid:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID, for a protected WEP or WPA/WPA2 personal Wi-Fi network.
- [init(ssid: String, eapSettings: NEHotspotEAPSettings)](nehotspotconfiguration/init(ssid:eapsettings:).md)
  Creates a new hotspot configuration, identified by an SSID, for a WPA/WPA2 enterprise Wi-Fi network with EAP settings.
- [init(hs20Settings: NEHotspotHS20Settings, eapSettings: NEHotspotEAPSettings)](nehotspotconfiguration/init(hs20settings:eapsettings:).md)
  Creates a new hotspot configuration, identified by a domain name, for a Hotspot 2.0 Wi-Fi network with HS 2.0 and EAP settings.
- [init(ssidPrefix: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssidprefix:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for a protected WEP or WPA/WPA2 personal Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/init(ssidprefix:))*
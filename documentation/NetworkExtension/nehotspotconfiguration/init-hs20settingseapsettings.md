# init(hs20Settings:eapSettings:)

**Framework**: Network Extension  
**Kind**: init

Creates a new hotspot configuration, identified by a domain name, for a Hotspot 2.0 Wi-Fi network with HS 2.0 and EAP settings.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(hs20Settings: NEHotspotHS20Settings, eapSettings: NEHotspotEAPSettings)
```

## Parameters

- `hs20Settings`: Hotspot 2.0 settings. For possible values, see  .
- `eapSettings`: EAP settings. For possible values, see 

## See Also

- [init(ssid: String)](nehotspotconfiguration/init(ssid:).md)
  Creates a new hotspot configuration, identified by an SSID, for an open Wi-Fi network.
- [init(ssid: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssid:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID, for a protected WEP or WPA/WPA2 personal Wi-Fi network.
- [init(ssid: String, eapSettings: NEHotspotEAPSettings)](nehotspotconfiguration/init(ssid:eapsettings:).md)
  Creates a new hotspot configuration, identified by an SSID, for a WPA/WPA2 enterprise Wi-Fi network with EAP settings.
- [init(ssidPrefix: String)](nehotspotconfiguration/init(ssidprefix:).md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for an open Wi-Fi network.
- [init(ssidPrefix: String, passphrase: String, isWEP: Bool)](nehotspotconfiguration/init(ssidprefix:passphrase:iswep:).md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for a protected WEP or WPA/WPA2 personal Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/init(hs20settings:eapsettings:))*
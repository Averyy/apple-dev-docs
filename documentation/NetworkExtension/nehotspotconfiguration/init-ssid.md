# init(ssid:)

**Framework**: Network Extension  
**Kind**: init

Creates a new hotspot configuration, identified by an SSID, for an open Wi-Fi network.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(ssid SSID: String)
```

## Parameters

- `SSID`: The SSID of the open Wi-Fi network. See  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/init(ssid:))*
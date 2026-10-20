# init(ssid:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSSID:(NSString *) SSID;
```

## Parameters

- `SSID`: The SSID of the open Wi-Fi network. See [`ssid`](./ssid.md).

## See Also

### Initializing a configuration
- [init(ssid: String, passphrase: String, isWEP: Bool)](./init%28ssid,passphrase,iswep%29-3ll1v.md)
  Creates a new hotspot configuration, identified by an SSID, for a protected WEP or WPA/WPA2 personal Wi-Fi network.
- [init(ssid: String, eapSettings: NEHotspotEAPSettings)](./init%28ssid,eapsettings%29-53cpf.md)
  Creates a new hotspot configuration, identified by an SSID, for a WPA/WPA2 enterprise Wi-Fi network with EAP settings.
- [init(hs20Settings: NEHotspotHS20Settings, eapSettings: NEHotspotEAPSettings)](./init%28hs20settings,eapsettings%29-291m2.md)
  Creates a new hotspot configuration, identified by a domain name, for a Hotspot 2.0 Wi-Fi network with HS 2.0 and EAP settings.
- [init(ssidPrefix: String)](./init%28ssidprefix%29-1v8bx.md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for an open Wi-Fi network.
- [init(ssidPrefix: String, passphrase: String, isWEP: Bool)](./init%28ssidprefix,passphrase,iswep%29-7ttmu.md)
  Creates a new hotspot configuration, identified by an SSID prefix string, for a protected WEP or WPA/WPA2 personal Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/init(ssid:)-9apfi)*
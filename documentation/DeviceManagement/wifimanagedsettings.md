# WiFiManagedSettings

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure managed Wi-Fi settings.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object WiFiManagedSettings
```

#### Discussion

Specify `com.apple.MCX` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>RequireAdminForAirPortNetworkChange</key>
            <true/>
            <key>RequireAdminForIBSS</key>
            <true/>
            <key>RequireAdminToTurnAirPortOnOff</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mymanagedwifipayload</string>
            <key>PayloadType</key>
            <string>com.apple.MCX</string>
            <key>PayloadUUID</key>
            <string>8d527efa-0768-49e4-b328-9b222d23c379</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Managed Wi-Fi</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>944429fb-2a8d-4d48-81ab-056428104593</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object Cellular](cellular.md)
  The payload you use to configure cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload to provide device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload you use to configure the content-caching service.
- [object DNSSettings](dnssettings.md)
  The payload you use to configure encrypted DNS settings.
- [object Domains](domains.md)
  The payload you use to configure the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload you use to configure the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload you use to configure network-usage rules.
- [object Relay](relay.md)
  The payload you use to configure relay settings.
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifimanagedsettings)*
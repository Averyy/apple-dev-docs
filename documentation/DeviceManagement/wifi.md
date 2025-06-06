# WiFi

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Wi-Fi settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WiFi
```

#### Discussion

Specify `com.apple.wifi.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Allow Manual Install | iOS, macOS, tvOS, watchOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS, macOS |
| Allow Multiple Payloads | iOS, macOS, Shared iPad, tvOS, watchOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>New item</key>
    <dict>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>AutoJoin</key>
                <true/>
                <key>CaptiveBypass</key>
                <false/>
                <key>DisableAssociationMACRandomization</key>
                <false/>
                <key>EncryptionType</key>
                <string>WPA</string>
                <key>HIDDEN_NETWORK</key>
                <true/>
                <key>IsHotspot</key>
                <false/>
                <key>Password</key>
                <string>Password123</string>
                <key>PayloadDisplayName</key>
                <string>Wi-Fi</string>
                <key>ProxyType</key>
                <string>None</string>
                <key>SSID_STR</key>
                <string>Example</string>
                <key>PayloadIdentifier</key>
                <string>com.example.mywifipayload</string>
                <key>PayloadType</key>
                <string>com.apple.wifi.managed</string>
                <key>PayloadUUID</key>
                <string>94c487e0-d6f8-41e3-b66d-a89994e6919b</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
            </dict>
        </array>
        <key>PayloadDisplayName</key>
        <string>Wi-Fi</string>
        <key>PayloadIdentifier</key>
        <string>com.example.myprofile</string>
        <key>PayloadType</key>
        <string>Configuration</string>
        <key>PayloadUUID</key>
        <string>71e9b0f7-02f8-4aea-b365-b381d872909a</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
    </dict>
</dict>
</plist>
```

## Topics

### Objects
- [object WiFi.EAPClientConfiguration](wifi/eapclientconfiguration-data.dictionary.md)
  A dictionary that configures an enterprise network.
- [object WiFi.QoSMarkingPolicy](wifi/qosmarkingpolicy-data.dictionary.md)
  A dictionary that defines the quality-of-service settings.

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
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi)*
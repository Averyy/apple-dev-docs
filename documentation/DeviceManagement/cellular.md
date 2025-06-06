# Cellular

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure cellular settings.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- watchOS 3.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Cellular
```

#### Discussion

Specify `com.apple.cellular` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, watchOS |
| User Channel | - |
| Allow Manual Install | iOS, watchOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AttachAPN</key>
            <dict>
                <key>Name</key>
                <string>example.com</string>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mycellularnetworkpayload</string>
            <key>PayloadType</key>
            <string>com.apple.cellular</string>
            <key>PayloadUUID</key>
            <string>5a024a67-119f-4b38-8648-4c28a054ec5f</string>
            <key>PayloadVersion</key>
            <real>1</real>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Cellular</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>07eeff13-902a-408b-9bec-2228b86f944f</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Cellular.APNsItem](cellular/apnsitem.md)
  A dictionary that contains details about an access point name (APN) configuration.
- [object Cellular.AttachAPN](cellular/attachapn-data.dictionary.md)
  A dictionary that contains details about an attach access point name (APN) configuration.

## See Also

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
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellular)*
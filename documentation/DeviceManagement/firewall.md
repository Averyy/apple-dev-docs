# Firewall

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the firewall.

**Availability**:
- macOS 10.12+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Firewall
```

#### Discussion

Specify `com.apple.security.firewall` as the payload type.

The payload needs to exist in a system-scoped profile.

If more than one profile contains this payload, the system uses the most restrictive union of settings.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | macOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EnableFirewall</key>
            <true/>
            <key>Applications</key>
            <array>
                <dict>
                    <key>BundleID</key>
                    <string>com.example.myapp</string>
                    <key>Allowed</key>
                    <false/>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myfirewallpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.firewall</string>
            <key>PayloadUUID</key>
            <string>28b1fef7-ddb6-4d56-9a6a-6bb4e56e7f0b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Firewall</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>8f2fa915-f2da-4034-9424-2218355a6f3c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Firewall.ApplicationsItem](firewall/applicationsitem.md)
  A dictionary of details for apps.

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
- [object NetworkUsageRules](networkusagerules.md)
  The payload you use to configure network-usage rules.
- [object Relay](relay.md)
  The payload you use to configure relay settings.
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/firewall)*
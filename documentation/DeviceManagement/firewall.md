# Firewall

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the firewall.

**Availability**:
- macOS 10.12+

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
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload that configures the Content Caching service.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/firewall)*
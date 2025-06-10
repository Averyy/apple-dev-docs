# NetworkUsageRules

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure network-usage rules.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Declaration

```swift
object NetworkUsageRules
```

#### Discussion

Specify `com.apple.networkusagerules` as the payload type.

Network usage rules allow enterprises to specify how devices use networks, such as cellular data networks. iOS 9-12 require the application rules. In iOS 13, application rules, SIM rules, or both must be present.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Allow manual install | NA |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>ApplicationRules</key>
            <array>
                <dict>
                    <key>AllowCellularData</key>
                    <false/>
                    <key>AllowRoamingCellularData</key>
                    <false/>
                    <key>AppIdentifierMatches</key>
                    <array>
                        <string>com.apple.appname</string>
                    </array>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mynetworkusagepayload</string>
            <key>PayloadType</key>
            <string>com.apple.networkusagerules</string>
            <key>PayloadUUID</key>
            <string>'ef0250de-bfd4-4095-9ad3-34cf1281d5da</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Network Usage</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b724f950-5853-4b78-8f4a-9a37a0ccac1f</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object NetworkUsageRules.ApplicationRulesItem](networkusagerules/applicationrulesitem.md)
  The application rules dictionary.
- [object NetworkUsageRules.SIMRulesItem](networkusagerules/simrulesitem.md)
  The policy for individual SIM cards.

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
- [object Relay](relay.md)
  The payload you use to configure relay settings.
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkusagerules)*
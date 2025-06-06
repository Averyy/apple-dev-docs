# Domains

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the domains under an organization’s management.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Domains
```

#### Discussion

Specify `com.apple.domains` as the payload type.

A URL that begins with the prefix `www.` is treated as though it doesn’t contain that prefix during matching. For example, `http://www.apple.com/store` is matched as `http://apple.com/store`.

Trailing slashes are ignored.

If a domain string entry contains a port number, the system considers only addresses that specify that port number managed. Otherwise, the system matches the domain without regard to the port number specified. For example, the pattern `*.apple.com:8080` matches `http://site.apple.com:8080/page.html` but not `http://site.apple.com/page.html`, while the pattern `*.apple.com` matches both URLs.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad |
| User Channel | macOS, Shared iPad |
| Allow Manual Install | iOS, macOS |
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
            <key>EmailDomains</key>
            <array>
                <string>example.com</string>
            </array>
            <key>SafariPasswordAutoFillDomains</key>
            <array>
                <string>example.com</string>
            </array>
            <key>WebDomains</key>
            <array>
                <string>example.com</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mysafaridomainspayload</string>
            <key>PayloadType</key>
            <string>com.apple.domains</string>
            <key>PayloadUUID</key>
            <string>0f94e664-4c36-4637-b264-19a533adc8e1</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Domains</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>0cf6d95f-8e9f-49f3-9cba-c5e78de5430e</string>
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/domains)*
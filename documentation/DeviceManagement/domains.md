# Domains

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the domains under an organization’s management.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- visionOS 2.0+

## Declaration

```swift
object Domains
```

#### Discussion

Specify `com.apple.domains` as the payload type.

The `WebDomains`, `SafariPasswordAutoFillDomains`, and `CrossSiteTrackingPreventionRelaxedDomains` keys are arrays containing strings that use the following matching patterns:

- `example.com`: Any path under `example.com` matches, but not `site.example.com`.
- `foo.example.com`: Any path under `foo.example.com` matches, but not `example.com` or `bar.example.com`.
- `\*.example.com`: Any path under `foo.example.com` or `bar.example.com` matches, but not `example.com`.
- `example.com/sub`: `example.com/sub` and any path under it matches, but not `example.com`.
- `foo.example.com/sub`: Any path under `foo.example.com/sub` matches, but not `example.com`, `example.com/sub`, `foo.example.com/`, or `bar.example.com/sub`.
- `\*.example.com/sub`: Any path under `foo.example.com/sub` or `bar.example.com/sub` matches, but not `example.com` or `foo.example.com/`.
- `\*.co`: Any path under `example.co` or `betterbag.co` matches, but not `example.co.uk` or `example.com`.

A URL that begins with the prefix `www.` is treated as though it doesn’t contain that prefix during matching. For example, `http://www.example.com/store` is matched as `http://example.com/store`.

Trailing slashes are ignored.

If a domain string contains a port number, the system considers only addresses that specify that port number managed. Otherwise, the system matches the domain without regard to the port number specified. For example, the pattern `*.example.com:8080` matches `http://site.example.com:8080/page.html` but not `http://site.example.com/page.html`, while the pattern `*.example.com` matches both URLs.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, visionOS |
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
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload that configures the Content Caching service.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/domains)*
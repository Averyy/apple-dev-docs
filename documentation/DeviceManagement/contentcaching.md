# ContentCaching

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the content-caching service.

**Availability**:
- macOS 10.13.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ContentCaching
```

#### Discussion

Specify `com.apple.AssetCache.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowPersonalCaching</key>
            <false/>
            <key>AllowSharedCaching</key>
            <true/>
            <key>AutoActivation</key>
            <true/>
            <key>CacheLimit</key>
            <integer>180000000000</integer>
            <key>DenyTetheredCaching</key>
            <false/>
            <key>ListenRangesOnly</key>
            <false/>
            <key>LocalSubnetsOnly</key>
            <true/>
            <key>LogClientIdentity</key>
            <false/>
            <key>ParentSelectionPolicy</key>
            <string>round-robin</string>
            <key>PeerLocalSubnetsOnly</key>
            <true/>
            <key>Port</key>
            <integer>0</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.mycontentcachingpayload</string>
            <key>PayloadType</key>
            <string>com.apple.AssetCache.managed</string>
            <key>PayloadUUID</key>
            <string>c7d8c850-e4ef-0135-0bd6-0c4de9ce4c04</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Content Caching</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>a430c370-b5d5-4e5b-b46b-137931e8b230</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ContentCaching.Ranges](contentcaching/ranges.md)
  A range of IP addresses to cache.

## See Also

- [object Cellular](cellular.md)
  The payload you use to configure cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload to provide device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcaching)*
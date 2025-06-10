# Relay

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure relay settings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
object Relay
```

#### Discussion

Specify `com.apple.relay.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS |

## Topics

### Objects
- [object Relay.Relay](relay/relay.md)
  A dictionary that describes a relay server.

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
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/relay)*
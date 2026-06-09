# DNSSettings

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures encrypted DNS settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
object DNSSettings
```

#### Discussion

Specify `com.apple.dnsSettings.managed` as the payload type.

When installed from an MDM, the setting only applies to managed Wi-Fi networks.

When installed manually, this setting also applies to cellular networks.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | N/A |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

## Topics

### Objects
- [object DNSSettings.DNSSettings](dnssettings/dnssettings-data.dictionary.md)
  A dictionary that defines a configuration for an encrypted DNS server.
- [object DNSSettings.OnDemandRulesElement](dnssettings/ondemandruleselement.md)
  A list of domain strings that determine which DNS queries use the DNS server.

## Properties

- `DNSSettings` (DNSSettings.DNSSettings) *(required)*: A dictionary that defines a configuration for an encrypted DNS server.
- `OnDemandRules` ([DNSSettings.OnDemandRulesElement]): An array of rules that define the DNS settings. If not set, the system always applies the DNS settings. These rules are identical to the `OnDemandRules` array in VPN payloads.
- `ProhibitDisablement` (boolean): If `true`, the system prohibits users from disabling DNS settings. This key is only available on supervised devices.

## See Also

- [object Cellular](cellular.md)
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCachingService](contentcachingservice.md)
  The payload that configures the Content Caching service.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnssettings)*
# Relay

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures relay settings.

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

## Properties

- `AllowDNSFailover` (boolean): If `true`, the device allows the relay to failover to the default system DNS resolver.
- `ExcludedDomains` ([string]): A list of domain strings to exclude from routing through the servers in `Relays`. Any connection that matches a domain in the list exactly or is a subdomain of the listed domain won’t use the relay server.
- `ExcludedFQDNs` ([string]): A list of Fully Qualified Domain Names (FQDNs) to exclude from routing through the servers contained in `Relays`. Any connection that matches an FQDN in the list exactly won’t use the relay server. When `MatchDomains` is also present, any FQDN listed in the list should be a subdomain of at least one `MatchDomain` value, otherwise it will not have any effect.
- `MatchDomains` ([string]): A list of domain strings that the system uses to determine which connection to route through the servers in `Relays`. Any connection that matches a domain in the list exactly or is a subdomain of the listed domain uses the relay servers, unless it matches a domain in `ExcludedDomains`. If this list and `MatchFQDNs` are empty, the system routes traffic to all domains to the relay servers, except those that match an excluded domain or excluded FQDN.
- `MatchFQDNs` ([string]): A list of Fully Qualified Domain Names (FQDNs) to be routed through the servers contained in `Relays`. Any connection that matches an FQDN in the list exactly uses the relay servers. If this list and `MatchDomains` are empty, the system routes traffic to all domains to the relay servers, except those that match an excluded domain or excluded FQDN.
- `Relays` ([Relay.Relay]) *(required)*: An array of dictionaries that describe one or more relay servers that the system can chain together.
- `RelayUUID` (string): A globally unique identifier for this relay configuration. The system uses this UUID to route managed apps through the servers in `Relays`. This key is required for user enrollment.
- `UIToggleEnabled` (boolean): If `true`, the device allows the user to disable this network relay configuration.

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
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/relay)*
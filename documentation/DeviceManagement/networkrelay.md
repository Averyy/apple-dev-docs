# NetworkRelay

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Network Relay settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkRelay
```

#### Discussion

Specify `com.apple.configuration.network.relay` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, visionOS |
| Allowed in user scope | Shared iPad |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**Single relay**:

This configuration routes traffic to two domains through a single HTTP/2 relay with a custom authorization header.

```json
{
    "Type": "com.apple.configuration.network.relay",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Corporate Relay",
        "Relays": [
            {
                "HTTP2RelayURL": "https://relay.example.com/proxy",
                "AdditionalHTTPHeaderFields": {
                    "Authorization": "Bearer enterprise-token-12345"
                }
            }
        ],
        "MatchDomains": ["example.com", "internal.example.com"],
        "RelayUUID": "C3D4E5F6-A7B8-9012-CDEF-123456789012",
        "UIToggleEnabled": false
    }
}
```

**Chained relays**:

This configuration routes specific hostnames through two chained relay hops supporting both HTTP/2 and HTTP/3.

```json
{
    "Type": "com.apple.configuration.network.relay",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "VisibleName": "Two-Hop Privacy Relay",
        "Relays": [
            {
                "HTTP3RelayURL": "https://relay1.example.com/hop1",
                "HTTP2RelayURL": "https://relay1.example.com/hop1"
            },
            {
                "HTTP3RelayURL": "https://relay2.example.com/hop2"
            }
        ],
        "MatchFQDNs": ["secure.example.com", "api.example.com"],
        "ExcludedDomains": ["cdn.example.com"],
        "RelayUUID": "D4E5F6A7-B8C9-0123-DEF0-234567890123",
        "AllowDNSFailover": true
    }
}
```

## Topics

### Objects
- [object NetworkRelayRelayObject](networkrelayrelayobject.md)
  An array of dictionaries that describe one or more relay servers that the system can chain together.

## Properties

- `AllowDNSFailover` (boolean): If `true`, the device allows the relay to failover to the default system DNS resolver.
- `ExcludedDomains` ([string]): A list of domain strings to exclude from routing through the servers in `Relays`. Any connection that matches a domain in the list exactly or is a subdomain of the listed domain won’t use the relay server.
- `ExcludedFQDNs` ([string]): A list of Fully Qualified Domain Names (FQDNs) to exclude from routing through the servers contained in `Relays`. Any connection that matches an FQDN in the list exactly won’t use the relay server. When `MatchDomains` is also present, any FQDN listed in the list should be a subdomain of at least one `MatchDomain` value, otherwise it won’t have any effect.
- `MatchDomains` ([string]): A list of domain strings that the system uses to determine which connection to route through the servers in `Relays`. Any connection that matches a domain in the list exactly or is a subdomain of the listed domain uses the relay servers, unless it matches a domain in `ExcludedDomains`. If this list and `MatchFQDNs` are empty, the system routes traffic to all domains to the relay servers, except those that match an excluded domain or excluded FQDN.
- `MatchFQDNs` ([string]): A list of Fully Qualified Domain Names (FQDNs) to route through the servers contained in `Relays`. Any connection that matches an FQDN in the list exactly uses the relay servers. If this list and `MatchDomains` are empty, the system routes traffic to all domains to the relay servers, except those that match an excluded domain or excluded FQDN.
- `Relays` ([NetworkRelayRelayObject]) *(required)*: An array of dictionaries that describe one or more relay servers that the system can chain together.
- `RelayUUID` (string): A globally unique identifier for this relay configuration. The system uses this UUID to route managed apps through the servers in `Relays`. This key is required for user enrollment. Available: iOS 27+ | iPadOS 27+ | visionOS 27+
- `UIToggleEnabled` (boolean): If `true`, the device allows the user to disable this network relay configuration.
- `VisibleName` (string) *(required)*: The name of the network relays that the system displays on the device.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkrelay)*
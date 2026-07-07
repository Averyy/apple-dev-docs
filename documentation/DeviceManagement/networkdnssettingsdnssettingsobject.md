# NetworkDNSSettingsDNSSettingsObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that defines a configuration for an encrypted DNS server.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkDNSSettingsDNSSettingsObject
```

## Properties

- `AllowFailover` (boolean): If `true`, the device allows failover to the default system DNS resolver.
- `DNSProtocol` (string) *(required)*: The encrypted transport protocol used to communicate with the DNS server.
- `IdentityAssetReference` (string): Specifies the identifier of an asset declaration containing an identity that the system uses to authenticate the user to the DNS resolver.
- `ServerAddresses` ([string]): An unordered list of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.
- `ServerName` (string): The hostname of a DNS-over-TLS server used to validate the server certificate, as defined in RFC 7858. If no `ServerAddresses` are provided, the system uses the hostname to determine the server addresses. This key must be present only if the DNSProtocol is `TLS`.
- `ServerURL` (string): The URI template of a DNS-over-HTTPS server, as defined in RFC 8484. This URL needs to use the `https://` scheme, and the system uses the hostname or address in the URL to validate the server certificate. If no `ServerAddresses` are provided, the system uses the hostname or address in the URL to determine the server addresses. Required if `DNSProtocol` is `HTTPS`.
- `SupplementalMatchDomains` ([string]): A list of domain strings used to determine which DNS queries use the DNS server. If not set, all domains use the DNS server. The system supports a single wildcard (`\*`) prefix, but it’s not required. For example, both `\*.example.com` and `example.com` match against `mydomain.example.com` and `your.domain.example.com`, but don’t match against `mydomain-example.com`.

## See Also

- [object NetworkDNSSettingsOnDemandRulesElementObject](networkdnssettingsondemandruleselementobject.md)
  An array of rules that define the DNS settings. If not set, the system always applies the DNS settings. These rules are identical to the `OnDemandRules` array in VPN payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkdnssettingsdnssettingsobject)*
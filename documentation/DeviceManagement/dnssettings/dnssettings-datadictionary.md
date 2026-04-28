# DNSSettings.DNSSettings

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that defines a configuration for an encrypted DNS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DNSSettings.DNSSettings
```

## Properties

- `AllowFailover` (boolean): If `true`, the device allows failover to the default system DNS resolver.
- `DNSProtocol` (string) *(required)*: The encrypted transport protocol used to communicate with the DNS server.
- `PayloadCertificateUUID` (string): The UUID that points to an identity certificate payload. The system uses this identity to authenticate the user to the DNS resolver.
- `ServerAddresses` ([string]): An unordered list of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.
- `ServerName` (string): The hostname of a DNS-over-TLS server used to validate the server certificate, as defined in RFC 7858. If no `ServerAddresses` are provided, the system uses the hostname to determine the server addresses. This key must be present only if the DNSProtocol is `TLS`.
- `ServerURL` (string): The URI template of a DNS-over-HTTPS server, as defined in RFC 8484. This URL needs to use the `https://` scheme, and the system uses the hostname or address in the URL to validate the server certificate. If no `ServerAddresses` are provided, the system uses the hostname or address in the URL to determine the server addresses. Required if `DNSProtocol` is `HTTPS`.
- `SupplementalMatchDomains` ([string]): A list of domain strings used to determine which DNS queries use the DNS server. If not set, all domains use the DNS server. The system supports a single wildcard (`*`) prefix, but it’s not required. For example, both `*.example.com` and `example.com` match against `mydomain.example.com` and `your.domain.example.com`, but don’t match against `mydomain-example.com`.

## See Also

- [object DNSSettings.OnDemandRulesElement](dnssettings/ondemandruleselement.md)
  A list of domain strings that determine which DNS queries use the DNS server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnssettings/dnssettings-data.dictionary)*
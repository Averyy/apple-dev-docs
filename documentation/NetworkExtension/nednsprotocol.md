# NEDNSProtocol

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEDNSProtocol
```

## Topics

### DNS protocols
- [NEDNSProtocol.cleartext](nednsprotocol/cleartext.md)
  The DNS server uses cleartext UDP or TCP over port 53.
- [NEDNSProtocol.TLS](nednsprotocol/tls.md)
  The DNS server uses DNS-over-TLS.
- [NEDNSProtocol.HTTPS](nednsprotocol/https.md)
  The DNS server uses DNS-over-HTTPS.
### Initializers
- [init?(rawValue: Int)](nednsprotocol/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var servers: [String]](nednssettings/servers.md)
  The DNS server IP addresses.
- [var searchDomains: [String]?](nednssettings/searchdomains.md)
  A list of domain strings used to fully qualify single-label host names.
- [var domainName: String?](nednssettings/domainname.md)
  The primary domain of the tunnel.
- [var matchDomains: [String]?](nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
- [var matchDomainsNoSearch: Bool](nednssettings/matchdomainsnosearch.md)
  A Boolean that specifies if the domains in the `matchDomains` list should not be appended to the resolver’s list of search domains.
- [var dnsProtocol: NEDNSProtocol](nednssettings/dnsprotocol.md)
  The DNS protocol used by the server, such as HTTPS or TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsprotocol)*
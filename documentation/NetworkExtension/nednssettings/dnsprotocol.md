# dnsProtocol

**Framework**: Network Extension  
**Kind**: property

The DNS protocol used by the server, such as HTTPS or TLS.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var dnsProtocol: NEDNSProtocol { get }
```

#### Discussion

By default, an [`NEDNSSettings`](nednssettings.md) object will use [`NEDNSProtocol.cleartext`](nednsprotocol/cleartext.md). In order to use encryption, create an [`NEDNSOverHTTPSSettings`](nednsoverhttpssettings.md) or [`NEDNSOverTLSSettings`](nednsovertlssettings.md) object.

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
- [enum NEDNSProtocol](nednsprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings/dnsprotocol)*
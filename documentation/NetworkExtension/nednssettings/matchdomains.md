# matchDomains

**Framework**: Network Extension  
**Kind**: property

A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var matchDomains: [String]? { get set }
```

#### Discussion

This property is used to create a “split DNS” configuration, where only hosts in certain domains are resolved using the tunnel’s DNS resolver settings. Hosts not in one of the domains in this list are resolved using the system’s default resolver.

If `matchDomains` contains the empty string it becomes the default domain. This is how a split-tunnel configuration can direct all DNS queries first to the VPN DNS servers before the primary DNS servers.

If the VPN tunnel becomes the network’s default route, the servers listed earlier by `NEDNSSettings` become the default resolver and the `matchDomains` list is ignored.

## See Also

- [var servers: [String]](nednssettings/servers.md)
  The DNS server IP addresses.
- [var searchDomains: [String]?](nednssettings/searchdomains.md)
  A list of domain strings used to fully qualify single-label host names.
- [var domainName: String?](nednssettings/domainname.md)
  The primary domain of the tunnel.
- [var matchDomainsNoSearch: Bool](nednssettings/matchdomainsnosearch.md)
  A Boolean that specifies if the domains in the `matchDomains` list should not be appended to the resolver’s list of search domains.
- [var dnsProtocol: NEDNSProtocol](nednssettings/dnsprotocol.md)
  The DNS protocol used by the server, such as HTTPS or TLS.
- [enum NEDNSProtocol](nednsprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings/matchdomains)*
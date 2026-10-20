# matchDomainsNoSearch

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean that specifies if the domains in the `matchDomains` list should not be appended to the resolver’s list of search domains.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var matchDomainsNoSearch: Bool { get set }
```

```objc
@property BOOL matchDomainsNoSearch;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Accessing DNS properties
- [var servers: [String]](./servers.md)
  The DNS server IP addresses.
- [var searchDomains: [String]?](./searchdomains.md)
  A list of domain strings used to fully qualify single-label host names.
- [var domainName: String?](./domainname.md)
  The primary domain of the tunnel.
- [var matchDomains: [String]?](./matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
- [var dnsProtocol: NEDNSProtocol](./dnsprotocol.md)
  The DNS protocol used by the server, such as HTTPS or TLS.
- [enum NEDNSProtocol](../nednsprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings/matchdomainsnosearch)*
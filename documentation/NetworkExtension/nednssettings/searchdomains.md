# searchDomains

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A list of domain strings used to fully qualify single-label host names.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var searchDomains: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * searchDomains;
```

## See Also

### Accessing DNS properties
- [var servers: [String]](./servers.md)
  The DNS server IP addresses.
- [var domainName: String?](./domainname.md)
  The primary domain of the tunnel.
- [var matchDomains: [String]?](./matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
- [var matchDomainsNoSearch: Bool](./matchdomainsnosearch.md)
  A Boolean that specifies if the domains in the `matchDomains` list should not be appended to the resolver’s list of search domains.
- [var dnsProtocol: NEDNSProtocol](./dnsprotocol.md)
  The DNS protocol used by the server, such as HTTPS or TLS.
- [enum NEDNSProtocol](../nednsprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings/searchdomains)*
# NEDNSSettings

**Framework**: Network Extension  
**Kind**: class

The DNS resolver settings of a network tunnel or a system-wide configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEDNSSettings
```

## Topics

### Initializing DNS settings
- [init(servers: [String])](nednssettings/init(servers:).md)
  Initialize the `NEDNSSetting` object.
### Accessing DNS properties
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
- [enum NEDNSProtocol](nednsprotocol.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NEDNSOverHTTPSSettings](nednsoverhttpssettings.md)
- [NEDNSOverTLSSettings](nednsovertlssettings.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEDNSOverHTTPSSettings](nednsoverhttpssettings.md)
  The DNS resolver settings for a DNS-over-HTTPS server.
- [class NEDNSOverTLSSettings](nednsovertlssettings.md)
  The DNS resolver settings for a DNS-over-TLS server.
- [class NEDNSProxyProvider](nednsproxyprovider.md)
  The principal class for a DNS proxy provider app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings)*
# NEDNSSettings

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEDNSSettings : NSObject
```

## Topics

### Initializing DNS settings
- [init(servers: [String])](./nednssettings/init%28servers%29.md)
  Initialize the `NEDNSSetting` object.
### Accessing DNS properties
- [var servers: [String]](./nednssettings/servers.md)
  The DNS server IP addresses.
- [var searchDomains: [String]?](./nednssettings/searchdomains.md)
  A list of domain strings used to fully qualify single-label host names.
- [var domainName: String?](./nednssettings/domainname.md)
  The primary domain of the tunnel.
- [var matchDomains: [String]?](./nednssettings/matchdomains.md)
  A list of domain strings used to determine which DNS queries will use the DNS resolver settings contained in this object.
- [var matchDomainsNoSearch: Bool](./nednssettings/matchdomainsnosearch.md)
  A Boolean that specifies if the domains in the `matchDomains` list should not be appended to the resolver’s list of search domains.
- [var dnsProtocol: NEDNSProtocol](./nednssettings/dnsprotocol.md)
  The DNS protocol used by the server, such as HTTPS or TLS.
- [enum NEDNSProtocol](./nednsprotocol.md)
### Instance Properties
- [var allowFailover: Bool](./nednssettings/allowfailover.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NEDNSOverHTTPSSettings](./nednsoverhttpssettings.md)
- [NEDNSOverTLSSettings](./nednsovertlssettings.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Related Documentation
- [class NEDNSOverHTTPSSettings](./nednsoverhttpssettings.md)
  The DNS resolver settings for a DNS-over-HTTPS server.
- [class NEDNSOverTLSSettings](./nednsovertlssettings.md)
  The DNS resolver settings for a DNS-over-TLS server.
### Provider
- [class NEDNSProxyProvider](./nednsproxyprovider.md)
  The principal class for a DNS proxy provider app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettings)*
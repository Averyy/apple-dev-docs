# probeURL

**Framework**: Network Extension  
**Kind**: property

A URL to probe when all other network identifiers match to validate that an expected resource is available.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var probeURL: URL? { get set }
```

#### Discussion

An HTTP or HTTPS URL. If a request sent to this URL results in a HTTP 200 OK response and all of the other conditions in the rule match, then then rule matches. If this property is nil (the default), then an HTTP request does not factor into the rule match.

## See Also

- [var dnsSearchDomainMatch: [String]?](neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var dnsServerAddressMatch: [String]?](neondemandrule/dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](neondemandrule/interfacetypematch.md)
  An interface type to identify a network.
- [enum NEOnDemandRuleInterfaceType](neondemandruleinterfacetype.md)
- [var ssidMatch: [String]?](neondemandrule/ssidmatch.md)
  SSIDs that identify a network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule/probeurl)*
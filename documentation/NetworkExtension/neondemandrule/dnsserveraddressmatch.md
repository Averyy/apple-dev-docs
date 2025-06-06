# dnsServerAddressMatch

**Framework**: Network Extension  
**Kind**: property

DNS server addresses that identify a network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var dnsServerAddressMatch: [String]? { get set }
```

#### Discussion

An array of DNS server IP addresses represented as `NSString` objects. If each of the current default DNS servers is equal to one of the strings in this array and all of the other conditions in the rule match, then the rule matches. If this property is nil (the default), then the default DNS servers do not factor into the rule match.

## See Also

- [var dnsSearchDomainMatch: [String]?](neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](neondemandrule/interfacetypematch.md)
  An interface type to identify a network.
- [enum NEOnDemandRuleInterfaceType](neondemandruleinterfacetype.md)
- [var ssidMatch: [String]?](neondemandrule/ssidmatch.md)
  SSIDs that identify a network.
- [var probeURL: URL?](neondemandrule/probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule/dnsserveraddressmatch)*
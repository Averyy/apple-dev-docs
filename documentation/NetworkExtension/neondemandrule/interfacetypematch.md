# interfaceTypeMatch

**Framework**: Network Extension  
**Kind**: property

An interface type to identify a network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var interfaceTypeMatch: NEOnDemandRuleInterfaceType { get set }
```

#### Discussion

The type of interface that this rule matches. If the current primary network interface is of this type and all of the other conditions in the rule match, then the rule matches. If this property is `NEOnDemandRuleInterfaceTypeAny` (the default), then the current primary interface type does not factor into the rule match.

## See Also

- [var dnsSearchDomainMatch: [String]?](neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var dnsServerAddressMatch: [String]?](neondemandrule/dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [enum NEOnDemandRuleInterfaceType](neondemandruleinterfacetype.md)
- [var ssidMatch: [String]?](neondemandrule/ssidmatch.md)
  SSIDs that identify a network.
- [var probeURL: URL?](neondemandrule/probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule/interfacetypematch)*
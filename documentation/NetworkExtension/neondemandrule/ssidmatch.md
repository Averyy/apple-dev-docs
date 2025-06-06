# ssidMatch

**Framework**: Network Extension  
**Kind**: property

SSIDs that identify a network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var ssidMatch: [String]? { get set }
```

#### Discussion

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. If the Service Set Identifier (SSID) of the current primary connected network matches one of the strings in this array and all of the other conditions in the rule match, then the rule matches. If this property is nil (the default), then the current primary connected network SSID does not factor into the rule match.

## See Also

- [var dnsSearchDomainMatch: [String]?](neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var dnsServerAddressMatch: [String]?](neondemandrule/dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](neondemandrule/interfacetypematch.md)
  An interface type to identify a network.
- [enum NEOnDemandRuleInterfaceType](neondemandruleinterfacetype.md)
- [var probeURL: URL?](neondemandrule/probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule/ssidmatch)*
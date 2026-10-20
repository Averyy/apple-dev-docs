# dnsSearchDomainMatch

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

DNS search domains that identify a network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var dnsSearchDomainMatch: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * DNSSearchDomainMatch;
```

#### Discussion

An array of [`NSString`](../../Foundation/nsstring.md) objects. If the current default search domain is equal to one of the strings in this array and all of the other conditions in the rule match, then the rule matches. If this property is nil (the default), then the current default search domain does not factor into the rule match.

## See Also

### Accessing match parameters
- [var dnsServerAddressMatch: [String]?](./dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](./interfacetypematch.md)
  An interface type to identify a network.
- [enum NEOnDemandRuleInterfaceType](../neondemandruleinterfacetype.md)
- [var ssidMatch: [String]?](./ssidmatch.md)
  SSIDs that identify a network.
- [var probeURL: URL?](./probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule/dnssearchdomainmatch)*
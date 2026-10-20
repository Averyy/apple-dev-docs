# NEOnDemandRuleInterfaceType

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEOnDemandRuleInterfaceType
```

```c
enum NEOnDemandRuleInterfaceType : NSInteger;
```

## Topics

### Interface Types
- [NEOnDemandRuleInterfaceType.any](./neondemandruleinterfacetype/any.md)
  Match any interface type
- [NEOnDemandRuleInterfaceType.ethernet](./neondemandruleinterfacetype/ethernet.md)
  Match wired ethernet interfaces
- [NEOnDemandRuleInterfaceType.wiFi](./neondemandruleinterfacetype/wifi.md)
  Match Wi-Fi interfaces
- [NEOnDemandRuleInterfaceType.cellular](./neondemandruleinterfacetype/cellular.md)
  Match cellular data interfaces
### Initializers
- [init?(rawValue: Int)](./neondemandruleinterfacetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing match parameters
- [var dnsSearchDomainMatch: [String]?](./neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var dnsServerAddressMatch: [String]?](./neondemandrule/dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](./neondemandrule/interfacetypematch.md)
  An interface type to identify a network.
- [var ssidMatch: [String]?](./neondemandrule/ssidmatch.md)
  SSIDs that identify a network.
- [var probeURL: URL?](./neondemandrule/probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleinterfacetype)*
# NEOnDemandRule

**Framework**: Network Extension  
**Kind**: class

A base class shared by all VPN On Demand rules.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEOnDemandRule
```

#### Overview

Each rule is defined by a single action and a set of optional matching conditions. The action defines how the system should trigger the VPN when the conditions are met, such as connecting automatically for all connections, connecting conditionally, or disconnecting. The optional conditions describe parameters of a network. Some common rules include disconnecting the VPN on a trusted, internal network, and triggering on all other networks. When rules are defined in an array, they are evaluated in order and the action of the first rule to match all conditions is chosen.

Instances of the `NEOnDemandRule` class should be created through one of its subclasses: [`NEOnDemandRuleConnect`](neondemandruleconnect.md), [`NEOnDemandRuleDisconnect`](neondemandruledisconnect.md), [`NEOnDemandRuleEvaluateConnection`](neondemandruleevaluateconnection.md), or [`NEOnDemandRuleIgnore`](neondemandruleignore.md).

## Topics

### Accessing match parameters
- [var dnsSearchDomainMatch: [String]?](neondemandrule/dnssearchdomainmatch.md)
  DNS search domains that identify a network.
- [var dnsServerAddressMatch: [String]?](neondemandrule/dnsserveraddressmatch.md)
  DNS server addresses that identify a network.
- [var interfaceTypeMatch: NEOnDemandRuleInterfaceType](neondemandrule/interfacetypematch.md)
  An interface type to identify a network.
- [enum NEOnDemandRuleInterfaceType](neondemandruleinterfacetype.md)
- [var ssidMatch: [String]?](neondemandrule/ssidmatch.md)
  SSIDs that identify a network.
- [var probeURL: URL?](neondemandrule/probeurl.md)
  A URL to probe when all other network identifiers match to validate that an expected resource is available.
### Accessing the rule action
- [var action: NEOnDemandRuleAction](neondemandrule/action.md)
  The action of the On Demand Rule.
- [enum NEOnDemandRuleAction](neondemandruleaction.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NEOnDemandRuleConnect](neondemandruleconnect.md)
- [NEOnDemandRuleDisconnect](neondemandruledisconnect.md)
- [NEOnDemandRuleEvaluateConnection](neondemandruleevaluateconnection.md)
- [NEOnDemandRuleIgnore](neondemandruleignore.md)
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

- [class NEOnDemandRuleConnect](neondemandruleconnect.md)
  A VPN On Demand rule that connects the VPN.
- [class NEOnDemandRuleDisconnect](neondemandruledisconnect.md)
  A VPN On Demand rule that disconnects the VPN.
- [class NEOnDemandRuleIgnore](neondemandruleignore.md)
  A VPN On Demand rule that doesn’t change the status of the VPN.
- [class NEOnDemandRuleEvaluateConnection](neondemandruleevaluateconnection.md)
  A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandrule)*
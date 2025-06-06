# NEOnDemandRuleEvaluateConnection

**Framework**: Network Extension  
**Kind**: class

A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEOnDemandRuleEvaluateConnection
```

#### Overview

When rules of this class match, the properties of the network connection being established are matched against a set of connection rules. The action of the matched rule (if any) is used to determine whether or not the VPN will be started.

## Topics

### Accessing connection rules
- [var connectionRules: [NEEvaluateConnectionRule]?](neondemandruleevaluateconnection/connectionrules.md)
  An array of [`NEEvaluateConnectionRule`](neevaluateconnectionrule.md) objects
- [class NEEvaluateConnectionRule](neevaluateconnectionrule.md)
  `NEEvaluateConnectionRule` associates properties of network connections with an action.

## Relationships

### Inherits From
- [NEOnDemandRule](neondemandrule.md)
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
- [class NEOnDemandRule](neondemandrule.md)
  A base class shared by all VPN On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection)*
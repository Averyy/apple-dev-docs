# NEEvaluateConnectionRule

**Framework**: Network Extension  
**Kind**: class

`NEEvaluateConnectionRule` associates properties of network connections with an action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEEvaluateConnectionRule
```

## Topics

### Initializing a Rule
- [init(matchDomains: [String], andAction: NEEvaluateConnectionRuleAction)](neevaluateconnectionrule/init(matchdomains:andaction:).md)
  Initialize an `NEEvaluateConnectionRule` instance with a list of destination host domains and an action.
### Accessing Rule Match Properties
- [var matchDomains: [String]](neevaluateconnectionrule/matchdomains.md)
  An array of domains used to match the destination hostname of connections. If the destination hostname of a connection matches any of the domains in the array, then the connection matches the rule. Each domain is matched against the destination hostname using suffix matching, and each label in the domain must match an entire label in the hostname. For example, the domain `example.com` will match the hostname `www.example.com` but not `www.anotherexample.com`.
- [var useDNSServers: [String]?](neevaluateconnectionrule/usednsservers.md)
  If the rule matches the connection being established and the action is `NEEvaluateConnectionRuleActionConnectIfNeeded`, the DNS servers specified in this array are used to resolve the destination hostname of the connection while evaluating connectivity to the destination of the connection. If the resolution fails for any reason, the VPN is started.
- [var probeURL: URL?](neevaluateconnectionrule/probeurl.md)
  An HTTP or HTTPS URL. If the rule matches the connection being established and the action is `NEEvaluateConnectionRuleActionConnectIfNeeded` and a request sent to this URL results in a response with an HTTP response code other than 200, then the VPN is started.
### Accessing the Rule Action
- [var action: NEEvaluateConnectionRuleAction](neevaluateconnectionrule/action.md)
  The action to take if the properties of the network connection being established match the rule.
- [enum NEEvaluateConnectionRuleAction](neevaluateconnectionruleaction.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [var connectionRules: [NEEvaluateConnectionRule]?](neondemandruleevaluateconnection/connectionrules.md)
  An array of [`NEEvaluateConnectionRule`](neevaluateconnectionrule.md) objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule)*
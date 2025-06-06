# connectionRules

**Framework**: Network Extension  
**Kind**: property

An array of [`NEEvaluateConnectionRule`](neevaluateconnectionrule.md) objects

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var connectionRules: [NEEvaluateConnectionRule]? { get set }
```

#### Discussion

Each `NEEvaluateConnectionRule` object defines a behavior to take for connections that match the domain of the rule. Each rule is evaluated in order against the properties of a network connection being established. An example configuration has two connection rules: a rule matching `myserver.example.com` with the domain action [`NEEvaluateConnectionRuleAction.neverConnect`](neevaluateconnectionruleaction/neverconnect.md), followed by a rule matching `example.com` with the domain action [`NEEvaluateConnectionRuleAction.connectIfNeeded`](neevaluateconnectionruleaction/connectifneeded.md). This configuration would cause all connections to hostnames in `example.com` that do not resolve on the current network to trigger the VPN, except for `myserver.example.com`.

## See Also

- [class NEEvaluateConnectionRule](neevaluateconnectionrule.md)
  `NEEvaluateConnectionRule` associates properties of network connections with an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleevaluateconnection/connectionrules)*
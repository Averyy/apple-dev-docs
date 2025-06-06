# init(matchDomains:andAction:)

**Framework**: Network Extension  
**Kind**: init

Initialize an `NEEvaluateConnectionRule` instance with a list of destination host domains and an action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(matchDomains domains: [String], andAction action: NEEvaluateConnectionRuleAction)
```

## Parameters

- `domains`: An array of domains used to match the destination hostname of connections. If the destination hostname of a connection matches any of the domains in the array, then the connection matches the rule. Each domain is matched against the destination hostname using suffix matching, and each label in the domain must match an entire label in the hostname. For example, the domain   will match the hostname   but not  .
- `action`: The action to apply for connections matching the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/init(matchdomains:andaction:))*
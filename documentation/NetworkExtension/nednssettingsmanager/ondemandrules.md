# onDemandRules

**Framework**: Network Extension  
**Kind**: property

A list of ordered rules that defines the networks on which the DNS settings will apply.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var onDemandRules: [NEOnDemandRule]? { get set }
```

#### Discussion

An On Demand rule with the action [`NEOnDemandRuleAction.connect`](neondemandruleaction/connect.md) defines a network on which the DNS settings apply. An On Demand rule with the action [`NEOnDemandRuleAction.disconnect`](neondemandruleaction/disconnect.md) causes DNS settings to not apply. An On Demand rule with the action of [`NEOnDemandRuleAction.evaluateConnection`](neondemandruleaction/evaluateconnection.md) can be used to enable the DNS settings on a network with excluded domains, as specified using a [`NEEvaluateConnectionRuleAction.neverConnect`](neevaluateconnectionruleaction/neverconnect.md) rule.

## See Also

- [var isEnabled: Bool](nednssettingsmanager/isenabled.md)
  A Boolean you use to query the enabled state of the DNS settings configuration.
- [var dnsSettings: NEDNSSettings?](nednssettingsmanager/dnssettings.md)
  An object that contains the configuration settings for a DNS server.
- [var localizedDescription: String?](nednssettingsmanager/localizeddescription.md)
  A string that contains the display name of the DNS settings configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/ondemandrules)*
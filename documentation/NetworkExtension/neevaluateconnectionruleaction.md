# NEEvaluateConnectionRuleAction

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEEvaluateConnectionRuleAction
```

## Topics

### Rule Actions
- [NEEvaluateConnectionRuleAction.connectIfNeeded](neevaluateconnectionruleaction/connectifneeded.md)
  Start the VPN if connections to the matching hostname cannot be resolved.
- [NEEvaluateConnectionRuleAction.neverConnect](neevaluateconnectionruleaction/neverconnect.md)
  Do not start the VPN.
### Initializers
- [init?(rawValue: Int)](neevaluateconnectionruleaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: NEEvaluateConnectionRuleAction](neevaluateconnectionrule/action.md)
  The action to take if the properties of the network connection being established match the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neevaluateconnectionruleaction)*
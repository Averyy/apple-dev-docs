# NEOnDemandRuleAction

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
enum NEOnDemandRuleAction
```

## Topics

### Rule Actions
- [NEOnDemandRuleAction.connect](neondemandruleaction/connect.md)
  Start the VPN connection for every connection attempt.
- [NEOnDemandRuleAction.disconnect](neondemandruleaction/disconnect.md)
  Do not start the VPN connection, and disconnect the VPN connection if it is not currently disconnected.
- [NEOnDemandRuleAction.evaluateConnection](neondemandruleaction/evaluateconnection.md)
  Start the VPN after evaluating the destination host being accessed against the rule’s parameters.
- [NEOnDemandRuleAction.ignore](neondemandruleaction/ignore.md)
  Do not start the VPN connection, but do not disconnect it if it is currently connected.
### Initializers
- [init?(rawValue: Int)](neondemandruleaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: NEOnDemandRuleAction](neondemandrule/action.md)
  The action of the On Demand Rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleaction)*
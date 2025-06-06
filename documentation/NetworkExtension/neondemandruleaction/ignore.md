# NEOnDemandRuleAction.ignore

**Framework**: Network Extension  
**Kind**: case

Do not start the VPN connection, but do not disconnect it if it is currently connected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case ignore
```

## See Also

- [NEOnDemandRuleAction.connect](neondemandruleaction/connect.md)
  Start the VPN connection for every connection attempt.
- [NEOnDemandRuleAction.disconnect](neondemandruleaction/disconnect.md)
  Do not start the VPN connection, and disconnect the VPN connection if it is not currently disconnected.
- [NEOnDemandRuleAction.evaluateConnection](neondemandruleaction/evaluateconnection.md)
  Start the VPN after evaluating the destination host being accessed against the rule’s parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleaction/ignore)*
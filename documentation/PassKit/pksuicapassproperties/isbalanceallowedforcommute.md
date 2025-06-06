# isBalanceAllowedForCommute

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates how the balance can be used.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var isBalanceAllowedForCommute: Bool { get }
```

#### Discussion

The Suica network determines the value and usage of this property.

## See Also

- [var transitBalance: NSDecimalNumber](pksuicapassproperties/transitbalance.md)
  The current usable stored value on the transit card.
- [var transitBalanceCurrencyCode: String](pksuicapassproperties/transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.
- [var isLowBalanceGateNotificationEnabled: Bool](pksuicapassproperties/islowbalancegatenotificationenabled.md)
  A Boolean value that determines whether the terminal provides feedback if the balance is low after a deduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isbalanceallowedforcommute)*
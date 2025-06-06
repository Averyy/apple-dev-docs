# transitBalance

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The current usable stored value on the transit card.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
@NSCopying
var transitBalance: NSDecimalNumber { get }
```

## See Also

- [var transitBalanceCurrencyCode: String](pksuicapassproperties/transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.
- [var isBalanceAllowedForCommute: Bool](pksuicapassproperties/isbalanceallowedforcommute.md)
  A Boolean value that indicates how the balance can be used.
- [var isLowBalanceGateNotificationEnabled: Bool](pksuicapassproperties/islowbalancegatenotificationenabled.md)
  A Boolean value that determines whether the terminal provides feedback if the balance is low after a deduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/transitbalance)*
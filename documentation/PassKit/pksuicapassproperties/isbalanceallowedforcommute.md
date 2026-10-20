# isBalanceAllowedForCommute

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates how the balance can be used.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var isBalanceAllowedForCommute: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isBalanceAllowedForCommute) BOOL balanceAllowedForCommute;
```

#### Discussion

The Suica network determines the value and usage of this property.

## See Also

### Getting suica balance information
- [var transitBalance: NSDecimalNumber](./transitbalance.md)
  The current usable stored value on the transit card.
- [var transitBalanceCurrencyCode: String](./transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.
- [var isLowBalanceGateNotificationEnabled: Bool](./islowbalancegatenotificationenabled.md)
  A Boolean value that determines whether the terminal provides feedback if the balance is low after a deduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isbalanceallowedforcommute)*
# transitBalanceCurrencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The currency code associated with the balance on the pass.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
var transitBalanceCurrencyCode: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * transitBalanceCurrencyCode;
```

#### Discussion

Represent the currency code associated with [`transitBalance`](./transitbalance.md) as a three-letter ISO 4217 alphabetic code. For example, US Dollars is `USD` and Japanese Yen is `JPY`.

## See Also

### Getting suica balance information
- [var transitBalance: NSDecimalNumber](./transitbalance.md)
  The current usable stored value on the transit card.
- [var isBalanceAllowedForCommute: Bool](./isbalanceallowedforcommute.md)
  A Boolean value that indicates how the balance can be used.
- [var isLowBalanceGateNotificationEnabled: Bool](./islowbalancegatenotificationenabled.md)
  A Boolean value that determines whether the terminal provides feedback if the balance is low after a deduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/transitbalancecurrencycode)*
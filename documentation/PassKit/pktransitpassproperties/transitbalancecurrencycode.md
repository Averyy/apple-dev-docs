# transitBalanceCurrencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The currency code associated with the balance on the pass.

**Availability**:
- iOS 11.3+ - Deprecated in 15.0
- iPadOS 11.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 11.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.3+ - Deprecated in 8.0

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

### Getting balance information
- [var transitBalance: NSDecimalNumber](./transitbalance.md)
  The current usable stored value on the transit card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/transitbalancecurrencycode)*
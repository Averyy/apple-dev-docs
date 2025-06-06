# transitBalanceCurrencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The currency code associated with the balance on the pass.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var transitBalanceCurrencyCode: String { get }
```

#### Discussion

Represent the currency code associated with [`transitBalance`](pktransitpassproperties/transitbalance.md) as a three-letter ISO 4217 alphabetic code. For example, US Dollars is `USD` and Japanese Yen is `JPY`.

## See Also

- [var transitBalance: NSDecimalNumber](pktransitpassproperties/transitbalance.md)
  The current usable stored value on the transit card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/transitbalancecurrencycode)*
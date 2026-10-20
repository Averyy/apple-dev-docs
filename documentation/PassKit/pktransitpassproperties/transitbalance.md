# transitBalance

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The current usable stored value on the transit card.

**Availability**:
- iOS 11.3+ - Deprecated in 15.0
- iPadOS 11.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 11.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.3+ - Deprecated in 8.0

## Declaration

```swift
@NSCopying
var transitBalance: NSDecimalNumber { get }
```

```objc
@property (nonatomic, copy, readonly) NSDecimalNumber * transitBalance;
```

## See Also

### Getting balance information
- [var transitBalanceCurrencyCode: String](./transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/transitbalance)*
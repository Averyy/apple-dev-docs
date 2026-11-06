# price

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The per-seat price of the seats in this tier.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let price: Decimal
```

## Discussion

The value is in units of the transaction’s [`currency`](../../currency.md). The App Store Server API and the transaction’s JSON representation give the price in milliunits of the currency.

## See Also

### Getting the price and seats
- [let quantity: Int](./quantity.md)
  The number of seats that the customer bought at this tier’s price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct/pricetier/price)*
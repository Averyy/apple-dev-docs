# maximumSeatQuantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of seats in this price tier.

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
let maximumSeatQuantity: Int?
```

## Discussion

Each tier covers the seats that follow the previous tier. For example, two tiers with a value of 5 cover seats 1 through 5 and 6 through 10.

This value is `nil` for the last tier, which has no upper bound.

## See Also

### Getting the price and seats
- [let price: Decimal](./price.md)
  The per-seat price of the seats in this tier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/seatpricetier/maximumseatquantity)*
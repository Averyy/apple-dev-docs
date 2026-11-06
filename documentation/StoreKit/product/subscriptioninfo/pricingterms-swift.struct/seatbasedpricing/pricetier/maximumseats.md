# maximumSeats

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The upper limit of this tier’s seat range.

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
let maximumSeats: Int?
```

## Discussion

The range includes this number of seats. This value is `nil` for the last tier, which applies to every seat count from [`minimumSeats`](./minimumseats.md) up.

## See Also

### Getting the seat range
- [let minimumSeats: Int](./minimumseats.md)
  The seat count at which this tier’s range starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetier/maximumseats)*
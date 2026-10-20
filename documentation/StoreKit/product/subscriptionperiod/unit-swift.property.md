# unit

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The increment of time for the subscription period.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let unit: Product.SubscriptionPeriod.Unit
```

#### Discussion

The units used to specify a subscription period include day, week, month, and year, as defined in [`Product.SubscriptionPeriod.Unit`](./unit-swift.enum.md).

To calculate the duration of one subscription period, multiply the [`unit`](./unit-swift.property.md) by the number of units ([`value`](./value.md)).

## See Also

### Getting the subscription period
- [let value: Int](./value.md)
  The number of period units.
- [Product.SubscriptionPeriod.Unit](./unit-swift.enum.md)
  Units of time that describe subscription periods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod/unit-swift.property)*
# periodCount

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of periods that the subscription offer renews for.

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
let periodCount: Int
```

## Discussion

If the payment mode is [`payAsYouGo`](./paymentmode-swift.struct/payasyougo.md), the period count represents the number of periods the subscription renews at the discounted [`price`](./price.md).

The period count is 1 for offers with payment modes [`freeTrial`](./paymentmode-swift.struct/freetrial.md) and [`payUpFront`](./paymentmode-swift.struct/payupfront.md).

## See Also

### Getting the subscription duration
- [let period: Product.SubscriptionPeriod](./period.md)
  The subscription period for the subscription offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/periodcount)*
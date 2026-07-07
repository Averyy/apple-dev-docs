# periodCount

**Framework**: StoreKit  
**Kind**: property

The number of periods that the subscription offer renews for.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let periodCount: Int
```

#### Discussion

If the payment mode is [`payAsYouGo`](product/subscriptionoffer/paymentmode-swift.struct/payasyougo.md), the period count represents the number of periods the subscription renews at the discounted [`price`](product/subscriptionoffer/price.md).

The period count is 1 for offers with payment modes [`freeTrial`](product/subscriptionoffer/paymentmode-swift.struct/freetrial.md) and [`payUpFront`](product/subscriptionoffer/paymentmode-swift.struct/payupfront.md).

## See Also

- [let period: Product.SubscriptionPeriod](product/subscriptionoffer/period.md)
  The subscription period for the subscription offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionoffer/periodcount)*
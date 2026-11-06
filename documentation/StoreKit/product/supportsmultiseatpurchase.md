# supportsMultiSeatPurchase

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether multiseat purchases are allowed for this product.

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
let supportsMultiSeatPurchase: Bool
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../testing-multiseat-subscriptions.md)

## Discussion

When this value is `true`, you can sell the product as a multiseat subscription by using the [`seats(_:)`](./purchaseoption/seats%28_%29.md) purchase option.

For more information, see [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Getting subscription information
- [let subscription: Product.SubscriptionInfo?](./subscription.md)
  The subscription information for an auto-renewable subscripton.
- [Product.SubscriptionInfo](./subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [Product.SubscriptionPeriod](./subscriptionperiod.md)
  Values that represent the duration of time between subscription renewals.
- [Product.SubscriptionOffer](./subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionInfo.Status](./subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/supportsmultiseatpurchase)*
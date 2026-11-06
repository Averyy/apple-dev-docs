# renewalQuantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of seats in a multiseat subscription at its next renewal.

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
let renewalQuantity: Int?
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

The value is the number of seats currently expected at the next renewal, including any seat additions and reductions so far. It can change until the subscription renews.

For more information, see [Managing the life cycle of multiseat subscriptions](../../../managing-the-life-cycle-of-multiseat-subscriptions.md).

## See Also

### Getting multiseat renewal information
- [let multiSeatInfo: Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo?](./multiseatinfo-swift.property.md)
  The seat information for the next renewal of a multiseat subscription.
- [Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo](./multiseatinfo-swift.struct.md)
  The price tiers of a multiseat subscription at its next renewal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/renewalquantity)*
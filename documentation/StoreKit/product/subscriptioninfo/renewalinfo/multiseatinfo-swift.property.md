# multiSeatInfo

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The seat information for the next renewal of a multiseat subscription.

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
let multiSeatInfo: Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo?
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../../../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

This value is `nil` if the next renewal isn’t for a multiseat subscription.

## See Also

### Getting multiseat renewal information
- [let renewalQuantity: Int?](./renewalquantity.md)
  The number of seats in a multiseat subscription at its next renewal.
- [Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo](./multiseatinfo-swift.struct.md)
  The price tiers of a multiseat subscription at its next renewal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/multiseatinfo-swift.property)*
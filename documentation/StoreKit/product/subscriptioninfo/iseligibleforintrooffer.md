# isEligibleForIntroOffer

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the customer is eligible for an introductory offer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isEligibleForIntroOffer: Bool { get async }
```

#### Discussion

This value is `true` if the customer is eligible for an introductory offer on this auto-renewable subscription, or any auto-renewable subscription in the same subscription group; this value is `false` otherwise. This value may be `true` even if you haven’t set up an introductory offer in App Store Connect. The following example illustrates checking the [`subscription`](product/subscription.md) property of a product to determine whether the user is eligible for an introductory offer.

```swift
func eligibleForIntro(product: Product) async throws -> Bool {
    guard let renewableSubscription = product.subscription else {
        // No renewable subscription is available for this product.
        return false
    }
    if await renewableSubscription.isEligibleForIntroOffer {
        // The product is eligible for an introductory offer.
        return true
    }
    return false
}
```

To specify a customer’s eligibility for an introductory offer, see [`introductoryOfferEligibility(compactJWS:)`](product/purchaseoption/introductoryoffereligibility(compactjws:).md).

## See Also

- [static func isEligibleForIntroOffer(for: String) async -> Bool](product/subscriptioninfo/iseligibleforintrooffer(for:).md)
  Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [let introductoryOffer: Product.SubscriptionOffer?](product/subscriptioninfo/introductoryoffer.md)
  Information about the introductory offer available for the auto-renewable subscription.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer)*
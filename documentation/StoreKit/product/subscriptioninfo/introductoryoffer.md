# introductoryOffer

**Framework**: StoreKit  
**Kind**: property

Information about the introductory offer available for the auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let introductoryOffer: Product.SubscriptionOffer?
```

#### Discussion

This value is `nil` if you don’t set up an introductory offer in App Store Connect. Use [`isEligibleForIntroOffer`](product/subscriptioninfo/iseligibleforintrooffer.md) to determine whether the customer is eligible for an introductory offer.

## See Also

- [var isEligibleForIntroOffer: Bool](product/subscriptioninfo/iseligibleforintrooffer.md)
  A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [static func isEligibleForIntroOffer(for: String) async -> Bool](product/subscriptioninfo/iseligibleforintrooffer(for:).md)
  Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/introductoryoffer)*
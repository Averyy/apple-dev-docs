# isEligibleForIntroOffer(for:)

**Framework**: StoreKit  
**Kind**: method

Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func isEligibleForIntroOffer(for groupID: String) async -> Bool
```

#### Return Value

`true` if the customer is eligible for an introductory offer on any auto-renewable subscription within the subscription group; `false` otherwise.

#### Discussion

This value may be `true` even if you haven’t set up an introductory offer in App Store Connect.

## Parameters

- `groupID`: The subscription group identifier to check eligibility for an introductory offer.

## See Also

- [var isEligibleForIntroOffer: Bool](product/subscriptioninfo/iseligibleforintrooffer.md)
  A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [let introductoryOffer: Product.SubscriptionOffer?](product/subscriptioninfo/introductoryoffer.md)
  Information about the introductory offer available for the auto-renewable subscription.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer(for:))*
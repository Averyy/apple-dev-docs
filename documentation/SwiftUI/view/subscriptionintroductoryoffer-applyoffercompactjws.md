# subscriptionIntroductoryOffer(applyOffer:compactJWS:)

**Framework**: SwiftUI  
**Kind**: method

Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func subscriptionIntroductoryOffer(applyOffer: @escaping (Product, Product.SubscriptionInfo) -> Bool, compactJWS: @escaping (Product, Product.SubscriptionInfo) async throws -> String) -> some View
```

#### Discussion

Subscription stores within this view uses the introductory subscription offers to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreControlStyle) to style the in-app subscription store. Standard [`ProductViewStyle`](https://developer.apple.com/documentation/StoreKit/ProductViewStyle) instances don’t show introductory or promotional offers in UI, instead use [`SubscriptionStoreView`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreView).

Determine if the introductory offer should be displayed in the view and applied to the purchase using the `applyOffer`. If the signature passes validation, the system applies or removes the offer to the purchases according to the offer eligibility preference. If the signature fails validation, the purchase will fail with [`Product.PurchaseError.invalidOfferSignature`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseError/invalidOfferSignature).

## Parameters

- `applyOffer`: The system calls this function before drawing the given subscription product on   the subscription store view. Return if the introductory offer should be applied   to a given product, if any, to have system-provided UI reflect the discounted terms under   the selected offer.
- `compactJWS`: The system calls this function before processing a purchase, with the   product to be purchased provided as a parameter. Return a compact JWS   signature you generate on your server that validates the selected offer eligibility preference.   Errors thrown from this closure will be surfaced via the    modifier.   For information about generating the JWS signature, see   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionintroductoryoffer(applyoffer:compactjws:))*
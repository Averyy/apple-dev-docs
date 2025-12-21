# subscriptionPromotionalOffer(offer:compactJWS:)

**Framework**: SwiftUI  
**Kind**: method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

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
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, compactJWS: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> String) -> some View
```

#### Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreControlStyle) to style the in-app subscription store. Standard [`ProductViewStyle`](https://developer.apple.com/documentation/StoreKit/ProductViewStyle) instances don’t show introductory or promotional offers in UI. Use the [`SubscriptionStoreView`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreView) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [`Product.PurchaseError.invalidOfferSignature`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseError/invalidOfferSignature).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## Parameters

- `offer`: The system calls this function before drawing the given subscription product on   the subscription store view. Return the promotional offer to apply to the   product, if any, to have system-provided UI reflect the discounted terms under   the selected offer.
- `compactJWS`: The system calls this function before processing a purchase, with the   product to be purchased provided as a parameter, along with the selected   subscription offer to be applied to the purchase. Return a compact JWS   signature you generate on your server that validates the selected offer.   Errors thrown from this closure will be surfaced via the    modifier.   For information about generating the JWS signature, see   ..


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:compactjws:))*
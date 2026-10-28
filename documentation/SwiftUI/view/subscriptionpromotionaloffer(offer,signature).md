# subscriptionPromotionalOffer(offer:signature:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0
- macOS 14.4+ - Deprecated in 26.0
- tvOS 17.4+ - Deprecated in 26.0
- visionOS 1.1+ - Deprecated in 26.0
- watchOS 10.4+ - Deprecated in 26.0

> **Deprecated**: Sign promotional offers with JWS and use the [`subscriptionPromotionalOffer(offer:compactJWS:)`](./subscriptionpromotionaloffer%28offer,compactjws%29.md) view modifier instead.

## Declaration

```swift
nonisolated
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View
```

## Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](../../StoreKit/subscriptionstorecontrolstyle.md) to style the in-app subscription store. Standard [`ProductViewStyle`](../../StoreKit/productviewstyle.md) instances don’t show introductory or promotional offers in UI. Use the [`SubscriptionStoreView`](../../StoreKit/subscriptionstoreview.md) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [`Product.PurchaseError.invalidOfferSignature`](../../StoreKit/product/purchaseerror/invalidoffersignature.md).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## Parameters

- `offer`: The system calls this function before drawing the given subscription product on the subscription store view. Return the promotional offer to apply to the product, if any, to have system-provided UI reflect the discounted terms under the selected offer.
- `signature`: The system calls this function before processing a purchase, with the product to be purchased provided as a parameter, along with the selected subscription offer to be applied to the purchase. Return a signature you generate on your server that validates the selected offer. Errors thrown from this closure will be surfaced via the [`onInAppPurchaseCompletion(perform:)`](./oninapppurchasecompletion%28perform%29.md) modifier. For information about generating the signature, see [Generating a signature for promotional offers](../../StoreKit/generating-a-signature-for-promotional-offers.md).

## See Also

### Technology-specific modifiers
- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](./posttophotossharedalbumsheet%28ispresented,items,photolibrary,defaultalbumidentifier,completion%29.md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](./offercoderedemption%28ispresented,oncompletion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:))*
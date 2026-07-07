# subscriptionPromotionalOffer(offer:signature:)

**Framework**: SwiftUI  
**Kind**: method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
nonisolated
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View
```

#### Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreControlStyle) to style the in-app subscription store. Standard [`ProductViewStyle`](https://developer.apple.com/documentation/StoreKit/ProductViewStyle) instances don’t show introductory or promotional offers in UI. Use the [`SubscriptionStoreView`](https://developer.apple.com/documentation/StoreKit/SubscriptionStoreView) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [`Product.PurchaseError.invalidOfferSignature`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseError/invalidOfferSignature).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## Parameters

- `offer`: The system calls this function before drawing the given subscription product on the subscription store view. Return the promotional offer to apply to the product, if any, to have system-provided UI reflect the discounted terms under the selected offer.
- `signature`: The system calls this function before processing a purchase, with the product to be purchased provided as a parameter, along with the selected subscription offer to be applied to the purchase. Return a signature you generate on your server that validates the selected offer. Errors thrown from this closure will be surfaced via the [`onInAppPurchaseCompletion(perform:)`](view/oninapppurchasecompletion(perform:).md) modifier. For information about generating the signature, see [`Generating a signature for promotional offers`](https://developer.apple.com/documentation/StoreKit/generating-a-signature-for-promotional-offers).

## See Also

- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](view/offercoderedemption(ispresented:oncompletion:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:))*
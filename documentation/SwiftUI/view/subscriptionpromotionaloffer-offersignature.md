# subscriptionPromotionalOffer(offer:signature:)

**Framework**: SwiftUI  
**Kind**: method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
nonisolated
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View
```

## See Also

- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](view/offercoderedemption(ispresented:oncompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:))*
# postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0

> **Deprecated**: Use View.photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:) instead.

## Declaration

```swift
nonisolated
func postToPhotosSharedAlbumSheet(isPresented: Binding<Bool>, items: [PHPickerResult], photoLibrary: PHPhotoLibrary, defaultAlbumIdentifier: String? = nil, completion: ((Result<Void, any Error>) -> Void)? = nil) -> some View
```

**Other overloads**:

```swift
nonisolated
func postToPhotosSharedAlbumSheet(isPresented: Binding<Bool>, items: [PhotosPickerItem], photoLibrary: PHPhotoLibrary, defaultAlbumIdentifier: String? = nil, completion: ((Result<Void, any Error>) -> Void)? = nil) -> some View
```

## Parameters

- `isPresented`: The binding to whether the sheet should be shown.
- `items`: The items to be posted to the shared album.
- `photoLibrary`: Library to choose from.
- `defaultAlbumIdentifier`: Identifier for the shared album to be pre-selected. If none provided user can manually choose the shared album in UI.
- `completion`: Called with the result on completion of the request.

## See Also

### Technology-specific modifiers
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](./offercoderedemption%28ispresented,oncompletion%29.md)
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](./subscriptionpromotionaloffer%28offer,signature%29.md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:))*
# offerCodeRedemption(isPresented:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View
```

#### Discussion

The [`offerCodeRedemption(isPresented:onCompletion:)`](view/offercoderedemption(ispresented:oncompletion:).md) method displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this function to enable customers to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(in:)`.

> ❗ **Important**: Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [`Supporting subscription offer codes in your app`](https://developer.apple.com/documentation/StoreKit/supporting-subscription-offer-codes-in-your-app).

The following code example shows a view that displays the offer code redemption sheet upon a button press:

```swift
import SwiftUI
import StoreKit

struct ContentView: View {
    @State private var redeemSheetIsPresented = false

    var body: some View {
        Button("Present offer code redemption sheet.") {
            redeemSheetIsPresented = true
        }
        .offerCodeRedemption(isPresented: $redeemSheetIsPresented) { result in
            // Handle result
        }
    }
}
```

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](https://developer.apple.com/documentation/StoreKit/Transaction/updates). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to true to cause the system to display the sheet. The system sets it to false when it dismisses the sheet.
- `onCompletion`: A closure that returns the result of the presentation. In Mac apps built with Mac Catalyst, the completion handler returns a failure with an error prior to macOS 15.

## See Also

- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](view/subscriptionpromotionaloffer(offer:signature:).md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(ispresented:oncompletion:))*
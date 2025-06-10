# presentOfferCodeRedeemSheet(in:)

**Framework**: StoreKit  
**Kind**: method

Displays a sheet in the window scene that enables users to redeem a subscription offer code that you configure in App Store Connect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(in scene: UIWindowScene) async throws
```

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Implementing offer codes in your app](implementing-offer-codes-in-your-app.md)
- [Testing purchases made outside your app](testing-purchases-made-outside-your-app.md)

#### Discussion

The [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) method displays a system sheet in the window scene, where customers can enter and redeem subscription offer codes. If you generate subscription offer codes in App Store Connect, call this function to enable users to redeem the offer. To display the sheet using SwiftUI, see [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)).

> ❗ **Important**:  Set up subscription offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [`Supporting subscription offer codes in your app`](supporting-subscription-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running. For more information, see [`updates`](transaction/updates.md).

In Mac apps built with Mac Catalyst, this method throws a [`StoreKitError.unknown`](storekiterror/unknown.md) error.

## Parameters

- `scene`: The   that StoreKit uses to display the offer code redemption sheet.

## See Also

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
  Provide subscription service for customers who redeem offer codes through the App Store or within your app.
- [nonisolated func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View
](../SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:).md)
  Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.
- [static func presentOfferCodeRedeemSheet(from: NSViewController) async throws](appstore/presentoffercoderedeemsheet(from:).md)
  Displays a sheet in the view that enables users to redeem a subscription offer code that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(in:))*
# presentOfferCodeRedeemSheet(from:)

**Framework**: StoreKit  
**Kind**: method

Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(from controller: NSViewController) async throws
```

## Mentions

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

This method displays a system sheet in the view, where customers can enter and redeem offer codes. Use this method if you generate offer codes in App Store Connect and your app uses AppKit.

> ❗ **Important**:  Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [`Supporting offer codes in your app`](supporting-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## Parameters

- `controller`: An   that StoreKit uses to display the offer code redemption sheet.

## See Also

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [static func presentOfferCodeRedeemSheet(in: UIWindowScene) async throws](appstore/presentoffercoderedeemsheet(in:).md)
  Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](../SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:))*
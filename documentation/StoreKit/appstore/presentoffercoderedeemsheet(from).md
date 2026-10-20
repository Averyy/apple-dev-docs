# presentOfferCodeRedeemSheet(from:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.

**Availability**:
- macOS 15.0+ - Deprecated in 27.0

> **Deprecated**: Use [`presentOfferCodeRedeemSheet(from:options:)`](./presentoffercoderedeemsheet%28from,options%29-gj8m.md) instead.

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(from controller: NSViewController) async throws
```

## Mentions

- [Supporting subscription offer codes in your app](../supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

This method displays a system sheet in the view, where customers can enter and redeem offer codes. Use this method if you generate offer codes in App Store Connect and your app uses AppKit.

> ❗ **Important**:  Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](../transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## Parameters

- `controller`: An [`NSViewController`](../../AppKit/nsviewcontroller.md) that StoreKit uses to display the offer code redemption sheet.

## See Also

### Deprecated
- [static func presentOfferCodeRedeemSheet(in: UIWindowScene) async throws](./presentoffercoderedeemsheet%28in%29.md)
  Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../../SwiftUI/view/offercoderedemption%28ispresented,oncompletion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:))*
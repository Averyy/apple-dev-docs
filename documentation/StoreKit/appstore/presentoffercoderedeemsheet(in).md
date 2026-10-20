# presentOfferCodeRedeemSheet(in:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use [`presentOfferCodeRedeemSheet(from:options:)`](./presentoffercoderedeemsheet%28from,options%29-89agc.md) instead.

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(in scene: UIWindowScene) async throws
```

## Mentions

- [Implementing offer codes in your app](../implementing-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](../supporting-subscription-offer-codes-in-your-app.md)
- [Testing purchases made outside your app](../testing-purchases-made-outside-your-app.md)

#### Discussion

The [`presentOfferCodeRedeemSheet(in:)`](./presentoffercoderedeemsheet%28in%29.md) method displays a system sheet in the window scene, where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this function to enable customers to redeem the offer. To display the sheet using SwiftUI, see [`offerCodeRedemption(isPresented:onCompletion:)`](../../SwiftUI/view/offercoderedemption%28ispresented,oncompletion%29.md).

> ❗ **Important**:  Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI.

For more information on offer codes, see [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md).

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](../transaction/updates.md). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running. For more information, see [`updates`](../transaction/updates.md).

In Mac apps built with Mac Catalyst, this method throws a [`StoreKitError.unknown`](../storekiterror/unknown.md) error.

## Parameters

- `scene`: The [`UIWindowScene`](../../UIKit/uiwindowscene.md) that StoreKit uses to display the offer code redemption sheet.

## See Also

### Deprecated
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../../SwiftUI/view/offercoderedemption%28ispresented,oncompletion%29.md)
- [static func presentOfferCodeRedeemSheet(from: NSViewController) async throws](./presentoffercoderedeemsheet%28from%29.md)
  Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(in:))*
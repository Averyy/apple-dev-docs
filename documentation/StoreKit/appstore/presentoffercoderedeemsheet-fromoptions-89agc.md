# presentOfferCodeRedeemSheet(from:options:)

**Framework**: StoreKit  
**Kind**: method

Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(from viewController: UIViewController, options: Set<RedeemOption> = []) async throws -> VerificationResult<Transaction>
```

## Mentions

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)

#### Return Value

A [`VerificationResult`](verificationresult.md) containing the [`Transaction`](transaction.md) that the redemption produces.

#### Discussion

> **Note**: [`StoreKitError`](storekiterror.md) if the system cannot present the sheet or the redemption fails.

## Parameters

- `viewController`: The `UIViewController` that StoreKit uses to display the offer code redemption sheet.
- `options`: A set of [`RedeemOption`](redeemoption.md) values to configure the offer code redemption.

## See Also

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View
](../SwiftUI/View/offerCodeRedemption(options:isPresented:onCompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc)*
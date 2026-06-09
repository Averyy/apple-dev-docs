# presentOfferCodeRedeemSheet(from:options:)

**Framework**: StoreKit  
**Kind**: method

Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func presentOfferCodeRedeemSheet(from window: NSWindow, options: Set<RedeemOption> = []) async throws -> VerificationResult<Transaction>
```

#### Return Value

A [`VerificationResult`](verificationresult.md) containing the [`Transaction`](transaction.md) that the redemption produces.

#### Discussion

> **Note**: [`StoreKitError`](storekiterror.md) if the system cannot present the sheet or the redemption fails.

## Parameters

- `window`: The `NSWindow` that StoreKit uses to display the offer code redemption sheet.
- `options`: A set of [`RedeemOption`](redeemoption.md) values to configure the offer code redemption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-gj8m)*
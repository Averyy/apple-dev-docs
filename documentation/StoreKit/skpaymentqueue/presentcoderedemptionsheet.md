# presentCodeRedemptionSheet()

**Framework**: Storekit  
**Kind**: method

Displays a sheet that enables customers to redeem subscription offer codes that you configure in App Store Connect.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func presentCodeRedemptionSheet()
```

## Mentions

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Implementing offer codes in your app](implementing-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)

#### Discussion

The [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) function displays a system sheet where customers can enter and redeem subscription offer codes. If you generate subscription offer codes in App Store Connect, call this function to enable customers to redeem the offer. For information on implementing subscription offer codes, see [`Implementing offer codes in your app`](implementing-offer-codes-in-your-app.md).

> **Note**:  For apps with more than one scene, and on iOS 16 or later and iPadOS 16 or later, use [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) or [`presentOfferCodeRedeemSheet(in:)`](appstore/presentoffercoderedeemsheet(in:).md) instead.

When your app calls [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md), the system determines where to display the screen. Use [`presentCodeRedemptionSheet()`](skpaymentqueue/presentcoderedemptionsheet().md) to support devices running iOS 14 through iOS 15, and iPadOS 14 through iPadOS 15.

> ❗ **Important**:  Set up subscription offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For information on configuring and generating subscription offer codes, see [`Set up offer codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1).

This method applies to subscription offer codes only; it doesn’t apply to promo codes for apps or in-app purchases. For more information on promo codes, see [`Request and manage promo codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev50869de4a).

This function doesn’t affect Mac apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/presentcoderedemptionsheet())*
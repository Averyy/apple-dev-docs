# Product.PurchaseError.multiSeatPurchaseDisabled

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The product doesn’t support multiseat purchases.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
case multiSeatPurchaseDisabled
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

The purchase fails with this error when you add the [`seats(_:)`](../purchaseoption/seats%28_%29.md) purchase option for a product that isn’t enabled for multiseat purchases in App Store Connect. Check [`supportsMultiSeatPurchase`](../supportsmultiseatpurchase.md) before you offer seats. For more information, see [Manage purchase options for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions) and [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Getting Purchase Error Codes
- [Product.PurchaseError.invalidOfferIdentifier](./invalidofferidentifier.md)
  The promotional offer identifier provided in the purchase options is invalid.
- [Product.PurchaseError.productUnavailable](./productunavailable.md)
  The product isn’t available.
- [Product.PurchaseError.purchaseNotAllowed](./purchasenotallowed.md)
  The user isn’t allowed to make purchases.
- [Product.PurchaseError.ineligibleForOffer](./ineligibleforoffer.md)
  The user isn’t eligible for the offer.
- [Product.PurchaseError.invalidOfferPrice](./invalidofferprice.md)
  The price of the offer isn’t valid.
- [Product.PurchaseError.invalidOfferSignature](./invalidoffersignature.md)
  The offer signature isn’t valid.
- [Product.PurchaseError.invalidQuantity](./invalidquantity.md)
  The quantity to purchase is invalid.
- [Product.PurchaseError.missingOfferParameters](./missingofferparameters.md)
  The offer parameters are missing.
- [Product.PurchaseError.seatReductionNotAllowed](./seatreductionnotallowed.md)
  The purchase would reduce the number of seats in a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseerror/multiseatpurchasedisabled)*
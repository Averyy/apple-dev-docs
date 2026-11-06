# Product.PurchaseError.seatReductionNotAllowed

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The purchase would reduce the number of seats in a multiseat subscription.

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
case seatReductionNotAllowed
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

The purchase fails with this error when the total you pass to [`seats(_:)`](../purchaseoption/seats%28_%29.md) is less than the number of seats the subscription already has. Only the group purchaser can reduce the number of seats, in Manage Subscriptions, and the change takes effect at the next renewal. To let the group purchaser change the number of seats, present Manage Subscriptions with [`showManageSubscriptions(in:)`](../../appstore/showmanagesubscriptions%28in%29.md) or, on macOS, [`showManageSubscriptions(from:)`](../../appstore/showmanagesubscriptions%28from%29.md).

For more information, see [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md).

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
- [Product.PurchaseError.multiSeatPurchaseDisabled](./multiseatpurchasedisabled.md)
  The product doesn’t support multiseat purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseerror/seatreductionnotallowed)*
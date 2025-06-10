# Product.PurchaseError

**Framework**: StoreKit  
**Kind**: enum

Error information for product purchase errors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum PurchaseError
```

#### Overview

The [`purchase(options:)`](product/purchase(options:).md) function may throw a purchase error.

## Topics

### Getting Purchase Error Codes
- [Product.PurchaseError.invalidOfferIdentifier](product/purchaseerror/invalidofferidentifier.md)
  The promotional offer identifier provided in the purchase options is invalid.
- [Product.PurchaseError.productUnavailable](product/purchaseerror/productunavailable.md)
  The product isn’t available.
- [Product.PurchaseError.purchaseNotAllowed](product/purchaseerror/purchasenotallowed.md)
  The user isn’t allowed to make purchases.
- [Product.PurchaseError.ineligibleForOffer](product/purchaseerror/ineligibleforoffer.md)
  The user isn’t eligible for the offer.
- [Product.PurchaseError.invalidOfferPrice](product/purchaseerror/invalidofferprice.md)
  The price of the offer isn’t valid.
- [Product.PurchaseError.invalidOfferSignature](product/purchaseerror/invalidoffersignature.md)
  The offer signature isn’t valid.
- [Product.PurchaseError.invalidQuantity](product/purchaseerror/invalidquantity.md)
  The quantity to purchase is invalid.
- [Product.PurchaseError.missingOfferParameters](product/purchaseerror/missingofferparameters.md)
  The offer parameters are missing.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-6dj6y.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: UIViewController, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-3bivf.md)
  Processes a purchase for the product.
- [func purchase(confirmIn: NSWindow, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-8eai6.md)
  Processes a purchase for the product.
- [Product.PurchaseOption](product/purchaseoption.md)
  Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseerror)*
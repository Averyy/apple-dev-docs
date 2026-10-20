# Product.PurchaseError

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Error information for product purchase errors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum PurchaseError
```

#### Overview

The [`purchase(options:)`](./purchase%28options%29.md) function may throw a purchase error.

## Topics

### Getting Purchase Error Codes
- [Product.PurchaseError.invalidOfferIdentifier](./purchaseerror/invalidofferidentifier.md)
  The promotional offer identifier provided in the purchase options is invalid.
- [Product.PurchaseError.productUnavailable](./purchaseerror/productunavailable.md)
  The product isn’t available.
- [Product.PurchaseError.purchaseNotAllowed](./purchaseerror/purchasenotallowed.md)
  The user isn’t allowed to make purchases.
- [Product.PurchaseError.ineligibleForOffer](./purchaseerror/ineligibleforoffer.md)
  The user isn’t eligible for the offer.
- [Product.PurchaseError.invalidOfferPrice](./purchaseerror/invalidofferprice.md)
  The price of the offer isn’t valid.
- [Product.PurchaseError.invalidOfferSignature](./purchaseerror/invalidoffersignature.md)
  The offer signature isn’t valid.
- [Product.PurchaseError.invalidQuantity](./purchaseerror/invalidquantity.md)
  The quantity to purchase is invalid.
- [Product.PurchaseError.missingOfferParameters](./purchaseerror/missingofferparameters.md)
  The offer parameters are missing.
### Enumeration Cases
- [Product.PurchaseError.paymentMethodBindingConfigurationRequired](./purchaseerror/paymentmethodbindingconfigurationrequired.md)
  The customer needs to add a payment method to their Apple Account before making a purchase; use [`PaymentMethodBinding`](../paymentmethodbinding.md) to prompt the customer and bind the payment method.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Purchasing a product
- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28options%29.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28confirmin,options%29-6dj6y.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: UIViewController, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28confirmin,options%29-3bivf.md)
  Processes a purchase for the product.
- [func purchase(confirmIn: NSWindow, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](./purchase%28confirmin,options%29-8eai6.md)
  Processes a purchase for the product.
- [Product.PurchaseOption](./purchaseoption.md)
  Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [Product.PurchaseResult](./purchaseresult.md)
  The result of a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseerror)*
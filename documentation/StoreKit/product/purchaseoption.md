# Product.PurchaseOption

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.

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
struct PurchaseOption
```

## Overview

Associate purchase options with an Apple In-App Purchase when you call the methods to initiate a purchase, such as [`purchase(options:)`](./purchase%28options%29.md) or [`purchase(confirmIn:options:)`](./purchase%28confirmin,options%29-6dj6y.md). Use the testing-specific options with [StoreKit Test](../../StoreKitTest/StoreKitTest.md) or in the sandbox testing environment.

Purchase options enable you to provide additional information for the purchase, such as an app account token, promotional offer, win back offer, and quantity. You can also use purchase options to indicate how the transaction behaves if the storefront changes, and to indicate whether the transaction is eligible for an introductory offer.

> ❗ **Important**:  Purchases fail if a purchase option is invalid, and can result in the purchase method throwing a [`StoreKitError`](../storekiterror.md) or [`Product.PurchaseError`](./purchaseerror.md).

### Use purchase options during testing

In the sandbox testing environment, use [`simulatesAskToBuyInSandbox(_:)`](./purchaseoption/simulatesasktobuyinsandbox%28_%29.md) to test Ask To Buy scenarios.

In the Xcode testing environment with [StoreKit Test](../../StoreKitTest/StoreKitTest.md), use the following testing-specific purchase options when you call [`buyProduct(identifier:options:)`](../../StoreKitTest/sktestsession/buyproduct%28identifier,options%29.md):

- Use [`codeOffer(referenceName:)`](./purchaseoption/codeoffer%28referencename%29.md) and [`promotionalOffer(id:)`](./purchaseoption/promotionaloffer%28id%29.md) to simulate customers redeeming the offers.
- Use [`purchaseDate(_:renewalBehavior:)`](./purchaseoption/purchasedate%28_,renewalbehavior%29.md) to control the transaction date and subscription renewal behavior.

## Topics

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](./purchaseoption/appaccounttoken%28_%29.md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](./purchaseoption/winbackoffer%28_%29.md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](./purchaseoption/promotionaloffer%28offerid,keyid,nonce,signature,timestamp%29.md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](./purchaseoption/promotionaloffer%28offerid,signature%29.md)
- [static func quantity(Int) -> Product.PurchaseOption](./purchaseoption/quantity%28_%29.md)
  Indicates the quantity of items the customer is purchasing.
### Specifying the behavior for storefront changes
- [static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool) -> Product.PurchaseOption](./purchaseoption/onstorefrontchange%28shouldcontinuepurchase%29.md)
  Indicates whether a transaction needs to continue if the App Store storefront changes on the device during the transaction.
### Specifying eligibility for an introductory offer
- [static func introductoryOfferEligibility(compactJWS: String) -> Product.PurchaseOption](./purchaseoption/introductoryoffereligibility%28compactjws%29.md)
  Set the eligibility of an introductory offer for a purchase.
### Setting options for StoreKit Testing in Xcode
- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](./purchaseoption/purchasedate%28_,renewalbehavior%29.md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [Product.PurchaseOption.SubscriptionRenewalBehavior](./purchaseoption/subscriptionrenewalbehavior.md)
  Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](./purchaseoption/codeoffer%28referencename%29.md)
  Sets an offer code for the transaction in the testing environment.
- [static func promotionalOffer(id: String) -> Product.PurchaseOption](./purchaseoption/promotionaloffer%28id%29.md)
  Sets a promotional offer for the transaction in the testing environment.
### Setting options for sandbox testing
- [static func simulatesAskToBuyInSandbox(Bool) -> Product.PurchaseOption](./purchaseoption/simulatesasktobuyinsandbox%28_%29.md)
  Simulates an Ask to Buy scenario when testing your app in the sandbox environment.
### Setting custom purchase options
- [static func custom(key: String, value: Data) -> Product.PurchaseOption](./purchaseoption/custom%28key,value%29-80cvh.md)
  Adds data for a custom key to a purchase.
- [static func custom(key: String, value: String) -> Product.PurchaseOption](./purchaseoption/custom%28key,value%29-3g3nc.md)
  Adds a string for a custom key to a purchase.
- [static func custom(key: String, value: Bool) -> Product.PurchaseOption](./purchaseoption/custom%28key,value%29-8tjim.md)
  Adds a Boolean value for a custom key to a purchase.
- [static func custom(key: String, value: Double) -> Product.PurchaseOption](./purchaseoption/custom%28key,value%29-7rju9.md)
  Adds a number for a custom key to a purchase.
### Type Methods
- [static func promotionalOffer(String, compactJWS: String) -> [Product.PurchaseOption]](./purchaseoption/promotionaloffer%28_,compactjws%29.md)
  Apply a promotional offer to a purchase.
- [static func billingPlanType(Product.SubscriptionInfo.BillingPlanType) -> Product.PurchaseOption](./purchaseoption/billingplantype%28_%29.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
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
- [Product.PurchaseResult](./purchaseresult.md)
  The result of a purchase.
- [Product.PurchaseError](./purchaseerror.md)
  Error information for product purchase errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption)*
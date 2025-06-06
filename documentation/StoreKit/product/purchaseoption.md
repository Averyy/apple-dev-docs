# Product.PurchaseOption

**Framework**: StoreKit  
**Kind**: struct

Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct PurchaseOption
```

## Mentions

- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md)

#### Overview

Associate purchase options with an in-app purchase when you call the methods to initiate a purchase, such as [`purchase(options:)`](product/purchase(options:).md) or [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-6dj6y.md). Use the testing-specific options with [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) or in the sandbox testing environment.

Purchase options enable you to provide additional information for the purchase, such as an app account token, promotional offer, win back offer, and quantity. You can also use purchase options to indicate how the transaction behaves if the storefront changes, and to indicate whether the transaction is eligible for an introductory offer.

> ❗ **Important**:  Purchases fail if a purchase option is invalid, and can result in the purchase method throwing a [`StoreKitError`](storekiterror.md) or [`Product.PurchaseError`](product/purchaseerror.md).

 Purchases fail if a purchase option is invalid, and can result in the purchase method throwing a [`StoreKitError`](storekiterror.md) or [`Product.PurchaseError`](product/purchaseerror.md).

##### Use Purchase Options During Testing

In the sandbox testing environment, use [`simulatesAskToBuyInSandbox(_:)`](product/purchaseoption/simulatesasktobuyinsandbox(_:).md) to test Ask To Buy scenarios.

In the Xcode testing environment with [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest), use the following testing-specific purchase options when you call [`buyProduct(identifier:options:)`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession/buyProduct(identifier:options:)):

- Use [`codeOffer(referenceName:)`](product/purchaseoption/codeoffer(referencename:).md) and [`promotionalOffer(id:)`](product/purchaseoption/promotionaloffer(id:).md) to simulate customers redeeming the offers.
- Use [`purchaseDate(_:renewalBehavior:)`](product/purchaseoption/purchasedate(_:renewalbehavior:).md) to control the transaction date and subscription renewal behavior.

## Topics

### Setting the purchase options
- [static func appAccountToken(UUID) -> Product.PurchaseOption](product/purchaseoption/appaccounttoken(_:).md)
  Sets a UUID to associate the purchase with an account in your system.
- [static func winBackOffer(Product.SubscriptionOffer) -> Product.PurchaseOption](product/purchaseoption/winbackoffer(_:).md)
  Sets a win-back offer to apply to the purchase.
- [static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:).md)
  Applies a promotional offer for an auto-renewable subscription.
- [static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(offerid:signature:).md)
- [static func quantity(Int) -> Product.PurchaseOption](product/purchaseoption/quantity(_:).md)
  Indicates the quantity of items the customer is purchasing.
### Specifying the behavior for storefront changes
- [static func onStorefrontChange(shouldContinuePurchase: (Storefront) -> Bool) -> Product.PurchaseOption](product/purchaseoption/onstorefrontchange(shouldcontinuepurchase:).md)
  Indicates whether a transaction needs to continue if the App Store storefront changes on the device during the transaction.
### Specifying eligibility for an introductory offer
- [static func introductoryOfferEligibility(compactJWS: String) -> Product.PurchaseOption](product/purchaseoption/introductoryoffereligibility(compactjws:).md)
  Set the eligibility of an introductory offer for a purchase.
### Setting options for StoreKit Testing in Xcode
- [static func purchaseDate(Date, renewalBehavior: Product.PurchaseOption.SubscriptionRenewalBehavior) -> Product.PurchaseOption](product/purchaseoption/purchasedate(_:renewalbehavior:).md)
  Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [Product.PurchaseOption.SubscriptionRenewalBehavior](product/purchaseoption/subscriptionrenewalbehavior.md)
  Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [static func codeOffer(referenceName: String) -> Product.PurchaseOption](product/purchaseoption/codeoffer(referencename:).md)
  Sets an offer code for the transaction in the testing environment.
- [static func promotionalOffer(id: String) -> Product.PurchaseOption](product/purchaseoption/promotionaloffer(id:).md)
  Sets a promotional offer for the transaction in the testing environment.
### Setting options for sandbox testing
- [static func simulatesAskToBuyInSandbox(Bool) -> Product.PurchaseOption](product/purchaseoption/simulatesasktobuyinsandbox(_:).md)
  Simulates an Ask to Buy scenario when testing your app in the sandbox environment.
### Setting custom purchase options
- [static func custom(key: String, value: Data) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-80cvh.md)
  Adds data for a custom key to a purchase.
- [static func custom(key: String, value: String) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-3g3nc.md)
  Adds a string for a custom key to a purchase.
- [static func custom(key: String, value: Bool) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-8tjim.md)
  Adds a Boolean value for a custom key to a purchase.
- [static func custom(key: String, value: Double) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-7rju9.md)
  Adds a number for a custom key to a purchase.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func purchase(options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(options:).md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: some UIScene, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-6dj6y.md)
  Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [func purchase(confirmIn: UIViewController, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-3bivf.md)
  Processes a purchase for the product.
- [func purchase(confirmIn: NSWindow, options: Set<Product.PurchaseOption>) async throws -> Product.PurchaseResult](product/purchase(confirmin:options:)-8eai6.md)
  Processes a purchase for the product.
- [Product.PurchaseResult](product/purchaseresult.md)
  The result of a purchase.
- [Product.PurchaseError](product/purchaseerror.md)
  Error information for product purchase errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption)*
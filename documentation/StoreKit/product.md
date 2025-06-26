# Product

**Framework**: StoreKit  
**Kind**: struct

Information about a product that you configure in App Store Connect.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Product
```

## Mentions

- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)
- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)

#### Overview

The `Product` type represents the in-app purchases that you configure in App Store Connect and make available for purchase within your app. Use `Product` to perform all product-related tasks in your app, from displaying in-app purchases and offers to making a purchase and getting transaction and subscription status information.

To get a `Product` instance, call [`products(for:)`](product/products(for:).md) and provide one or more in-app purchase product identifiers. Use a `Product` instance to display in-app purchases and subscription offers in your store, as follows:

- Show the localized name, description, and pricing information using [`displayName`](product/displayname.md), [`description`](product/description.md), and [`displayPrice`](product/displayprice.md), respectively.
- Determine whether a user is eligible for an introductory offer for the product using [`isEligibleForIntroOffer`](product/subscriptioninfo/iseligibleforintrooffer.md).
- Display your subscription offers using the subscription information in [`subscription`](product/subscription.md).

When users initiate a purchase, call [`purchase(options:)`](product/purchase(options:).md) or [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-3bivf.md) on the product instance. If your app uses SwiftUI, you can also use [`PurchaseAction`](purchaseaction.md). Set purchase options ([`Product.PurchaseOption`](product/purchaseoption.md)) to define an optional app account token, apply a promotional offer, or set a product quantity. Purchase options can also simulate an Ask to Buy scenario when you’re testing your app in the sandbox environment.

Use a `Product` instance to learn whether a user is entitled to a product by checking [`currentEntitlement`](product/currententitlement.md), which holds the transaction that entitles the user to the product. This transaction information, as well as the transaction in [`latestTransaction`](product/latesttransaction.md), are cryptographically signed by the App Store in JSON Web Signature (JWS) format.

If the product is an auto-renewable subscription, use the [`status`](product/subscriptioninfo/status-swift.property.md) and [`renewalInfo`](product/subscriptioninfo/status-swift.struct/renewalinfo.md) in the [`subscription`](product/subscription.md) information to help manage subscriptions and inform business decisions, such as presenting subscription offers.

For information about configuring In-App Purchases in App Store Connect, see [`Overview for configuring In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases).

## Topics

### Requesting products from the App Store
- [static func products<Identifiers>(for: Identifiers) async throws -> [Product]](product/products(for:).md)
  Requests product data from the App Store.
### Displaying a product description and price
- [let displayName: String](product/displayname.md)
  The localized display name of the product, if it exists.
- [let description: String](product/description.md)
  The localized description of the product.
- [let displayPrice: String](product/displayprice.md)
  The localized string representation of the product price, suitable for display.
- [let price: Decimal](product/price.md)
  The decimal representation of the cost of the product, in local currency.
- [var priceFormatStyle: Decimal.FormatStyle.Currency](product/priceformatstyle.md)
  The format style for the numbers in the price of the product.
- [var subscriptionPeriodFormatStyle: Date.ComponentsFormatStyle](product/subscriptionperiodformatstyle.md)
  The format style for the date components related to a subscription’s duration.
- [var subscriptionPeriodUnitFormatStyle: Product.SubscriptionPeriod.Unit.FormatStyle](product/subscriptionperiodunitformatstyle.md)
  The format style for subscription period units, such as week, month, or year.
### Purchasing a product
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
- [Product.PurchaseError](product/purchaseerror.md)
  Error information for product purchase errors.
### Receiving current entitlement information
- [var currentEntitlement: VerificationResult<Transaction>?](product/currententitlement.md)
  The transaction that entitles the user to the product.
### Getting the latest transaction
- [var latestTransaction: VerificationResult<Transaction>?](product/latesttransaction.md)
  The most recent transaction for the product.
### Getting subscription information
- [let subscription: Product.SubscriptionInfo?](product/subscription.md)
  The subscription information for an auto-renewable subscripton.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [Product.SubscriptionPeriod](product/subscriptionperiod.md)
  Values that represent the duration of time between subscription renewals.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
### Getting product identifiers and type
- [let id: String](product/id.md)
  The unique product identifier.
- [let type: Product.ProductType](product/type.md)
  The in-app purchase product type.
- [Product.ProductType](product/producttype.md)
  The types of in-app purchases.
### Getting Family Sharing status
- [let isFamilyShareable: Bool](product/isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
### Managing promoted in-app purchases
- [Product.PromotionInfo](product/promotioninfo.md)
  Information about a promoted In-App Purchase that customizes its order and visibility on the device.
### Loading products
- [Product.CollectionTaskState](product/collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.
- [Product.TaskState](product/taskstate.md)
  The state of a task that loads a product in the background.
### Getting product info in JSON format
- [var jsonRepresentation: Data](product/jsonrepresentation.md)
  The JSON representation of the product information.
### Getting subscription relationship
- [Product.SubscriptionRelationship](product/subscriptionrelationship.md)
### Instance Properties
- [var currentEntitlements: Transaction.Transactions](product/currententitlements.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md)
  Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [typealias SubscriptionInfo](subscriptioninfo.md)
  Information about an auto-renewable subscription.
- [typealias SubscriptionStatus](subscriptionstatus.md)
  Represents the renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product)*
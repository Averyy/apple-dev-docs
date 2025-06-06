# SKProduct

**Framework**: StoreKit  
**Kind**: class

Information about a registered product in App Store Connect.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKProduct
```

## Mentions

- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md)

#### Overview

[`SKProduct`](skproduct.md) objects are returned as part of an [`SKProductsResponse`](skproductsresponse.md) object.

## Topics

### Getting the Product Identifier
- [var productIdentifier: String](skproduct/productidentifier.md)
  The string that identifies the product to the Apple App Store.
### Getting Product Attributes
- [var localizedDescription: String](skproduct/localizeddescription.md)
  A description of the product.
- [var localizedTitle: String](skproduct/localizedtitle.md)
  The name of the product.
- [var contentVersion: String](skproduct/contentversion.md)
  A string that identifies the version of the content.
- [var isFamilyShareable: Bool](skproduct/isfamilyshareable.md)
  A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.
- [var contentLengths: [NSNumber]](skproduct/contentlengths.md)
  The total size of the content, in bytes.
### Getting Pricing Information
- [var price: NSDecimalNumber](skproduct/price.md)
  The cost of the product in the local currency.
- [var priceLocale: Locale](skproduct/pricelocale.md)
  The locale used to format the price of the product.
- [var introductoryPrice: SKProductDiscount?](skproduct/introductoryprice.md)
  The object containing introductory price information for the product.
- [var discounts: [SKProductDiscount]](skproduct/discounts.md)
  An array of subscription offers available for the auto-renewable subscription.
- [class SKProductDiscount](skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.
### Getting Subscription Information
- [var subscriptionGroupIdentifier: String?](skproduct/subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [var subscriptionPeriod: SKProductSubscriptionPeriod?](skproduct/subscriptionperiod.md)
  The period details for products that are subscriptions.
- [class SKProductSubscriptionPeriod](skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.
### Getting Downloadable Content Information
- [var isDownloadable: Bool](skproduct/isdownloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.
- [var downloadContentLengths: [NSNumber]](skproduct/downloadcontentlengths.md)
  The lengths of the downloadable files available for this product.
- [var downloadContentVersion: String](skproduct/downloadcontentversion.md)
  A string that identifies which version of the content is available for download.
- [var downloadable: Bool](skproduct/downloadable.md)
  A Boolean value that indicates whether the App Store has downloadable content for this product.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md)
  Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
  Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [class SKProductsRequest](skproductsrequest.md)
  An object that can retrieve localized information from the App Store about a specified list of products.
- [class SKProductsResponse](skproductsresponse.md)
  An App Store response to a request for information about a list of products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct)*
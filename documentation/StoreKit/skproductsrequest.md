# SKProductsRequest

**Framework**: StoreKit  
**Kind**: class

An object that can retrieve localized information from the App Store about a specified list of products.

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
class SKProductsRequest
```

## Mentions

- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md)
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Testing a product request](testing-a-product-request.md)

#### Overview

Your app uses an [`SKProductsRequest`](skproductsrequest.md) object to present localized prices and other information to the user without having to maintain that list of product information itself.

To use an [`SKProductsRequest`](skproductsrequest.md) object, you initialize it with a list of product identifier strings, attach a delegate, and then call the request’s [`start()`](skrequest/start().md) method. When the request completes, your delegate receives an [`SKProductsResponse`](skproductsresponse.md) object.

> **Note**:  Be sure to keep a strong reference to the request object; otherwise, the system might deallocate the request before it can complete.

## Topics

### Initializing a Products Request
- [init(productIdentifiers: Set<String>)](skproductsrequest/init(productidentifiers:).md)
  Initializes the request with the set of product identifiers.
### Setting the Delegate
- [var delegate: (any SKProductsRequestDelegate)?](skproductsrequest/delegate.md)
  The delegate that receives the response of the app’s products request.
- [protocol SKProductsRequestDelegate](skproductsrequestdelegate.md)
  A set of methods the delegate implements so it receives the product information your app requests.

## Relationships

### Inherits From
- [SKRequest](skrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md)
  Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
  Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [class SKProductsResponse](skproductsresponse.md)
  An App Store response to a request for information about a list of products.
- [class SKProduct](skproduct.md)
  Information about a registered product in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsrequest)*
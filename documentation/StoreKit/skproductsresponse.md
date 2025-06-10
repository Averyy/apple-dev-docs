# SKProductsResponse

**Framework**: StoreKit  
**Kind**: class

An App Store response to a request for information about a list of products.

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
class SKProductsResponse
```

## Topics

### Response Information
- [var products: [SKProduct]](skproductsresponse/products.md)
  A list of products, one product for each valid product identifier provided in the original request.
- [var invalidProductIdentifiers: [String]](skproductsresponse/invalidproductidentifiers.md)
  An array of product identifier strings that the App Store doesn’t recognize.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md)
  Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
  Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [class SKProductsRequest](skproductsrequest.md)
  An object that can retrieve localized information from the App Store about a specified list of products.
- [class SKProduct](skproduct.md)
  Information about a registered product in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsresponse)*
# invalidProductIdentifiers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An array of product identifier strings that the App Store doesn’t recognize.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Get products using Product.products(for:).

## Declaration

```swift
var invalidProductIdentifiers: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * invalidProductIdentifiers;
```

## Mentions

- [Fetching product information from the App Store](../fetching-product-information-from-the-app-store.md)

#### Discussion

The App Store may not recognize your product identifiers unless you meet following criteria, as applicable:

- Agree to the latest Apple Developer Program License Agreement.
- Complete all the financial agreements as described in the [Agreements, Tax, and Banking Overview](https://help.apple.com/itunes-connect/developer/#/devb6df5ee51). When you renew your developer membership, see if you need to make updates to your agreements. When your developer membership expires, your financial agreements expire as well.
- Your app uses an explicit App ID.
- Clear the Apple In-App Purchases for sale in App Store Connect. See [Set availability for Apple In-App Purchase](https://help.apple.com/app-store-connect/#/dev360aba524).
- Modified Apple In-App Purchases are available to the App Store servers.
- The product identifier specified in App Store Connect matches the identifier used by the [`SKProductsRequest`](../skproductsrequest.md) object in your app.
- Upload the content of your product to App Store Connect.  See [Upload Apple In-App Purchase content to App Store Connect](https://help.apple.com/xcode/mac/current/#/dev285fb60ce).

For more troubleshooting information, see [Fetching product information from the App Store](../fetching-product-information-from-the-app-store.md).

## See Also

### Response Information
- [var products: [SKProduct]](./products.md)
  A list of products, one product for each valid product identifier provided in the original request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsresponse/invalidproductidentifiers)*
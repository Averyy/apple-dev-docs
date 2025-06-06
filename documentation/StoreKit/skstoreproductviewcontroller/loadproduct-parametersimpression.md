# loadProduct(parameters:impression:)

**Framework**: StoreKit  
**Kind**: method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
@preconcurrency func loadProduct(parameters: [String : Any], impression: AppImpression) async throws
```

## See Also

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [func loadProduct(withParameters: [String : Any], completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md)
  Loads a new product screen to display.
- [func loadProduct(withParameters: [String : Any], impression: SKAdImpression, completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression, reengagementURL: URL) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:reengagementurl:).md)
- [Product Dictionary Keys](product-dictionary-keys.md)
  Keys for identifying products and the tokens for affiliates and campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/loadproduct(parameters:impression:))*
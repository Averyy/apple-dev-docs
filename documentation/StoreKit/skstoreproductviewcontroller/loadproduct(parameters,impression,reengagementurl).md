# loadProduct(parameters:impression:reengagementURL:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func loadProduct(parameters: [String : Any], impression: AppImpression, reengagementURL: URL) async throws
```

## See Also

### Loading a new product screen
- [Offering media for sale in your app](../offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [func loadProduct(withParameters: [String : Any], completionBlock: ((Bool, (any Error)?) -> Void)?)](./loadproduct%28withparameters,completionblock%29.md)
  Loads a new product screen to display.
- [func loadProduct(withParameters: [String : Any], impression: SKAdImpression, completionBlock: ((Bool, (any Error)?) -> Void)?)](./loadproduct%28withparameters,impression,completionblock%29.md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression) async throws](./loadproduct%28parameters,impression%29.md)
- [Product Dictionary Keys](../product-dictionary-keys.md)
  Keys for identifying products and the tokens for affiliates and campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/loadproduct(parameters:impression:reengagementurl:))*
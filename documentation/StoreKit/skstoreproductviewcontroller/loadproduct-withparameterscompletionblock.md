# loadProduct(withParameters:completionBlock:)

**Framework**: StoreKit  
**Kind**: method

Loads a new product screen to display.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
func loadProduct(withParameters parameters: [String : Any]) async throws -> Bool
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Signing and providing ads](signing-and-providing-ads.md)

#### Discussion

For a seamless user experience, load the product information before presenting the [`SKStoreProductViewController`](skstoreproductviewcontroller.md) view controller. However, if you load the product information while presenting the view controller, once loaded, the product data replaces the contents of the view controller.

## Parameters

- `parameters`: A dictionary describing the content you want the view controller to display. See   for keys that describe the product. See   for keys that describe an impression in an advertising campaign.
- `block`: A block to be called when the product information has been loaded from the App Store. The completion block is called on the main thread and receives the following parameters:

## See Also

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [func loadProduct(withParameters: [String : Any], impression: SKAdImpression, completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression, reengagementURL: URL) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:reengagementurl:).md)
- [Product Dictionary Keys](product-dictionary-keys.md)
  Keys for identifying products and the tokens for affiliates and campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/loadproduct(withparameters:completionblock:))*
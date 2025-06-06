# Product Dictionary Keys

**Framework**: StoreKit

Keys for identifying products and the tokens for affiliates and campaigns.

#### Overview

These dictionary keys are used in the parameter for the [`loadProduct(withParameters:completionBlock:)`](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md) method.

The [`SKStoreProductParameterITunesItemIdentifier`](skstoreproductparameteritunesitemidentifier.md) key represents the product to display, and is always required. Other keys provide optional affiliate or promoted product information.

Learn more about the Affiliate Program at [`https://apple.com/itunes/affiliates`](https://developer.apple.comhttps://apple.com/itunes/affiliates).

## Topics

### Required Key
- [let SKStoreProductParameterITunesItemIdentifier: String](skstoreproductparameteritunesitemidentifier.md)
  The key representing the iTunes identifier for the item you want the store to display when the view controller is presented.
### Affiliate and Analytics Keys
- [let SKStoreProductParameterProductIdentifier: String](skstoreproductparameterproductidentifier.md)
  The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [let SKStoreProductParameterAdvertisingPartnerToken: String](skstoreproductparameteradvertisingpartnertoken.md)
  The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterAffiliateToken: String](skstoreproductparameteraffiliatetoken.md)
  The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterCampaignToken: String](skstoreproductparametercampaigntoken.md)
  The key representing an App Analytics campaign.
- [let SKStoreProductParameterProviderToken: String](skstoreproductparameterprovidertoken.md)
  The key representing the provider token for the developer that created the app specified by the [`SKStoreProductParameterITunesItemIdentifier`](skstoreproductparameteritunesitemidentifier.md) key.
- [let SKStoreProductParameterCustomProductPageIdentifier: String](skstoreproductparametercustomproductpageidentifier.md)
  The key that represents the custom product page identifier you want the store to display when you present the view controller.

## See Also

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [func loadProduct(withParameters: [String : Any], completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md)
  Loads a new product screen to display.
- [func loadProduct(withParameters: [String : Any], impression: SKAdImpression, completionBlock: ((Bool, (any Error)?) -> Void)?)](skstoreproductviewcontroller/loadproduct(withparameters:impression:completionblock:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:).md)
- [func loadProduct(parameters: [String : Any], impression: AppImpression, reengagementURL: URL) async throws](skstoreproductviewcontroller/loadproduct(parameters:impression:reengagementurl:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product-dictionary-keys)*
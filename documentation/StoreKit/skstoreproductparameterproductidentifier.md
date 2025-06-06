# SKStoreProductParameterProductIdentifier

**Framework**: StoreKit  
**Kind**: var

The key representing the product identifier for the promoted product you want the store to display at the top of the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 11.0+

## Declaration

```swift
let SKStoreProductParameterProductIdentifier: String
```

#### Discussion

The value for this key is an instance of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString).

When your app uses an [`SKStoreProductViewController`](skstoreproductviewcontroller.md) to render an app page for another app, you can optionally choose to highlight an in-app purchase by displaying it at the top of the store page.  Set  [`SKStoreProductParameterProductIdentifier`](skstoreproductparameterproductidentifier.md) to the identifier of the product you want displayed at the top of the page.

The product indicated by the identifier must be set up as a promoted product in the App Store, otherwise the identifier is ignored. See [`Promoting In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html#//apple_ref/doc/uid/TP40008267-CH11).

> **Note**:  Use the same product identifiers as used in the [`productIdentifier`](skproduct/productidentifier.md) variable in the [`SKProduct`](skproduct.md) class.

 Use the same product identifiers as used in the [`productIdentifier`](skproduct/productidentifier.md) variable in the [`SKProduct`](skproduct.md) class.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameterproductidentifier)*
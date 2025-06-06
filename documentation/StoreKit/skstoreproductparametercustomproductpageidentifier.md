# SKStoreProductParameterCustomProductPageIdentifier

**Framework**: StoreKit  
**Kind**: var

The key that represents the custom product page identifier you want the store to display when you present the view controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
let SKStoreProductParameterCustomProductPageIdentifier: String
```

#### Discussion

The value for this key is a UUID that represents a custom product page. Get this value from the `ppid` parameter of your custom product page’s URL. For example, in the following sample custom product page URL:

`https://apps.apple.com/us/app/example-appname/id1234567890?ppid=eb2b3606-2fef-4aab-a54e-b2e5547c9bc3`

- the custom product page identifier is the string that follows `ppid=`, which is `eb2b3606-2fef-4aab-a54e-b2e5547c9bc3`.

App Store Connect creates the URL when you configure your custom product page. For more information, see [`Create custom product pages`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions/).

For more information about custom product pages, see [`Custom product pages on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/custom-product-pages/).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparametercustomproductpageidentifier)*
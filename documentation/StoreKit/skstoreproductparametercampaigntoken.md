# SKStoreProductParameterCampaignToken

**Framework**: StoreKit  
**Kind**: var

The key representing an App Analytics campaign.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
let SKStoreProductParameterCampaignToken: String
```

#### Discussion

The value for this key is an instance of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), containing any 40-byte string.

This token allows you to track the effectiveness of your Affiliate Program link and your App Analytics campaign.

For more information about the Affiliate Program, see the Affiliate Program at [`https://apple.com/itunes/affiliates`](https://developer.apple.comhttps://apple.com/itunes/affiliates). For more information about App Store Connect Analytics, see [`App Store Connect Developer Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/About.html#//apple_ref/doc/uid/TP40011225).

## See Also

- [let SKStoreProductParameterProductIdentifier: String](skstoreproductparameterproductidentifier.md)
  The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [let SKStoreProductParameterAdvertisingPartnerToken: String](skstoreproductparameteradvertisingpartnertoken.md)
  The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterAffiliateToken: String](skstoreproductparameteraffiliatetoken.md)
  The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterProviderToken: String](skstoreproductparameterprovidertoken.md)
  The key representing the provider token for the developer that created the app specified by the [`SKStoreProductParameterITunesItemIdentifier`](skstoreproductparameteritunesitemidentifier.md) key.
- [let SKStoreProductParameterCustomProductPageIdentifier: String](skstoreproductparametercustomproductpageidentifier.md)
  The key that represents the custom product page identifier you want the store to display when you present the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparametercampaigntoken)*
# SKStoreProductParameterAffiliateToken

**Framework**: StoreKit  
**Kind**: var

The key representing the affiliate identifier you wish to use for any purchase made through the view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
let SKStoreProductParameterAffiliateToken: String
```

#### Discussion

The value for this key is an instance of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString).

You receive an affiliate identifier when you sign up for the Affiliate Program. The affiliate associated with this view controller is paid a commission for any items purchased using the controller.

Learn more about the Affiliate Program at [`https://apple.com/itunes/affiliates`](https://developer.apple.comhttps://apple.com/itunes/affiliates).

## See Also

- [let SKStoreProductParameterProductIdentifier: String](skstoreproductparameterproductidentifier.md)
  The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [let SKStoreProductParameterAdvertisingPartnerToken: String](skstoreproductparameteradvertisingpartnertoken.md)
  The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterCampaignToken: String](skstoreproductparametercampaigntoken.md)
  The key representing an App Analytics campaign.
- [let SKStoreProductParameterProviderToken: String](skstoreproductparameterprovidertoken.md)
  The key representing the provider token for the developer that created the app specified by the [`SKStoreProductParameterITunesItemIdentifier`](skstoreproductparameteritunesitemidentifier.md) key.
- [let SKStoreProductParameterCustomProductPageIdentifier: String](skstoreproductparametercustomproductpageidentifier.md)
  The key that represents the custom product page identifier you want the store to display when you present the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteraffiliatetoken)*
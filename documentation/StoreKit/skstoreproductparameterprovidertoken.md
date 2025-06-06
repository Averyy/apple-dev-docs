# SKStoreProductParameterProviderToken

**Framework**: StoreKit  
**Kind**: var

The key representing the provider token for the developer that created the app specified by the [`SKStoreProductParameterITunesItemIdentifier`](skstoreproductparameteritunesitemidentifier.md) key.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.0+
- macOS 11.0+

## Declaration

```swift
let SKStoreProductParameterProviderToken: String
```

#### Discussion

The value for this key is an instance of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString).

Use your own provider token when cross promoting your own apps. This token lets you track the effectiveness of the cross promotion effort separate from any affiliate campaign that shares the same campaign token.

When promoting apps for other developers, use their provider token instead. In this case, the token lets the developer track the effectiveness of your App Analytics campaign for their apps.

The key must be used in combination with your campaign token, [`SKStoreProductParameterCampaignToken`](skstoreproductparametercampaigntoken.md). For more information, see [`App Store Connect Developer Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/About.html#//apple_ref/doc/uid/TP40011225).

## See Also

- [let SKStoreProductParameterProductIdentifier: String](skstoreproductparameterproductidentifier.md)
  The key representing the product identifier for the promoted product you want the store to display at the top of the page.
- [let SKStoreProductParameterAdvertisingPartnerToken: String](skstoreproductparameteradvertisingpartnertoken.md)
  The key representing the advertising partner you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterAffiliateToken: String](skstoreproductparameteraffiliatetoken.md)
  The key representing the affiliate identifier you wish to use for any purchase made through the view controller.
- [let SKStoreProductParameterCampaignToken: String](skstoreproductparametercampaigntoken.md)
  The key representing an App Analytics campaign.
- [let SKStoreProductParameterCustomProductPageIdentifier: String](skstoreproductparametercustomproductpageidentifier.md)
  The key that represents the custom product page identifier you want the store to display when you present the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameterprovidertoken)*
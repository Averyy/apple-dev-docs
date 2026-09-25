# InAppPurchaseLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single In-App Purchase localization.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseLocalizationResponse
```

## Properties

- `data` (InAppPurchaseLocalization) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (DocumentLinks) *(required)*

## See Also

- [object InAppPurchaseV2Response](inapppurchasev2response.md)
  A response containing a single In-App Purchase configured via the v2 API.
- [object InAppPurchasesV2Response](inapppurchasesv2response.md)
  A response containing a list of In-App Purchases configured via the v2 API.
- [object InAppPurchaseV2](inapppurchasev2.md)
  An In-App Purchase item configured via the v2 API, supporting both consumable and non-consumable types.
- [object InAppPurchaseV2CreateRequest](inapppurchasev2createrequest.md)
  The request body you use to create an In-App Purchase.
- [object InAppPurchaseV2UpdateRequest](inapppurchasev2updaterequest.md)
  The request body you use to update an In-App Purchase v2 update request.
- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an In-App Purchase.
- [object InAppPurchasePricePointsResponse](inapppurchasepricepointsresponse.md)
  The response body for endpoints that list available price points for an In-App Purchase.
- [object InAppPurchasePricePoint](inapppurchasepricepoint.md)
  A standard price tier for In-App Purchases, specifying the customer price and developer proceeds in a territory.
- [object InAppPurchasePricesResponse](inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an In-App Purchase.
- [object InAppPurchasePrice](inapppurchaseprice.md)
  A configured price for an In-App Purchase in a specific App Store territory.
- [object InAppPurchasePriceInlineCreate](inapppurchasepriceinlinecreate.md)
  An inline object for specifying a territory-specific price when creating or updating an In-App Purchase price schedule.
- [object AppInAppPurchasesLinkagesResponse](appinapppurchaseslinkagesresponse.md)
- [object AppInAppPurchasesV2LinkagesResponse](appinapppurchasesv2linkagesresponse.md)
- [object InAppPurchasePricePointEqualizationsLinkagesResponse](inapppurchasepricepointequalizationslinkagesresponse.md)
- [object InAppPurchaseV2AppStoreReviewScreenshotLinkageResponse](inapppurchasev2appstorereviewscreenshotlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationresponse)*
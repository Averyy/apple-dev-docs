# InAppPurchaseV2CreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseV2CreateRequest
```

## Topics

### Objects
- [object InAppPurchaseV2CreateRequest.Data](inapppurchasev2createrequest/data-data.dictionary.md)
  The request body you use to create an in-app purchase.

## Properties

- `data` (InAppPurchaseV2CreateRequest.Data) *(required)*

## See Also

- [object InAppPurchaseV2Response](inapppurchasev2response.md)
  A response containing a single in-app purchase configured via the v2 API.
- [object InAppPurchasesV2Response](inapppurchasesv2response.md)
  A response containing a list of in-app purchases configured via the v2 API.
- [object InAppPurchaseV2](inapppurchasev2.md)
  An in-app purchase item configured via the v2 API, supporting both consumable and non-consumable types.
- [object InAppPurchaseV2UpdateRequest](inapppurchasev2updaterequest.md)
  The request body you use to update an in-app purchase v2update request.
- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an in-app purchase.
- [object InAppPurchaseLocalizationResponse](inapppurchaselocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single in-app purchase localization.
- [object InAppPurchasePricePointsResponse](inapppurchasepricepointsresponse.md)
  The response body for endpoints that list available price points for an in-app purchase.
- [object InAppPurchasePricePoint](inapppurchasepricepoint.md)
  A standard price tier for in-app purchases, specifying the customer price and developer proceeds in a territory.
- [object InAppPurchasePricesResponse](inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an in-app purchase.
- [object InAppPurchasePrice](inapppurchaseprice.md)
  A configured price for an in-app purchase in a specific App Store territory.
- [object InAppPurchasePriceInlineCreate](inapppurchasepriceinlinecreate.md)
  An inline object for specifying a territory-specific price when creating or updating an in-app purchase price schedule.
- [object AppInAppPurchasesLinkagesResponse](appinapppurchaseslinkagesresponse.md)
- [object AppInAppPurchasesV2LinkagesResponse](appinapppurchasesv2linkagesresponse.md)
- [object InAppPurchasePricePointEqualizationsLinkagesResponse](inapppurchasepricepointequalizationslinkagesresponse.md)
- [object InAppPurchaseV2AppStoreReviewScreenshotLinkageResponse](inapppurchasev2appstorereviewscreenshotlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasev2createrequest)*
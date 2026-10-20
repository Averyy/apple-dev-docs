# InAppPurchaseVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create or read an In-App Purchase version.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```
object InAppPurchaseVersionResponse
```

## Properties

- `data` (InAppPurchaseVersion) *(required)*
- `included` ([*]): **Allowed Types**: `InAppPurchaseImageV2`, `InAppPurchaseLocalizationV2`, `InAppPurchaseV2`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object InAppPurchaseVersion](./inapppurchaseversion.md)
  A draft version of an In-App Purchase that captures its localized metadata and review images for App Review submission.
- [object InAppPurchaseVersionCreateRequest](./inapppurchaseversioncreaterequest.md)
  The request body you use to create a draft version of an In-App Purchase.
- [object InAppPurchaseVersionImageLinkageResponse](./inapppurchaseversionimagelinkageresponse.md)
  A response containing the resource identifier of the review image for an In-App Purchase version.
- [object InAppPurchaseVersionImagesLinkagesResponse](./inapppurchaseversionimageslinkagesresponse.md)
  A response containing the resource identifiers of the review images for an In-App Purchase version.
- [object InAppPurchaseVersionLocalizationsLinkagesResponse](./inapppurchaseversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of the localizations for an In-App Purchase version.
- [object InAppPurchaseVersionsResponse](./inapppurchaseversionsresponse.md)
  The response body for endpoints that list In-App Purchase versions.
- [object InAppPurchaseV2VersionsLinkagesResponse](./inapppurchasev2versionslinkagesresponse.md)
  A response containing the resource identifiers of the versions of an In-App Purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseversionresponse)*
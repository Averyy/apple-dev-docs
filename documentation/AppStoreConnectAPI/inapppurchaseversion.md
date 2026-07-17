# InAppPurchaseVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

A draft version of an in-app purchase that captures its localized metadata and review images for App Review submission.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object InAppPurchaseVersion
```

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)

## Topics

### Objects and types
- [object InAppPurchaseVersion.Attributes](inapppurchaseversion/attributes-data.dictionary.md)
  Attributes that describe an in-app purchase version resource.
- [object InAppPurchaseVersion.Relationships](inapppurchaseversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (InAppPurchaseVersion.Attributes)
- `relationships` (InAppPurchaseVersion.Relationships)
- `links` (ResourceLinks)

## See Also

- [object InAppPurchaseVersionCreateRequest](inapppurchaseversioncreaterequest.md)
  The request body you use to create a draft version of an in-app purchase.
- [object InAppPurchaseVersionImageLinkageResponse](inapppurchaseversionimagelinkageresponse.md)
  A response containing the resource identifier of the review image for an in-app purchase version.
- [object InAppPurchaseVersionImagesLinkagesResponse](inapppurchaseversionimageslinkagesresponse.md)
  A response containing the resource identifiers of the review images for an in-app purchase version.
- [object InAppPurchaseVersionLocalizationsLinkagesResponse](inapppurchaseversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of the localizations for an in-app purchase version.
- [object InAppPurchaseVersionResponse](inapppurchaseversionresponse.md)
  The response body for endpoints that create or read an in-app purchase version.
- [object InAppPurchaseVersionsResponse](inapppurchaseversionsresponse.md)
  The response body for endpoints that list in-app purchase versions.
- [object InAppPurchaseV2VersionsLinkagesResponse](inapppurchasev2versionslinkagesresponse.md)
  A response containing the resource identifiers of the versions of an in-app purchase configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseversion)*
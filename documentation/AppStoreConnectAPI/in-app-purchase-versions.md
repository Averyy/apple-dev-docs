# In-App Purchase Versions

**Framework**: App Store Connect API

Create and read draft versions of an in-app purchase, with their localized metadata and review images.

#### Overview

Each in-app purchase has a version, which is the container for the localizations and images related to that in-app purchase. Use the in-app purchase version for submitting to review.

## Topics

### Endpoints
- [Create an in-app purchase version](post-v1-inapppurchaseversions.md)
  Create a draft version of an in-app purchase, capturing its current localized metadata and review images for App Review submission.
- [Read in-app purchase version information](get-v1-inapppurchaseversions-_id_.md)
  Get information about a specific draft version of an in-app purchase.
- [Read the image for an in-app purchase version](get-v1-inapppurchaseversions-_id_-image.md)
  Get the review image attached to a draft version of an in-app purchase.
- [List images for an in-app purchase version](get-v1-inapppurchaseversions-_id_-images.md)
  List the review images attached to a draft version of an in-app purchase.
- [List localizations for an in-app purchase version](get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an in-app purchase.
- [Read the image ID for an in-app purchase version](get-v1-inapppurchaseversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an in-app purchase.
- [List image IDs for an in-app purchase version](get-v1-inapppurchaseversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an in-app purchase.
- [List localization IDs for an in-app purchase version](get-v1-inapppurchaseversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an in-app purchase.
- [List the versions of an in-app purchase](get-v2-inapppurchases-_id_-versions.md)
  List the draft versions of an in-app purchase configured with the v2 API.
- [Get the resource IDs of the versions of an in-app purchase](get-v2-inapppurchases-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of an in-app purchase configured with the v2 API.
### Objects
- [object InAppPurchaseVersion](inapppurchaseversion.md)
  A draft version of an in-app purchase that captures its localized metadata and review images for App Review submission.
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

## See Also

- [Managing in-app purchases](managing-in-app-purchases.md)
  Create in-app purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with in-app purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an in-app purchase’s localized metadata and review images before submitting for App Review.
- [Migrating in-app purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchase versions.
- [In-app purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for in-app purchases.
- [In-App purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.
- [In-app purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an in-app purchase.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for in-app purchases.
- [In-app purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-versions)*
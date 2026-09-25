# In-App Purchase Versions

**Framework**: App Store Connect API

Create and read draft versions of an In-App Purchase, with their localized metadata and review images.

#### Overview

Each In-App Purchase has a version, which is the container for the localizations and images related to that In-App Purchase. Use the In-App Purchase version for submitting to review.

## Topics

### Endpoints
- [Create an In-App Purchase version](post-v1-inapppurchaseversions.md)
  Create a draft version of an In-App Purchase, capturing its current localized metadata and review images for App Review submission.
- [Read In-App Purchase version information](get-v1-inapppurchaseversions-_id_.md)
  Get information about a specific draft version of an In-App Purchase.
- [Read the image for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-image.md)
  Get the review image attached to a draft version of an In-App Purchase.
- [List images for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-images.md)
  List the review images attached to a draft version of an In-App Purchase.
- [List localizations for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an In-App Purchase.
- [Read the image ID for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-image.md)
  Get the related resource ID for the review image attached to a draft version of an In-App Purchase.
- [List image IDs for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-images.md)
  Get the related resource IDs for the review images attached to a draft version of an In-App Purchase.
- [List localization IDs for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of an In-App Purchase.
- [List the versions of an In-App Purchase](get-v2-inapppurchases-_id_-versions.md)
  List the draft versions of an In-App Purchase configured with the v2 API.
- [Get the resource IDs of the versions of an In-App Purchase](get-v2-inapppurchases-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of an In-App Purchase configured with the v2 API.
### Objects
- [object InAppPurchaseVersion](inapppurchaseversion.md)
  A draft version of an In-App Purchase that captures its localized metadata and review images for App Review submission.
- [object InAppPurchaseVersionCreateRequest](inapppurchaseversioncreaterequest.md)
  The request body you use to create a draft version of an In-App Purchase.
- [object InAppPurchaseVersionImageLinkageResponse](inapppurchaseversionimagelinkageresponse.md)
  A response containing the resource identifier of the review image for an In-App Purchase version.
- [object InAppPurchaseVersionImagesLinkagesResponse](inapppurchaseversionimageslinkagesresponse.md)
  A response containing the resource identifiers of the review images for an In-App Purchase version.
- [object InAppPurchaseVersionLocalizationsLinkagesResponse](inapppurchaseversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of the localizations for an In-App Purchase version.
- [object InAppPurchaseVersionResponse](inapppurchaseversionresponse.md)
  The response body for endpoints that create or read an In-App Purchase version.
- [object InAppPurchaseVersionsResponse](inapppurchaseversionsresponse.md)
  The response body for endpoints that list In-App Purchase versions.
- [object InAppPurchaseV2VersionsLinkagesResponse](inapppurchasev2versionslinkagesresponse.md)
  A response containing the resource identifiers of the versions of an In-App Purchase configured with the v2 API.

## See Also

- [Managing In-App Purchases](managing-in-app-purchases.md)
  Create In-App Purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with In-App Purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an In-App Purchase’s localized metadata and review images before submitting for App Review.
- [Migrating In-App Purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete In-App Purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for In-App Purchase versions.
- [In-App Purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for In-App Purchases.
- [In-App Purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.
- [In-App Purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an In-App Purchase.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-versions)*
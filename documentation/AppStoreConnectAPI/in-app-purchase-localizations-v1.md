# In-App Purchase localizations (v1)

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for In-App Purchases.

**Availability**:
- App Store Connect API 2.0+

#### Overview

> ❗ **Important**:  This is deprecated. Use [`In-App Purchase Localizations`](in-app-purchase-localizations.md) instead.

## Topics

### Endpoints
- [List all localizations for an In-App Purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific In-App Purchase.
- [Create an In-App Purchase localization (v1)](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase.
- [Read In-App Purchase localization information (v1)](get-v1-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale for an In-App Purchase.
- [Modify an In-App Purchase localization (v1)](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase.
- [Delete an In-App Purchase localization (v1)](delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single In-App Purchase localization.
### Objects
- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an In-App Purchase.
- [object InAppPurchaseContent](inapppurchasecontent.md)
  Hosted downloadable content associated with a non-consumable In-App Purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an In-App Purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an In-App Purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an In-App Purchase.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an In-App Purchase shown to customers in a specific language.

## See Also

- [Managing In-App Purchases](managing-in-app-purchases.md)
  Create In-App Purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with In-App Purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an In-App Purchase’s localized metadata and review images before submitting for App Review.
- [Migrating In-App Purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an In-App Purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete In-App Purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for In-App Purchase versions.
- [In-App Purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.
- [In-App Purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an In-App Purchase.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-localizations-v1)*
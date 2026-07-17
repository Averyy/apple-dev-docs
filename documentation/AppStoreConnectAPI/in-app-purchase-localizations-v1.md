# In-app purchase localizations (v1)

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for in-app purchases.

**Availability**:
- App Store Connect API 2.0+

#### Overview

> ❗ **Important**:  This is deprecated. Use [`In-App Purchase Localizations`](in-app-purchase-localizations.md) instead.

## Topics

### Endpoints
- [List all localizations for an in-app purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific in-app purchase.
- [Create an in-app purchase localization (v1)](post-v1-inapppurchaselocalizations.md)
  Create a localized display name and description for an in-app purchase.
- [Read in-app purchase localization information (v1)](get-v1-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale for an in-app purchase.
- [Modify an in-app purchase localization (v1)](patch-v1-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an in-app purchase.
- [Delete an in-app purchase localization (v1)](delete-v1-inapppurchaselocalizations-_id_.md)
  Delete the metadata for a single in-app purchase localization.
### Objects
- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an in-app purchase.
- [object InAppPurchaseContent](inapppurchasecontent.md)
  Hosted downloadable content associated with a non-consumable in-app purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an in-app purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an in-app purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an in-app purchase.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an in-app purchase shown to customers in a specific language.

## See Also

- [Managing in-app purchases](managing-in-app-purchases.md)
  Create in-app purchases, configure their metadata and pricing, submit them for review, and promote them with the App Store Connect API.
- [Working with in-app purchase versions](working-with-in-app-purchase-versions.md)
  Manage draft versions of an in-app purchase’s localized metadata and review images before submitting for App Review.
- [Migrating in-app purchase metadata to v2](migrating-in-app-purchase-metadata-to-v2.md)
  Update an existing integration from the pre-4.4.1 metadata workflow to the version-based v2 workflow.
- [In-App Purchase Versions](in-app-purchase-versions.md)
  Create and read draft versions of an in-app purchase, with their localized metadata and review images.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchase versions.
- [In-App purchase price schedules](in-app-purchase-price-schedules.md)
  Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.
- [In-app purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an in-app purchase.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for in-app purchases.
- [In-app purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-localizations-v1)*
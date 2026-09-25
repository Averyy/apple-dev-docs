# In-App Purchase Localizations

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for In-App Purchase versions.

## Topics

### Endpoints
- [List localizations for an In-App Purchase version](get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an In-App Purchase.
- [Create an In-App Purchase localization](post-v2-inapppurchaselocalizations.md)
  Create a localized display name and description for an In-App Purchase configured with the v2 API.
- [Read In-App Purchase localization information](get-v2-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale of an In-App Purchase configured with the v2 API.
- [Modify an In-App Purchase localization](patch-v2-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an In-App Purchase configured with the v2 API.
- [Delete an In-App Purchase localization](delete-v2-inapppurchaselocalizations-_id_.md)
  Delete a localized display name and description for an In-App Purchase configured with the v2 API.
### Objects
- [object InAppPurchaseLocalizationV2](inapppurchaselocalizationv2.md)
  The localized display name and description for an In-App Purchase configured with the v2 API, shown to customers in a specific language.
- [object InAppPurchaseLocalizationV2CreateRequest](inapppurchaselocalizationv2createrequest.md)
  The request body you use to create an In-App Purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2Response](inapppurchaselocalizationv2response.md)
  The response body for endpoints that create, read, or modify an In-App Purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2UpdateRequest](inapppurchaselocalizationv2updaterequest.md)
  The request body you use to update an In-App Purchase localization with the v2 API.
- [object InAppPurchaseLocalizationsV2Response](inapppurchaselocalizationsv2response.md)
  The response body for endpoints that list In-App Purchase localizations configured with the v2 API.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-localizations)*
# In-App Purchase Localizations

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for in-app purchase versions.

## Topics

### Endpoints
- [List localizations for an in-app purchase version](get-v1-inapppurchaseversions-_id_-localizations.md)
  List the localized display names and descriptions captured in a draft version of an in-app purchase.
- [Create an in-app purchase localization](post-v2-inapppurchaselocalizations.md)
  Create a localized display name and description for an in-app purchase configured with the v2 API.
- [Read in-app purchase localization information](get-v2-inapppurchaselocalizations-_id_.md)
  Get the display name and description for a specific locale of an in-app purchase configured with the v2 API.
- [Modify an in-app purchase localization](patch-v2-inapppurchaselocalizations-_id_.md)
  Update the display name and description for a specific locale of an in-app purchase configured with the v2 API.
- [Delete an in-app purchase localization](delete-v2-inapppurchaselocalizations-_id_.md)
  Delete a localized display name and description for an in-app purchase configured with the v2 API.
### Objects
- [object InAppPurchaseLocalizationV2](inapppurchaselocalizationv2.md)
  The localized display name and description for an in-app purchase configured with the v2 API, shown to customers in a specific language.
- [object InAppPurchaseLocalizationV2CreateRequest](inapppurchaselocalizationv2createrequest.md)
  The request body you use to create an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2Response](inapppurchaselocalizationv2response.md)
  The response body for endpoints that create, read, or modify an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2UpdateRequest](inapppurchaselocalizationv2updaterequest.md)
  The request body you use to update an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationsV2Response](inapppurchaselocalizationsv2response.md)
  The response body for endpoints that list in-app purchase localizations configured with the v2 API.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-localizations)*
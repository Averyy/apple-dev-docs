# In-App Purchase price schedules

**Framework**: App Store Connect API

Create a scheduled price change for an In-App Purchase, and get information about scheduled price changes.

## Topics

### Endpoints
- [Read In-App Purchase Price Schedule Information](get-v1-inapppurchasepriceschedules-_id_.md)
  Get information about a specific scheduled price change for an In-App Purchase.
- [Read Price Information for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-manualprices.md)
  Get information about a set price or prices for an In-App Purchase price schedule.
- [List manual price IDs for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an In-App Purchase](post-v1-inapppurchasepriceschedules.md)
  Create a scheduled price change for an In-App Purchase.
- [List Automatically Generated Prices for an In-App Purchase Price](get-v1-inapppurchasepriceschedules-_id_-automaticprices.md)
  Get information about a price or prices automatically set based on a base territory for an In-App Purchase price schedule.
- [List automatic price IDs for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-automaticprices.md)
- [Read the Selected Base Territory for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-baseterritory.md)
  Get information about the selected base territory for an In-App Purchase price schedule.
- [Get the base territory ID for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-baseterritory.md)
### Objects
- [object InAppPurchasePriceSchedule](inapppurchasepriceschedule.md)
  A time-based pricing schedule for an In-App Purchase, managing base prices and planned price changes.
- [object InAppPurchasePriceScheduleCreateRequest](inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an In-App Purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an In-App Purchase.
- [object InAppPurchasePricesResponse](inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an In-App Purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](inapppurchasepriceschedulemanualpriceslinkagesresponse.md)

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
- [In-App Purchase localizations (v1)](in-app-purchase-localizations-v1.md)
  Create, modify, and delete localized metadata for In-App Purchases.
- [In-App Purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an In-App Purchase.
- [In-App Purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for In-App Purchases.
- [In-App Purchase images (v1)](in-app-purchase-images-v1.md)
  Create, modify, and delete promotion images for your In-App Purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-price-schedules)*
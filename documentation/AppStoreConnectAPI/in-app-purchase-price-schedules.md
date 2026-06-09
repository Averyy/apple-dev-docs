# In-App purchase price schedules

**Framework**: App Store Connect API

Create a scheduled price change for an in-app purchase, and get information about scheduled price changes.

## Topics

### Endpoints
- [Read In-App Purchase Price Schedule Information](get-v1-inapppurchasepriceschedules-_id_.md)
  Get information about a specific scheduled price change for an in-app purchase.
- [Read Price Information for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-manualprices.md)
  Get information about a set price or prices for an in-app purchase price schedule.
- [List manual price IDs for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an In-App Purchase](post-v1-inapppurchasepriceschedules.md)
  Create a scheduled price change for an in-app purchase.
- [List Automatically Generated Prices for an In-App Purchase Price](get-v1-inapppurchasepriceschedules-_id_-automaticprices.md)
  Get information about a price or prices automatically set based on a base territory for an in-app purchase price schedule.
- [List automatic price IDs for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-automaticprices.md)
- [Read the Selected Base Territory for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-baseterritory.md)
  Get information about the selected base territory for an in-app purchase price schedule.
- [Get the base territory ID for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-baseterritory.md)
### Objects
- [object InAppPurchasePriceSchedule](inapppurchasepriceschedule.md)
  A time-based pricing schedule for an in-app purchase, managing base prices and planned price changes.
- [object InAppPurchasePriceScheduleCreateRequest](inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an in-app purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an in-app purchase.
- [object InAppPurchasePricesResponse](inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an in-app purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](inapppurchasepriceschedulemanualpriceslinkagesresponse.md)

## See Also

- [Managing in-app purchases](managing-in-app-purchases.md)
  Learn how to create and manage in-app purchases with the App Store Connect API.
- [In-App Purchases](in-app-purchases.md)
  Create, modify, and delete in-app purchases for your app.
- [In-App Purchase Localizations](in-app-purchase-localizations.md)
  Create, modify, and delete localized metadata for in-app purchases.
- [In-app purchase availability](in-app-purchase-availability.md)
  Read and modify territory availability for an in-app purchase.
- [In-app purchase images](in-app-purchase-images.md)
  Create, modify, and delete promotion images for your in-app purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-price-schedules)*
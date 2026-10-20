# InAppPurchasePriceSchedule

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A time-based pricing schedule for an In-App Purchase, managing base prices and planned price changes.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object InAppPurchasePriceSchedule
```

## Topics

### Objects
- [object InAppPurchasePriceSchedule.Relationships](./inapppurchasepriceschedule/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchasePriceSchedule.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `inAppPurchasePriceSchedules`

## See Also

### Objects
- [object InAppPurchasePriceScheduleCreateRequest](./inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an In-App Purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](./inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an In-App Purchase.
- [object InAppPurchasePricesResponse](./inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an In-App Purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](./inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](./inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](./inapppurchasepriceschedulemanualpriceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasepriceschedule)*
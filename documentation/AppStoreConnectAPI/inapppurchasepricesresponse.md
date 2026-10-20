# InAppPurchasePricesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of configured prices for an In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object InAppPurchasePricesResponse
```

## Properties

- `data` ([InAppPurchasePrice]) *(required)*
- `included` ([*]): **Allowed Types**: `InAppPurchasePricePoint`, `Territory`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object InAppPurchasePriceSchedule](./inapppurchasepriceschedule.md)
  A time-based pricing schedule for an In-App Purchase, managing base prices and planned price changes.
- [object InAppPurchasePriceScheduleCreateRequest](./inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an In-App Purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](./inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an In-App Purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](./inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](./inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](./inapppurchasepriceschedulemanualpriceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasepricesresponse)*
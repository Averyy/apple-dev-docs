# InAppPurchasePriceScheduleCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an In-App Purchase price schedule.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object InAppPurchasePriceScheduleCreateRequest
```

## Mentions

- [App Store Connect API 3.2 release notes](./app-store-connect-api-3-2-release-notes.md)

## Topics

### Objects
- [object InAppPurchasePriceScheduleCreateRequest.Data](./inapppurchasepriceschedulecreaterequest/data-data.dictionary.md)
  The request body you use to create an In-App Purchase price schedule.

## Properties

- `data` (InAppPurchasePriceScheduleCreateRequest.Data) *(required)*
- `included` ([*]): **Allowed Types**: `InAppPurchasePriceInlineCreate`, `TerritoryInlineCreate`

## See Also

### Objects
- [object InAppPurchasePriceSchedule](./inapppurchasepriceschedule.md)
  A time-based pricing schedule for an In-App Purchase, managing base prices and planned price changes.
- [object InAppPurchasePriceScheduleResponse](./inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an In-App Purchase.
- [object InAppPurchasePricesResponse](./inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an In-App Purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](./inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](./inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](./inapppurchasepriceschedulemanualpriceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasepriceschedulecreaterequest)*
# InAppPurchasePricesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of configured prices for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchasePricesResponse
```

## Properties

- `data` ([InAppPurchasePrice]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object InAppPurchasePriceSchedule](inapppurchasepriceschedule.md)
  A time-based pricing schedule for an in-app purchase, managing base prices and planned price changes.
- [object InAppPurchasePriceScheduleCreateRequest](inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an in-app purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an in-app purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](inapppurchasepriceschedulemanualpriceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasepricesresponse)*
# InAppPurchasePriceSchedule

**Framework**: App Store Connect API  
**Kind**: dictionary

A time-based pricing schedule for an in-app purchase, managing base prices and planned price changes.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchasePriceSchedule
```

## Topics

### Objects
- [object InAppPurchasePriceSchedule.Relationships](inapppurchasepriceschedule/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchasePriceSchedule.Relationships)
- `type` (string) *(required)*

## See Also

- [object InAppPurchasePriceScheduleCreateRequest](inapppurchasepriceschedulecreaterequest.md)
  The request body you use to create an in-app purchase price schedule.
- [object InAppPurchasePriceScheduleResponse](inapppurchasepricescheduleresponse.md)
  A response containing a single pricing schedule for an in-app purchase.
- [object InAppPurchasePricesResponse](inapppurchasepricesresponse.md)
  A response containing a list of configured prices for an in-app purchase.
- [object InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse](inapppurchasepricescheduleautomaticpriceslinkagesresponse.md)
- [object InAppPurchasePriceScheduleBaseTerritoryLinkageResponse](inapppurchasepriceschedulebaseterritorylinkageresponse.md)
- [object InAppPurchasePriceScheduleManualPricesLinkagesResponse](inapppurchasepriceschedulemanualpriceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasepriceschedule)*
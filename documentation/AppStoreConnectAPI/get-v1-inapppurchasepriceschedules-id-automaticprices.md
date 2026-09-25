# List Automatically Generated Prices for an In-App Purchase Price

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a price or prices automatically set based on a base territory for an In-App Purchase price schedule.

**Availability**:
- App Store Connect API 2.3+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchasePriceSchedules/{id}/automaticPrices`

## Parameters

- `fields[inAppPurchasePricePoints]` ([string])
- `fields[inAppPurchasePrices]` ([string])
- `include` ([string])
- `limit` (integer)
- `filter[territory]` ([string])
- `fields[territories]` ([string])

## See Also

- [Read In-App Purchase Price Schedule Information](get-v1-inapppurchasepriceschedules-_id_.md)
  Get information about a specific scheduled price change for an In-App Purchase.
- [Read Price Information for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-manualprices.md)
  Get information about a set price or prices for an In-App Purchase price schedule.
- [List manual price IDs for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an In-App Purchase](post-v1-inapppurchasepriceschedules.md)
  Create a scheduled price change for an In-App Purchase.
- [List automatic price IDs for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-automaticprices.md)
- [Read the Selected Base Territory for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-baseterritory.md)
  Get information about the selected base territory for an In-App Purchase price schedule.
- [Get the base territory ID for an In-App Purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-baseterritory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchasepriceschedules-_id_-automaticprices)*
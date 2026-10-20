# Read Price Information for an In-App Purchase Price Schedule

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a set price or prices for an In-App Purchase price schedule.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing In-App Purchases](./managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchasePriceSchedules/{id}/manualPrices`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[inAppPurchasePricePoints]` ([string]): **Allowed Values**: `customerPrice`, `proceeds`, `territory`, `equalizations`
- `fields[inAppPurchasePrices]` ([string]): **Allowed Values**: `startDate`, `endDate`, `manual`, `inAppPurchasePricePoint`, `territory`
- `include` ([string]): **Allowed Values**: `inAppPurchasePricePoint`, `territory`
- `limit` (integer): **Maximum**: `200`
- `filter[territory]` ([string])
- `fields[territories]` ([string]): **Allowed Values**: `currency`

## Responses

- `200` OK (`InAppPurchasePricesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read In-App Purchase Price Schedule Information](./get-v1-inapppurchasepriceschedules-_id_.md)
  Get information about a specific scheduled price change for an In-App Purchase.
- [List manual price IDs for an In-App Purchase price schedule](./get-v1-inapppurchasepriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an In-App Purchase](./post-v1-inapppurchasepriceschedules.md)
  Create a scheduled price change for an In-App Purchase.
- [List Automatically Generated Prices for an In-App Purchase Price](./get-v1-inapppurchasepriceschedules-_id_-automaticprices.md)
  Get information about a price or prices automatically set based on a base territory for an In-App Purchase price schedule.
- [List automatic price IDs for an In-App Purchase price schedule](./get-v1-inapppurchasepriceschedules-_id_-relationships-automaticprices.md)
- [Read the Selected Base Territory for an In-App Purchase Price Schedule](./get-v1-inapppurchasepriceschedules-_id_-baseterritory.md)
  Get information about the selected base territory for an In-App Purchase price schedule.
- [Get the base territory ID for an In-App Purchase price schedule](./get-v1-inapppurchasepriceschedules-_id_-relationships-baseterritory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchasepriceschedules-_id_-manualprices)*
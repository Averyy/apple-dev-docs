# List manual price IDs for an app price schedule

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPriceSchedules/{id}/relationships/manualPrices`

## Parameters

- `limit` (integer)

## See Also

- [Read Price Schedule Information for an App](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [Get the app price schedule ID for an app](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an App's Price Schedule Information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List Automatically Generated Prices for an App](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the Base Territory for an App's Price Schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List Manually Chosen Prices for an App](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [List automatic price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [Get the base territory ID for an app price schedule](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [Add a Scheduled Price Change to an App](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppriceschedules-_id_-relationships-manualprices)*
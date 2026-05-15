# Read the Base Territory for an App's Price Schedule

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the base territory and currency for a specific app.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/baseTerritory
```

**Response**:

```json
{
  "data" : {
    "type" : "territories",
    "id" : "CAN",
    "attributes" : {
      "currency" : "CAD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/CAN"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/baseTerritory"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPriceSchedules/{id}/baseTerritory`

## Parameters

- `fields[territories]` ([string])

## See Also

- [Read Price Schedule Information for an App](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [GET /v1/apps/{id}/relationships/appPriceSchedule](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an App's Price Schedule Information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List Automatically Generated Prices for an App](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [List Manually Chosen Prices for an App](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [GET /v1/appPriceSchedules/{id}/relationships/automaticPrices](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [GET /v1/appPriceSchedules/{id}/relationships/baseTerritory](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [GET /v1/appPriceSchedules/{id}/relationships/manualPrices](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an App](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppriceschedules-_id_-baseterritory)*
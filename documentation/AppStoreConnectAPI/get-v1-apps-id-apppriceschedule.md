# Read price schedule information for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read price schedule details for a specific app.

**Availability**:
- App Store Connect API 2.3+

## Mentions

- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6447402192/appPriceSchedule
```

**Response**:

```json
{
  "data" : {
    "type" : "appPriceSchedules",
    "id" : "6447402192",
    "relationships" : {
      "baseTerritory" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/relationships/baseTerritory",
          "related" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/baseTerritory"
        }
      },
      "manualPrices" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/relationships/manualPrices",
          "related" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/manualPrices"
        }
      },
      "automaticPrices" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/relationships/automaticPrices",
          "related" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/automaticPrices"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/6447402192/appPriceSchedule"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appPriceSchedule`

## Parameters

- `fields[appPriceSchedules]` ([string])
- `fields[appPrices]` ([string])
- `fields[apps]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit[automaticPrices]` (integer)
- `limit[manualPrices]` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/appPriceSchedule](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an app's price schedule information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List automatically generated prices for an app](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the base territory for an app's price schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List manually chosen prices for an app](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [GET /v1/appPriceSchedules/{id}/relationships/automaticPrices](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [GET /v1/appPriceSchedules/{id}/relationships/baseTerritory](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [GET /v1/appPriceSchedules/{id}/relationships/manualPrices](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a scheduled price change to an app](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apppriceschedule)*
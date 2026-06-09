# Read Price Schedule Information for an App

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

- `fields[appPriceSchedules]` ([string]): Additional fields to include for each app price schedule resource returned by the response.
- `fields[appPrices]` ([string]): Additional fields to include for each app price resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[automaticPrices]` (integer): The maximum number of related automatic prices resources to return.
- `limit[manualPrices]` (integer): The maximum number of related manual prices resources to return.

## See Also

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
- [List manual price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an App](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apppriceschedule)*
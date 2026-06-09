# Add a Scheduled Price Change to an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a scheduled price change for an app.

**Availability**:
- App Store Connect API 2.3+

## Mentions

- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)

#### Discussion

> ⚠️ **Warning**:  If you use this endpoint to add a scheduled price change to your app, you can’t use `AppPriceInlineCreate` to change your app’s price.

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/appPriceSchedules
```

**Response**:

```json
{
  "data": {
    "type": "appPriceSchedules",
    "attributes": {},
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6447402192"
        }
      },
      "manualPrices": {
        "data": [
          {
            "type": "appPrices",
            "id": "${newprice-0}"
          },
          {
            "type": "appPrices",
            "id": "${newprice-1}"
          },
          {
            "type": "appPrices",
            "id": "${newprice-2}"
          },
          {
            "type": "appPrices",
            "id": "${newprice-3}"
          }
        ]
      },
      "baseTerritory": {
        "data": {
          "type": "territories",
          "id": "CAN"
        }
      }
    }
  },
  "included": [
    {
      "id": "${newprice-0}",
      "relationships": {
        "appPricePoint": {
          "data": {
            "type": "appPricePoints",
            "id": "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBTEIiLCJwIjoiMTAwMTQifQ"
          }
        }
      },
      "type": "appPrices",
      "attributes": {
        "startDate": null,
        "endDate": "2023-03-11"
      }
    },
    {
      "id": "${newprice-1}",
      "relationships": {
        "appPricePoint": {
          "data": {
            "type": "appPricePoints",
            "id": "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBUkciLCJwIjoiMTAwMzQifQ"
          }
        }
      },
      "type": "appPrices",
      "attributes": {
        "startDate": null,
        "endDate": "2023-03-11"
      }
    },
    {
      "id": "${newprice-2}",
      "relationships": {
        "appPricePoint": {
          "data": {
            "type": "appPricePoints",
            "id": "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDcifQ"
          }
        }
      },
      "type": "appPrices",
      "attributes": {
        "startDate": null,
        "endDate": "2023-03-11"
      }
    },
    {
      "id": "${newprice-3}",
      "relationships": {
        "appPricePoint": {
          "data": {
            "type": "appPricePoints",
            "id": "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMTAifQ"
          }
        }
      },
      "type": "appPrices",
      "attributes": {
        "startDate": "2023-03-11",
        "endDate": null
      }
    }
  ]
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appPriceSchedules`

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
- [List manual price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-manualprices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-apppriceschedules)*
# List manually chosen prices for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the prices you chose for a specific app.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/manualPrices?limit=200&include=appPricePoint,territory&fields%5BappPricePoints%5D=customerPrice&filter%5Bterritory%5D=USA,CAN&fields%5Bterritories%5D=currency
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDciLCJzZCI6MC4wLCJlZCI6MC4wfQ",
    "attributes" : {
      "manual" : true,
      "startDate" : null,
      "endDate" : null
    },
    "relationships" : {
      "appPricePoint" : {
        "data" : {
          "type" : "appPricePoints",
          "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDcifQ"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDciLCJzZCI6MC4wLCJlZCI6MC4wfQ"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDciLCJzZCI6MC4wLCJlZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDB9",
    "attributes" : {
      "manual" : true,
      "startDate" : null,
      "endDate" : "2023-02-28"
    },
    "relationships" : {
      "appPricePoint" : {
        "data" : {
          "type" : "appPricePoints",
          "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDcifQ"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "USA"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDciLCJzZCI6MC4wLCJlZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDB9"
    }
  } ],
  "included" : [ {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDcifQ",
    "attributes" : {
      "customerPrice" : "9.99"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDcifQ"
    }
  }, {
    "type" : "territories",
    "id" : "CAN",
    "attributes" : {
      "currency" : "CAD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/CAN"
    }
  }, {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDcifQ",
    "attributes" : {
      "customerPrice" : "0.89"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDcifQ"
    }
  }, {
    "type" : "territories",
    "id" : "USA",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/USA"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/manualPrices?include=appPricePoint%2Cterritory&fields%5BappPricePoints%5D=customerPrice&filter%5Bterritory%5D=CAN%2CUSA&limit=200&fields%5Bterritories%5D=currency"
  },
  "meta" : {
    "paging" : {
      "total" : 2,
      "limit" : 200
    }
  }

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPriceSchedules/{id}/manualPrices`

## Parameters

- `fields[appPricePoints]` ([string])
- `fields[appPrices]` ([string])
- `fields[territories]` ([string])
- `filter[endDate]` ([string])
- `filter[startDate]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read price schedule information for an app](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [GET /v1/apps/{id}/relationships/appPriceSchedule](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an app's price schedule information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [List automatically generated prices for an app](get-v1-apppriceschedules-_id_-automaticprices.md)
  List the automatically calculated prices for an app generated from a base territory.
- [Read the base territory for an app's price schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [GET /v1/appPriceSchedules/{id}/relationships/automaticPrices](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [GET /v1/appPriceSchedules/{id}/relationships/baseTerritory](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [GET /v1/appPriceSchedules/{id}/relationships/manualPrices](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a scheduled price change to an app](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppriceschedules-_id_-manualprices)*
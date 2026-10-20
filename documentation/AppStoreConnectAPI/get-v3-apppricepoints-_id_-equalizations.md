# List App Price Point Equalizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all equivalent app prices points to a base price point.

**Availability**:
- App Store Connect API 2.3+

## Mentions

- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/equalizations?filter%5Bterritory%5D=USA,MEX&include=territory&fields%5BappPricePoints%5D=customerPrice,proceeds,territory&limit=5
```

**Response**:

```json
{
  “data” : [ {
    “type” : “appPricePoints”,
    “id” : “eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJNRVgiLCJwIjoiMTAwMDEifQ”,
    “attributes” : {
      “customerPrice” : “19.0”,
      “proceeds” : “13.3”
    },
    “relationships” : {
      “territory” : {
        “data” : {
          “type” : “territories”,
          “id” : “MEX”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJNRVgiLCJwIjoiMTAwMDEifQ”
    }
  }, {
    “type” : “appPricePoints”,
    “id” : “eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ”,
    “attributes” : {
      “customerPrice” : “0.29”,
      “proceeds” : “0.2”
    },
    “relationships” : {
      “territory” : {
        “data” : {
          “type” : “territories”,
          “id” : “USA”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ”
    }
  } ],
  “included” : [ {
    “type” : “territories”,
    “id” : “MEX”,
    “attributes” : {
      “currency” : “MXN”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/territories/MEX”
    }
  }, {
    “type” : “territories”,
    “id” : “USA”,
    “attributes” : {
      “currency” : “USD”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/territories/USA”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/equalizations?include=territory&fields%5BappPricePoints%5D=proceeds%2CcustomerPrice%2Cterritory&filter%5Bterritory%5D=MEX%2CUSA&limit=5”
  },
  “meta” : {
    “paging” : {
      “total” : 2,
      “limit” : 5
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v3/appPricePoints/{id}/equalizations`

## Parameters

- `fields[appPricePoints]` ([string]): Additional fields to include for each app price point resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `filter[territory]` ([string]): Filter the returned app price points by territory.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app price point resources to return.

## See Also

- [List All Price Points for an App](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [List app price point IDs for an app](get-v1-apps-_id_-relationships-apppricepoints.md)
- [Read App Price Point Information](get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List equalization price point IDs for an app price point](get-v3-apppricepoints-_id_-relationships-equalizations.md)
  Get a list of equalization price point IDs for a specific app price point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v3-apppricepoints-_id_-equalizations)*
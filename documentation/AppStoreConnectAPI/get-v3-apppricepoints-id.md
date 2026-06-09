# Read App Price Point Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a specific app price point.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ
```

**Response**:

```json
{
  "data" : {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ",
    "attributes" : {
      "customerPrice" : "1.39",
      "proceeds" : "0.97"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/equalizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v3/appPricePoints/{id}`

## Parameters

- `fields[appPricePoints]` ([string]): Additional fields to include for each app price point resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[apps]` ([string])
- `fields[territories]` ([string])

## See Also

- [List All Price Points for an App](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [List app price point IDs for an app](get-v1-apps-_id_-relationships-apppricepoints.md)
- [List App Price Point Equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
- [List equalization price point IDs for an app price point](get-v3-apppricepoints-_id_-relationships-equalizations.md)
  Get a list of equalization price point IDs for a specific app price point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v3-apppricepoints-_id_)*
# Read app price point information

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

- `fields[appPricePoints]` ([string])
- `include` ([string])

## See Also

- [List all price points for an app](get-v1-apps-_id_-apppricepoints.md)
  Get all the available price points for a specific app.
- [GET /v1/apps/{id}/relationships/appPricePoints](get-v1-apps-_id_-relationships-apppricepoints.md)
- [List app price point equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
- [GET /v3/appPricePoints/{id}/relationships/equalizations](get-v3-apppricepoints-_id_-relationships-equalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v3-apppricepoints-_id_)*
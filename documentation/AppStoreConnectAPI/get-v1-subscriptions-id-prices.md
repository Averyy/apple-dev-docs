# List all prices for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of prices for an auto-renewable subscription, by territory.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/subscriptions/6470878936/prices?filter[territory]=USA&include=subscriptionPricePoint,territory&limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "subscriptionPrices",
    "id" : "eyJhIjoiNjQ3MDg3ODkzNiIsImMiOiJVUyIsImQiOjAsInAiOiIwIn0",
    "attributes" : {
      "startDate" : null,
      "preserved" : true,
      "planType" : "UPFRONT"
    },
    "relationships" : {
      "territory" : {
        "data" : { "type" : "territories", "id" : "USA" }
      },
      "subscriptionPricePoint" : {
        "data" : { "type" : "subscriptionPricePoints", "id" : "eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMTAifQ" }
      }
    }
  }, {
    "type" : "subscriptionPrices",
    "id" : "eyJhIjoiNjQ3MDg3ODkzNiIsImMiOiJVUyIsImQiOjIwMTUwLCJwIjoiMCJ9",
    "attributes" : {
      "startDate" : "2025-03-03",
      "preserved" : false,
      "planType" : "UPFRONT"
    },
    "relationships" : {
      "territory" : {
        "data" : { "type" : "territories", "id" : "USA" }
      },
      "subscriptionPricePoint" : {
        "data" : { "type" : "subscriptionPricePoints", "id" : "eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMzYifQ" }
      }
    }
  } ],
  "included" : [ {
    "type" : "territories",
    "id" : "USA",
    "attributes" : { "currency" : "USD" }
  }, {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMTAifQ",
    "attributes" : { "customerPrice" : "0.99", "proceeds" : "0.7", "proceedsYear2" : "0.84" }
  }, {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMzYifQ",
    "attributes" : { "customerPrice" : "2.99", "proceeds" : "2.1", "proceedsYear2" : "2.54" }
  } ],
  "meta" : {
    "paging" : { "total" : 2, "limit" : 2 }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/prices`

## Parameters

- `fields[subscriptionPricePoints]` ([string])
- `fields[subscriptionPrices]` ([string])
- `fields[territories]` ([string])
- `filter[subscriptionPricePoint]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)
- `filter[planType]` ([string])

## See Also

- [List all price points for a subscription](get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.
- [List price point IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List all subscription price ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-prices.md)
  Get a list of resource IDs representing subscription prices for an auto-renewable subscription.
- [Delete prices from a subscription](delete-v1-subscriptions-_id_-relationships-prices.md)
  Delete a scheduled subscription price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-prices)*
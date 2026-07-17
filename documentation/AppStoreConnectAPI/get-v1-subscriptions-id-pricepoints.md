# List all price points for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of price points for an auto-renewable subscription by territory.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)
- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)

##### Discussion

> ❗ **Important**:  Use the `territory` filter on all requests. This will be required in a future release.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/subscriptions/6470878936/pricePoints?filter[territory]=USA&include=territory&limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ",
    "attributes" : {
      "customerPrice" : "0.29",
      "proceeds" : "0.21",
      "proceedsYear2" : "0.25"
    },
    "relationships" : {
      "territory" : {
        "data" : { "type" : "territories", "id" : "USA" }
      },
      "adjustedEqualizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ/relationships/adjustedEqualizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ/adjustedEqualizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ3MDg3ODkzNiIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ"
    }
  } ],
  "included" : [ {
    "type" : "territories",
    "id" : "USA",
    "attributes" : { "currency" : "USD" }
  } ],
  "meta" : {
    "paging" : { "total" : 900, "limit" : 2 }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/pricePoints`

## Parameters

- `fields[subscriptionPricePoints]` ([string])
- `fields[territories]` ([string])
- `filter[territory]` ([string]): Use this filter with all requests.
- `include` ([string])
- `limit` (integer)
- `filter[planType]` ([string])
- `filter[upfrontPricePointId]` ([string])

## See Also

- [List price point IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List all prices for a subscription](get-v1-subscriptions-_id_-prices.md)
  Get a list of prices for an auto-renewable subscription, by territory.
- [List all subscription price ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-prices.md)
  Get a list of resource IDs representing subscription prices for an auto-renewable subscription.
- [Delete prices from a subscription](delete-v1-subscriptions-_id_-relationships-prices.md)
  Delete a scheduled subscription price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-pricepoints)*
# List plan availabilities for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all plan availabilities for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4+

## Mentions

- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/subscriptions/6470878936/planAvailabilities?limit=2
```

**Response**:

```json
{
  "data" : [ {
    "type" : "subscriptionPlanAvailabilities",
    "id" : "eyJhIjoiNjQ3MDg3ODkzNiIsInAiOiIwIn0",
    "attributes" : {
      "availableInNewTerritories" : true,
      "planType" : "UPFRONT"
    },
    "relationships" : {
      "availableTerritories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/eyJhIjoiNjQ3MDg3ODkzNiIsInAiOiIwIn0/relationships/availableTerritories",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/eyJhIjoiNjQ3MDg3ODkzNiIsInAiOiIwIn0/availableTerritories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPlanAvailabilities/eyJhIjoiNjQ3MDg3ODkzNiIsInAiOiIwIn0"
    }
  } ],
  "meta" : {
    "paging" : { "total" : 1, "limit" : 2 }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/planAvailabilities`

## Parameters

- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscription plan availability resource that the response returns.
- `fields[territories]` ([string]): Additional fields to include for each territory resource that the response returns.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of subscription plan availability resources to return.
- `limit[availableTerritories]` (integer): The maximum number of available territory resources to return.

## See Also

- [List plan availability IDs for a subscription](get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-planavailabilities)*
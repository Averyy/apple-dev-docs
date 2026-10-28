# List plan availabilities for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all plan availabilities for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 4.4+

## Mentions

- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscription` resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `fields[subscriptionPlanAvailabilities]` ([string]): Additional fields to include for each subscription plan availability resource that the response returns.

  **Allowed Values**: `availableInNewTerritories`, `planType`, `availableTerritories`
- `fields[territories]` ([string]): Additional fields to include for each territory resource that the response returns.

  **Allowed Values**: `currency`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `availableTerritories`
- `limit` (integer): The maximum number of subscription plan availability resources to return.

  **Maximum**: `200`
- `limit[availableTerritories]` (integer): The maximum number of available territory resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionPlanAvailabilitiesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading plan availability from a subscription
- [List plan availability IDs for a subscription](./get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-planavailabilities)*
# Read the availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the territory availability for a subscription.

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This endpoint is deprecated. Use [`Read subscription plan availability information`](./get-v1-subscriptionplanavailabilities-_id_.md) instead.

## Mentions

- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418
```

**Response**:

```json
{
  "data" : {
    "type" : "subscriptionAvailabilities",
    "id" : "6447589418",
    "attributes" : {
      "availableInNewTerritories" : false
    },
    "relationships" : {
      "availableTerritories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/relationships/availableTerritories",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the subscription resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `fields[subscriptionAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `include` ([string]): **Allowed Values**: `availableTerritories`
- `limit[availableTerritories]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List the territory availability of a subscription](./get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [List available territory IDs for a subscription availability](./get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)
- [Modify the territory availability of a subscription](./post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionavailabilities-_id_)*
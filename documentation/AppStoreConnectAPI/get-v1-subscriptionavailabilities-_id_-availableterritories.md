# List the territory availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the territory availability and currency of a specific subscription.

**Availability**:
- App Store Connect API 2.3+ - Deprecated in 4.4

> **Deprecated**: This endpoint is deprecated. Use [`List available territories for a subscription plan availability`](./get-v1-subscriptionplanavailabilities-_id_-availableterritories.md) instead.

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?limit=5
```

**Response**:

```json
{
  "data" : [ {
    "type" : "territories",
    "id" : "SLV",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/SLV"
    }
  }, {
    "type" : "territories",
    "id" : "BRB",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/BRB"
    }
  }, {
    "type" : "territories",
    "id" : "CYM",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/CYM"
    }
  }, {
    "type" : "territories",
    "id" : "NIC",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/NIC"
    }
  }, {
    "type" : "territories",
    "id" : "NAM",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/NAM"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?limit=5",
    "next" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?cursor=BQ.AO4JFxQ&limit=5"
  },
  "meta" : {
    "paging" : {
      "total" : 175,
      "limit" : 5
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/{id}/availableTerritories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the subscription resource ID from the [`List all subscriptions for a subscription group`](./get-v1-subscriptiongroups-_id_-subscriptions.md) response.

### Query Parameters

- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`TerritoriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read the availability of a subscription](./get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List available territory IDs for a subscription availability](./get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)
- [Modify the territory availability of a subscription](./post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionavailabilities-_id_-availableterritories)*
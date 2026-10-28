# Modify a Marketplace Webhook Configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the endpoint URL and secret for alternative distribution package notifications.

**Availability**:
- App Store Connect API 3.3+ - Deprecated in 4.0.1

> **Deprecated**: This endpoint is deprecated.

## Discussion

### Example Request and Response

**Request**:

```
PATCH https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635
{
  "data": {
    "type": "marketplaceWebhooks",
    "id": "c74970b8-6be0-40fa-8f51-8e1532005635",
    "attributes": {
      "endpointUrl": "https://example-2.com/api/ingest/notifications",
      "secret": "mySecret"
    }
  }
}
```

**Response**:

```json
{
  "data": [
    {
      "type": "marketplaceWebhooks",
      "id": "c74970b8-6be0-40fa-8f51-8e1532005635",
      "attributes": {
        "endpointUrl": "https://example-2.com/api/ingest/notifications"
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `marketplaceWebhooks` resource ID from the [`Read Marketplace Webhook Information`](./get-v1-marketplacewebhooks.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `MarketplaceWebhookUpdateRequest`

## Responses

- `200` OK (`MarketplaceWebhookResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Webhook Endpoint URLs
- [Read Marketplace Webhook Information](./get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Add a Marketplace Webhook Configuration](./post-v1-marketplacewebhooks.md)
  Add a new endpoint URL and secret for alternative distribution package notifications.
- [Delete a Marketplace Webhook Configuration](./delete-v1-marketplacewebhooks-_id_.md)
  Delete a specific marketplace notifcation endpoint URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-marketplacewebhooks-_id_)*
# Add a Marketplace Webhook Configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new endpoint URL and secret for alternative distribution package notifications.

**Availability**:
- App Store Connect API 3.3+ - Deprecated in 4.0.1

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [App Store Connect API 3.3 release notes](./app-store-connect-api-3-3-release-notes.md)
- [Configuring alternative marketplaces and alternative marketplace apps](./configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
- [Creating alternative distribution packages](./creating-alternative-distribution-packages.md)

#### Discussion

Each developer account has a single marketplace webhooks `endpointUrl`, so if you operate mutliple marketplaces all notifications come to a single endpoint. The notification payload contains the `marketplaceAppId.`

##### Example Request and Response

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks
{
  "data": {
    "type": "marketplaceWebhooks",
    "attributes": {
      "endpointUrl": "https://example.com/api/ingest/notifications",
      "secret": "mysecretstring"
    }
  }
}
```

**Response**:

```json
{
  “data”: [
    {
      “type”: “marketplaceWebhooks”,
      “id”: “c74970b8-6be0-40fa-8f51-8e1532005635”,
      “attributes”: {
        “endpointUrl”: “https://example.com/api/ingest/notifications”
      },
      “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635”
      }
    }
  ],
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks”
  },
  “meta”: {
    “paging”: {
      “total”: 1,
      “limit”: 50
    }
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks`

## Request Body

**Content-Type**: `application/json`  
**Type**: `MarketplaceWebhookCreateRequest`

## Responses

- `201` Created (`MarketplaceWebhookResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Webhook Endpoint URLs
- [Read Marketplace Webhook Information](./get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Modify a Marketplace Webhook Configuration](./patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.
- [Delete a Marketplace Webhook Configuration](./delete-v1-marketplacewebhooks-_id_.md)
  Delete a specific marketplace notifcation endpoint URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-marketplacewebhooks)*
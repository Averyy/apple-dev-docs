# Delete a Marketplace Webhook Configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a specific marketplace notifcation endpoint URL.

**Availability**:
- App Store Connect API 3.3+ - Deprecated in 4.0.1

> **Deprecated**: This endpoint is deprecated.

#### Discussion

##### Example Request and Response

**Request**:

```
DELETE https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `marketplaceWebhooks` resource ID from the [`Read Marketplace Webhook Information`](./get-v1-marketplacewebhooks.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Webhook Endpoint URLs
- [Read Marketplace Webhook Information](./get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Add a Marketplace Webhook Configuration](./post-v1-marketplacewebhooks.md)
  Add a new endpoint URL and secret for alternative distribution package notifications.
- [Modify a Marketplace Webhook Configuration](./patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-marketplacewebhooks-_id_)*
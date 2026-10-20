# Modify a Webhook Configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update details for a specific webhook.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](./configuring-webhook-notifications.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/webhooks/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `WebhookUpdateRequest`

## Responses

- `200` OK (`WebhookResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing webhook notifications
- [Read Webhook Information for an App](./get-v1-apps-_id_-webhooks.md)
  Read webhook configuration details for a specific app.
- [Read Webhook Information](./get-v1-webhooks-_id_.md)
  Read configuration details for a specific webhook.
- [Create a Webhook Configuration](./post-v1-webhooks.md)
  Add a new webhook configuration.
- [Delete a Webhook](./delete-v1-webhooks-_id_.md)
  Remove a specific webhook configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-webhooks-_id_)*
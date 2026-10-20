# Create a Webhook Configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new webhook configuration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](./configuring-webhook-notifications.md)
- [Understanding webhook events](./webhook-events.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/webhooks`

## Request Body

**Content-Type**: `application/json`  
**Type**: `WebhookCreateRequest`

## Responses

- `201` Created (`WebhookResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing webhook notifications
- [Read Webhook Information for an App](./get-v1-apps-_id_-webhooks.md)
  Read webhook configuration details for a specific app.
- [Read Webhook Information](./get-v1-webhooks-_id_.md)
  Read configuration details for a specific webhook.
- [Modify a Webhook Configuration](./patch-v1-webhooks-_id_.md)
  Update details for a specific webhook.
- [Delete a Webhook](./delete-v1-webhooks-_id_.md)
  Remove a specific webhook configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-webhooks)*
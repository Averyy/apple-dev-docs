# Redeliver a Previous Notification

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Resend a webhook notification from a specified template.

**Availability**:
- App Store Connect API 4.0+

#### Overview

> **Note**: The `template` in this payload is the original delivery that you want to resend. Find the `id` using [`Read the Deliveries for a Webhook`](./get-v1-webhooks-_id_-deliveries.md).

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/webhookDeliveries`

## Request Body

**Content-Type**: `application/json`  
**Type**: `WebhookDeliveryCreateRequest`

## Responses

- `201` Created (`WebhookDeliveryResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing webhook deliveries
- [Read the Deliveries for a Webhook](./get-v1-webhooks-_id_-deliveries.md)
  Get a list of deliveries for a specific webhook configuration.
- [List delivery IDs for a webhook](./get-v1-webhooks-_id_-relationships-deliveries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-webhookdeliveries)*
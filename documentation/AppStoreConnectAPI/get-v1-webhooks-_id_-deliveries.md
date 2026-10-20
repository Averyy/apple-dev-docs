# Read the Deliveries for a Webhook

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of deliveries for a specific webhook configuration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](./configuring-webhook-notifications.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/webhooks/{id}/deliveries`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[webhookDeliveries]` ([string]): **Allowed Values**: `createdDate`, `deliveryState`, `errorMessage`, `redelivery`, `sentDate`, `request`, `response`, `event`
- `fields[webhookEvents]` ([string]): **Allowed Values**: `eventType`, `payload`, `ping`, `createdDate`
- `filter[createdDateGreaterThanOrEqualTo]` ([string])
- `filter[createdDateLessThan]` ([string])
- `filter[deliveryState]` ([string]): **Allowed Values**: `SUCCEEDED`, `FAILED`, `PENDING`
- `include` ([string]): **Allowed Values**: `event`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`WebhookDeliveriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing webhook deliveries
- [List delivery IDs for a webhook](./get-v1-webhooks-_id_-relationships-deliveries.md)
- [Redeliver a Previous Notification](./post-v1-webhookdeliveries.md)
  Resend a webhook notification from a specified template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-webhooks-_id_-deliveries)*
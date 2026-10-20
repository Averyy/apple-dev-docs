# List delivery IDs for a webhook

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/webhooks/{id}/relationships/deliveries`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`WebhookDeliveriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing webhook deliveries
- [Read the Deliveries for a Webhook](./get-v1-webhooks-_id_-deliveries.md)
  Get a list of deliveries for a specific webhook configuration.
- [Redeliver a Previous Notification](./post-v1-webhookdeliveries.md)
  Resend a webhook notification from a specified template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-webhooks-_id_-relationships-deliveries)*
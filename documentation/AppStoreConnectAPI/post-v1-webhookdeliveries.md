# Redeliver a Previous Notification

**Framework**: App Store Connect API  
**Kind**: httpRequest

Resend a webhook notification from a specified template.

**Availability**:
- App Store Connect API 4.0+

#### Overview

> **Note**: The `template` in this payload is the original delivery that you want to resend. Find the `id` using [`Read the Deliveries for a Webhook`](get-v1-webhooks-_id_-deliveries.md).

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/webhookDeliveries`

## See Also

- [Read the Deliveries for a Webhook](get-v1-webhooks-_id_-deliveries.md)
  Get a list of deliveries for a specific webhook configuration.
- [List delivery IDs for a webhook](get-v1-webhooks-_id_-relationships-deliveries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-webhookdeliveries)*
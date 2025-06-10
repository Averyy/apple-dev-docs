# Redeliver a previous notification

**Framework**: App Store Connect API  
**Kind**: httpRequest

Resend a webhook notification from a specified template.

**Availability**:
- App Store Connect API 4.0+

#### Overview

> **Note**: The `template` in this payload is the original delivery that you want to resend. Find the `id` using [`Read the deliveries for a webhook`](get-v1-webhooks-_id_-deliveries.md).

## See Also

- [Read the deliveries for a webhook](get-v1-webhooks-_id_-deliveries.md)
  Get a list of deliveries for a specific webhook configuration.
- [GET /v1/webhooks/{id}/relationships/deliveries](get-v1-webhooks-_id_-relationships-deliveries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-webhookdeliveries)*
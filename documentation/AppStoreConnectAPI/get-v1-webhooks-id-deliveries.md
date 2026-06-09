# Read the Deliveries for a Webhook

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of deliveries for a specific webhook configuration.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/webhooks/{id}/deliveries`

## Parameters

- `fields[webhookDeliveries]` ([string])
- `fields[webhookEvents]` ([string])
- `filter[createdDateGreaterThanOrEqualTo]` ([string])
- `filter[createdDateLessThan]` ([string])
- `filter[deliveryState]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List delivery IDs for a webhook](get-v1-webhooks-_id_-relationships-deliveries.md)
- [Redeliver a Previous Notification](post-v1-webhookdeliveries.md)
  Resend a webhook notification from a specified template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-webhooks-_id_-deliveries)*
# Read Webhook Information for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read webhook configuration details for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/webhooks`

## Parameters

- `fields[apps]` ([string])
- `fields[webhooks]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read Webhook Information](get-v1-webhooks-_id_.md)
  Read configuration details for a specific webhook.
- [Create a Webhook Configuration](post-v1-webhooks.md)
  Add a new webhook configuration.
- [Modify a Webhook Configuration](patch-v1-webhooks-_id_.md)
  Update details for a specific webhook.
- [Delete a Webhook](delete-v1-webhooks-_id_.md)
  Remove a specific webhook configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-webhooks)*
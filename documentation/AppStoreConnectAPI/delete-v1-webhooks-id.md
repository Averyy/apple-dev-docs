# Delete a Webhook

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a specific webhook configuration.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/webhooks/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Webhook Information for an App](get-v1-apps-_id_-webhooks.md)
  Read webhook configuration details for a specific app.
- [Read Webhook Information](get-v1-webhooks-_id_.md)
  Read configuration details for a specific webhook.
- [Create a Webhook Configuration](post-v1-webhooks.md)
  Add a new webhook configuration.
- [Modify a Webhook Configuration](patch-v1-webhooks-_id_.md)
  Update details for a specific webhook.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-webhooks-_id_)*
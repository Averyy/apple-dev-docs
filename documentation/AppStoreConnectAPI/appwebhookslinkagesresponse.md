# AppWebhooksLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object AppWebhooksLinkagesResponse
```

## Topics

### Dictionaries
- [object AppWebhooksLinkagesResponse.Data](appwebhookslinkagesresponse/data-data.dictionary.md)

## Properties

- `data` ([AppWebhooksLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Webhook](webhook.md)
  A configured HTTP endpoint in App Store Connect that receives notifications when specific events occur.
- [object WebhookCreateRequest](webhookcreaterequest.md)
  The request body for registering a webhook endpoint to receive App Store Connect event notifications.
- [object WebhookDeliveriesResponse](webhookdeliveriesresponse.md)
  A response containing a list of webhook delivery records, each showing the outcome of a notification attempt.
- [object WebhookDelivery](webhookdelivery.md)
  A recorded delivery attempt of an event notification to a webhook endpoint, including the request and response details.
- [object WebhookDeliveryCreateRequest](webhookdeliverycreaterequest.md)
  The request body for retrying a failed webhook delivery.
- [object WebhookDeliveryResponse](webhookdeliveryresponse.md)
  A response containing a single webhook delivery attempt record.
- [object WebhookEvent](webhookevent.md)
  An event type that can trigger webhook notifications, such as build completion or review status changes.
- [object WebhookPing](webhookping.md)
  A test payload sent to verify that a webhook endpoint is reachable and correctly configured.
- [object WebhookPingCreateRequest](webhookpingcreaterequest.md)
  The request body for sending a test ping event to verify that a webhook endpoint is reachable.
- [object WebhookPingResponse](webhookpingresponse.md)
  A response confirming that a test ping was sent to a webhook endpoint.
- [object WebhookResponse](webhookresponse.md)
  The response body for endpoints that create, read, or modify a single webhook.
- [object WebhookUpdateRequest](webhookupdaterequest.md)
  The request body you use to update a webhook update request.
- [object WebhooksResponse](webhooksresponse.md)
  The response body for endpoints that list webhooks.
- [type WebhookEventType](webhookeventtype.md)
  A string that represents the the event types for a webhook notification.
- [object WebhookDeliveriesLinkagesResponse](webhookdeliverieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appwebhookslinkagesresponse)*
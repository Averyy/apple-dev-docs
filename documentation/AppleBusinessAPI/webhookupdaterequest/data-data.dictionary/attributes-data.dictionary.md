# WebhookUpdateRequest.Data.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes with values that you’re changing as part of the update request.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookUpdateRequest.Data.Attributes
```

## Properties

- `name` (string): The name of the webhook.
- `enabled` (boolean): A Boolean value that indicates whether the webhook is enabled.
- `eventTypes` ([WebhookEventType]): The event types that the webhook subscribes to. See [`WebhookEventType`](../../webhookeventtype.md) for possible values.
- `secret` (string): The secret for the webhook. The API doesn’t return this value in responses.
- `url` (uri): The URL that receives webhook event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookupdaterequest/data-data.dictionary/attributes-data.dictionary)*
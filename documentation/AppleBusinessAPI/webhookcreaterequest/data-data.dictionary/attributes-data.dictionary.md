# WebhookCreateRequest.Data.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe the webhook you’re creating.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookCreateRequest.Data.Attributes
```

## Properties

- `name` (string) *(required)*: The name of the webhook.
- `enabled` (boolean) *(required)*: A Boolean value that indicates whether the webhook is enabled.
- `eventTypes` ([WebhookEventType]) *(required)*: The event types that the webhook subscribes to. See [`WebhookEventType`](../../webhookeventtype.md) for possible values.
- `secret` (string) *(required)*: The secret for the webhook. The API doesn’t return this value in responses.
- `url` (uri) *(required)*: The URL that receives webhook event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookcreaterequest/data-data.dictionary/attributes-data.dictionary)*
# Webhook.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a webhook resource.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object Webhook.Attributes
```

## Properties

- `name` (string): The name of the webhook.
- `enabled` (boolean): A Boolean value that indicates whether the webhook is enabled.
- `eventTypes` ([WebhookEventType]): The event types that the webhook subscribes to. See [`WebhookEventType`](../webhookeventtype.md) for possible values.
- `url` (uri): The URL that receives webhook event notifications.
- `createdDateTime` (date-time): The date and time that the webhook was created.
- `updatedDateTime` (date-time): The date and time that the webhook was last updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhook/attributes-data.dictionary)*
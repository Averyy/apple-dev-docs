# AuditEventWebhookCreated

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents the event data for a webhook created audit event.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object AuditEventWebhookCreated
```

## Properties

- `name` (string): The name of the webhook.
- `enabled` (string): Indicates whether the webhook is enabled.
- `eventTypes` ([string]): The event types that the webhook subscribes to.
- `url` (string): The URL that receives webhook event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditeventwebhookcreated)*
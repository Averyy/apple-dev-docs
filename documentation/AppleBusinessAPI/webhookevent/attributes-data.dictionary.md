# WebhookEvent.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a webhook event resource.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookEvent.Attributes
```

## Properties

- `eventType` (WebhookEventType): The type of event. See [`WebhookEventType`](../webhookeventtype.md) for possible values.
- `payload` (string): The payload of the event.
- `isPingEvent` (boolean): A Boolean value that indicates whether the event is a ping event.
- `createdDateTime` (date-time): The date and time that the event was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookevent/attributes-data.dictionary)*
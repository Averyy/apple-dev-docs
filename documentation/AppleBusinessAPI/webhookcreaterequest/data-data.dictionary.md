# WebhookCreateRequest.Data

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookCreateRequest.Data
```

## Topics

### Dictionaries
- [object WebhookCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe the webhook you’re creating.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `webhooks`
- `attributes` (WebhookCreateRequest.Data.Attributes) *(required)*: The attributes for the new webhook.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookcreaterequest/data-data.dictionary)*
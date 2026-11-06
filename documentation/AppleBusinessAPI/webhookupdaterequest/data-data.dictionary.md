# WebhookUpdateRequest.Data

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookUpdateRequest.Data
```

## Topics

### Dictionaries
- [object WebhookUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes with values that you’re changing as part of the update request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `webhooks`
- `id` (string) *(required)*: The unique identifier of the webhook to update.
- `attributes` (WebhookUpdateRequest.Data.Attributes): The attributes to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookupdaterequest/data-data.dictionary)*
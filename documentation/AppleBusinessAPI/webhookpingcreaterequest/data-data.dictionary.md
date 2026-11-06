# WebhookPingCreateRequest.Data

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookPingCreateRequest.Data
```

## Topics

### Dictionaries
- [object WebhookPingCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `webhookPings`
- `relationships` (WebhookPingCreateRequest.Data.Relationships) *(required)*: The relationships you include in the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookpingcreaterequest/data-data.dictionary)*
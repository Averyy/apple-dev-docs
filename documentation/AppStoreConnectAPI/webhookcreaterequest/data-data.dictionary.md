# WebhookCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a webhook.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object WebhookCreateRequest.Data
```

## Topics

### Dictionaries
- [object WebhookCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a webhook create request resource.
- [object WebhookCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (WebhookCreateRequest.Data.Attributes) *(required)*
- `relationships` (WebhookCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `webhooks`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhookcreaterequest/data-data.dictionary)*
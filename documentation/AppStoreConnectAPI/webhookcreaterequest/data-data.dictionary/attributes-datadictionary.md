# WebhookCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a webhook create request resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object WebhookCreateRequest.Data.Attributes
```

## Mentions

- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)

## Properties

- `enabled` (boolean) *(required)*
- `eventTypes` ([WebhookEventType]) *(required)*
- `name` (string) *(required)*
- `secret` (string) *(required)*: An arbitrary string. Alternative marketplaces use this secret string to verify incoming requests from Apple about changes to apps. For more information about webhook-style validation, see Github’s Validating webhook deliveries. For more information about implementing Hash-based Message Authentication Code (HMAC) security in your notifications webhook, see the “Set up notification authentication” section of [`Configuring and parsing App Store Connect API webhook notifications`](configuring-webhook-notifications.md).
- `url` (uri) *(required)*: The endpoint URL for your server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhookcreaterequest/data-data.dictionary/attributes-data.dictionary)*
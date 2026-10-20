# MarketplaceWebhookUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a marketplace webhook resource.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```
object MarketplaceWebhookUpdateRequest.Data.Attributes
```

## Properties

- `endpointUrl` (uri)
- `secret` (string): An arbitrary string. Alternative marketplaces use this secret string to verify the incoming requests from Apple about changes to apps. For more information about webhook-style validation, see [Github’s Validating webhook deliveries](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries#about-validating-webhook-deliveries).

  For more information about implementing Hash-based Message Authentication Code (HMAC) security in your notifications webhook, see [Processing alternative app marketplace notifications](../../../MarketplaceKit/processing-alternative-marketplace-notifications.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/marketplacewebhookupdaterequest/data-data.dictionary/attributes-data.dictionary)*
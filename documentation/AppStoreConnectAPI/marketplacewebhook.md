# MarketplaceWebhook

**Framework**: App Store Connect API  
**Kind**: dictionary

A webhook endpoint that receives event notifications from an alternative marketplace, such as app availability changes.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object MarketplaceWebhook
```

## Topics

### Objects
- [object MarketplaceWebhook.Attributes](marketplacewebhook/attributes-data.dictionary.md)
  The attribute that describes the url where you receive notifications.

## Properties

- `attributes` (MarketplaceWebhook.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object MarketplaceWebhookCreateRequest](marketplacewebhookcreaterequest.md)
  The request body you use to create a marketplace webhook url.
- [object MarketplaceWebhookResponse](marketplacewebhookresponse.md)
  A response containing a single marketplace webhook endpoint configuration.
- [object MarketplaceWebhooksResponse](marketplacewebhooksresponse.md)
  A response containing a list of webhook endpoints for an alternative marketplace.
- [object MarketplaceWebhookUpdateRequest](marketplacewebhookupdaterequest.md)
  The request body you use to update a marketplace webhook url.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/marketplacewebhook)*
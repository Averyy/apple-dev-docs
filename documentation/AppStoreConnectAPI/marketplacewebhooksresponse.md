# MarketplaceWebhooksResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of webhook endpoints for an alternative marketplace.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object MarketplaceWebhooksResponse
```

#### Discussion

Use this object with [`Read Marketplace Webhook Information`](get-v1-marketplacewebhooks.md).

## Properties

- `data` ([MarketplaceWebhook]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object MarketplaceWebhook](marketplacewebhook.md)
  A webhook endpoint that receives event notifications from an alternative marketplace, such as app availability changes.
- [object MarketplaceWebhookCreateRequest](marketplacewebhookcreaterequest.md)
  The request body you use to create a marketplace webhook url.
- [object MarketplaceWebhookResponse](marketplacewebhookresponse.md)
  A response containing a single marketplace webhook endpoint configuration.
- [object MarketplaceWebhookUpdateRequest](marketplacewebhookupdaterequest.md)
  The request body you use to update a marketplace webhook url.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/marketplacewebhooksresponse)*
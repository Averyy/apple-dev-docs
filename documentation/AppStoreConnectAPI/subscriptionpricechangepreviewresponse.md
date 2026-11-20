# SubscriptionPriceChangePreviewResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create a subscription price change preview.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceChangePreviewResponse
```

## Properties

- `data` (SubscriptionPriceChangePreview) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects and types
- [object SubscriptionPriceChangePreview](./subscriptionpricechangepreview.md)
  The result of previewing a subscription price change in each proposed territory.
- [object SubscriptionPriceChangePreviewCreateRequest](./subscriptionpricechangepreviewcreaterequest.md)
  The request body you use to create a subscription price change preview.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricechangepreviewresponse)*
# SubscriptionPriceChangePreview

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The result of previewing a subscription price change in each proposed territory.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceChangePreview
```

## Topics

### Objects
- [object SubscriptionPriceChangePreview.Attributes](./subscriptionpricechangepreview/attributes-data.dictionary.md)
  Attributes that describe a subscription price change preview resource.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionPriceChangePreviews`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (SubscriptionPriceChangePreview.Attributes): The resource’s attributes.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
- [object SubscriptionPriceChangePreviewCreateRequest](./subscriptionpricechangepreviewcreaterequest.md)
  The request body you use to create a subscription price change preview.
- [object SubscriptionPriceChangePreviewResponse](./subscriptionpricechangepreviewresponse.md)
  The response body for endpoints that create a subscription price change preview.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricechangepreview)*
# ProposedSubscriptionPriceTier

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A volume pricing tier that you propose for a territory.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object ProposedSubscriptionPriceTier
```

## Properties

- `minQuantity` (integer) *(required)*: The lowest number of seats the tier applies to.
- `subscriptionPricePointId` (string) *(required)*: The ID of the price point that sets the per-seat price for the tier.

## See Also

### Objects and types
- [object SubscriptionPriceChangePreview](./subscriptionpricechangepreview.md)
  The result of previewing a subscription price change in each proposed territory.
- [object SubscriptionPriceChangePreviewCreateRequest](./subscriptionpricechangepreviewcreaterequest.md)
  The request body you use to create a subscription price change preview.
- [object SubscriptionPriceChangePreviewResponse](./subscriptionpricechangepreviewresponse.md)
  The response body for endpoints that create a subscription price change preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/proposedsubscriptionpricetier)*
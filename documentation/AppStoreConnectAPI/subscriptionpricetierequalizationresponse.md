# SubscriptionPriceTierEqualizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create a subscription price tier equalization.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTierEqualizationResponse
```

## Properties

- `data` (SubscriptionPriceTierEqualization) *(required)*: The resource data.
- `included` ([SubscriptionPricePoint]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects and types
- [object SubscriptionPriceTierEqualization](./subscriptionpricetierequalization.md)
  The equalized volume pricing tiers for each territory, calculated from a base territory’s tiers.
- [object SubscriptionPriceTierEqualizationCreateRequest](./subscriptionpricetierequalizationcreaterequest.md)
  The request body you use to create a subscription price tier equalization.
- [object SubscriptionEqualizedPriceTiersForTerritory](./subscriptionequalizedpricetiersforterritory.md)
  The equalized volume pricing tiers for a single territory.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetierequalizationresponse)*
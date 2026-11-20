# SubscriptionEqualizedPriceTiersForTerritory

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The equalized volume pricing tiers for a single territory.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionEqualizedPriceTiersForTerritory
```

## Properties

- `territoryId` (string): The three-letter code of the territory.
- `basePricePointId` (string): The ID of the price point that sets the single-seat price in the territory.
- `additionalPriceTiers` ([ProposedSubscriptionPriceTier]): The equalized tiers for the territory, each with a minimum seat count and a price point.

## See Also

### Objects and types
- [object SubscriptionPriceTierEqualization](./subscriptionpricetierequalization.md)
  The equalized volume pricing tiers for each territory, calculated from a base territory’s tiers.
- [object SubscriptionPriceTierEqualizationCreateRequest](./subscriptionpricetierequalizationcreaterequest.md)
  The request body you use to create a subscription price tier equalization.
- [object SubscriptionPriceTierEqualizationResponse](./subscriptionpricetierequalizationresponse.md)
  The response body for endpoints that create a subscription price tier equalization.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionequalizedpricetiersforterritory)*
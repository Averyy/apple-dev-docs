# SubscriptionPriceTierEqualizationCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a subscription price tier equalization.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTierEqualizationCreateRequest
```

## Topics

### Objects
- [object SubscriptionPriceTierEqualizationCreateRequest.Data](./subscriptionpricetierequalizationcreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (SubscriptionPriceTierEqualizationCreateRequest.Data) *(required)*: The data element of the request body.

## See Also

### Objects and types
- [object SubscriptionPriceTierEqualization](./subscriptionpricetierequalization.md)
  The equalized volume pricing tiers for each territory, calculated from a base territory’s tiers.
- [object SubscriptionPriceTierEqualizationResponse](./subscriptionpricetierequalizationresponse.md)
  The response body for endpoints that create a subscription price tier equalization.
- [object SubscriptionEqualizedPriceTiersForTerritory](./subscriptionequalizedpricetiersforterritory.md)
  The equalized volume pricing tiers for a single territory.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetierequalizationcreaterequest)*
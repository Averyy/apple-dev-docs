# SubscriptionPriceTierEqualization

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The equalized volume pricing tiers for each territory, calculated from a base territory’s tiers.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTierEqualization
```

## Topics

### Objects
- [object SubscriptionPriceTierEqualization.Attributes](./subscriptionpricetierequalization/attributes-data.dictionary.md)
  Attributes that describe a subscription price tier equalization resource.
- [object SubscriptionPriceTierEqualization.Relationships](./subscriptionpricetierequalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionPriceTierEqualizations`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (SubscriptionPriceTierEqualization.Attributes): The resource’s attributes.
- `relationships` (SubscriptionPriceTierEqualization.Relationships): Navigational links to related data and included resource types and IDs.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
- [object SubscriptionPriceTierEqualizationCreateRequest](./subscriptionpricetierequalizationcreaterequest.md)
  The request body you use to create a subscription price tier equalization.
- [object SubscriptionPriceTierEqualizationResponse](./subscriptionpricetierequalizationresponse.md)
  The response body for endpoints that create a subscription price tier equalization.
- [object SubscriptionEqualizedPriceTiersForTerritory](./subscriptionequalizedpricetiersforterritory.md)
  The equalized volume pricing tiers for a single territory.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetierequalization)*
# SubscriptionPriceTier

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A volume pricing tier that sets a per-seat price from a minimum number of seats.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTier
```

## Topics

### Objects
- [object SubscriptionPriceTier.Attributes](./subscriptionpricetier/attributes-data.dictionary.md)
  Attributes that describe a subscription price tier resource.
- [object SubscriptionPriceTier.Relationships](./subscriptionpricetier/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionPriceTiers`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (SubscriptionPriceTier.Attributes): The resource’s attributes.
- `relationships` (SubscriptionPriceTier.Relationships): Navigational links to related data and included resource types and IDs.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
- [object SubscriptionPriceTierInlineCreate](./subscriptionpricetierinlinecreate.md)
  A volume pricing tier that you create inline with a subscription price.
- [object SubscriptionPriceTiersResponse](./subscriptionpricetiersresponse.md)
  The response body for endpoints that list subscription price tiers.
- [object SubscriptionPriceAdditionalPriceTiersLinkagesResponse](./subscriptionpriceadditionalpricetierslinkagesresponse.md)
  The response body for endpoints that list the IDs of a subscription price’s additional price tiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetier)*
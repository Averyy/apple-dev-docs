# SubscriptionPriceTierInlineCreate

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A volume pricing tier that you create inline with a subscription price.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTierInlineCreate
```

## Topics

### Objects
- [object SubscriptionPriceTierInlineCreate.Attributes](./subscriptionpricetierinlinecreate/attributes-data.dictionary.md)
  The attributes you include in the request.
- [object SubscriptionPriceTierInlineCreate.Relationships](./subscriptionpricetierinlinecreate/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionPriceTiers`
- `id` (string): An opaque resource ID that uniquely identifies the resource.
- `attributes` (SubscriptionPriceTierInlineCreate.Attributes): The resource’s attributes.
- `relationships` (SubscriptionPriceTierInlineCreate.Relationships): Navigational links to related data and included resource types and IDs.

## See Also

### Objects and types
- [object SubscriptionPriceTier](./subscriptionpricetier.md)
  A volume pricing tier that sets a per-seat price from a minimum number of seats.
- [object SubscriptionPriceTiersResponse](./subscriptionpricetiersresponse.md)
  The response body for endpoints that list subscription price tiers.
- [object SubscriptionPriceAdditionalPriceTiersLinkagesResponse](./subscriptionpriceadditionalpricetierslinkagesresponse.md)
  The response body for endpoints that list the IDs of a subscription price’s additional price tiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetierinlinecreate)*
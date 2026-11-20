# SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships.Subscription](./relationships-data.dictionary/subscription-data.dictionary.md)
  The subscription to equalize tiers for.
- [object SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships.BasePricePoint](./relationships-data.dictionary/basepricepoint-data.dictionary.md)
  The price point that sets the single-seat price in the base territory.

## Properties

- `subscription` (SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships.Subscription) *(required)*: The subscription to equalize tiers for.
- `basePricePoint` (SubscriptionPriceTierEqualizationCreateRequest.Data.Relationships.BasePricePoint) *(required)*: The price point that sets the single-seat price in the base territory.

## See Also

### Objects
- [object SubscriptionPriceTierEqualizationCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you include in the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricetierequalizationcreaterequest/data-data.dictionary/relationships-data.dictionary)*
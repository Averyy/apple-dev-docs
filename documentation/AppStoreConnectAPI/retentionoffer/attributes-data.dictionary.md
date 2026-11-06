# RetentionOffer.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a retention offer resource.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOffer.Attributes
```

## Properties

- `referenceName` (string): A name for the retention offer that you use in App Store Connect.
- `offerId` (string): An identifier for the offer that you define, which identifies the offer in StoreKit.
- `duration` (SubscriptionOfferDuration): The length of time for each offer period. The total length of the offer is the duration multiplied by the period count.
- `offerMode` (SubscriptionOfferMode): The payment mode for the offer.
- `periodCount` (integer): The number of offer periods.
- `customerEligibilityPaidSubscriptionDurationInMonths` (integer): The minimum number of months of paid subscription that makes a person eligible for the offer. Possible values are 1 to 24, 36, 48, and 60.
- `customerEligibilityWaitBetweenOffersInMonths` (integer): The number of months a person waits before they can redeem another retention offer for the same subscription. Possible values are 2 to 24.
- `targetSubscriptionPlanType` (SubscriptionPlanType): The subscription plan type that people subscribe to after the offer ends.

## See Also

### Objects
- [object RetentionOffer.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionoffer/attributes-data.dictionary)*
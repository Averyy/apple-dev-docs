# RetentionOfferCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that you set that describe the new resource.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferCreateRequest.Data.Attributes
```

## Properties

- `referenceName` (string) *(required)*: A name for the retention offer that you use in App Store Connect.
- `offerId` (string) *(required)*: An identifier for the offer that you define, which identifies the offer in StoreKit. It can contain only alphanumeric characters, underscores, and periods.
- `duration` (SubscriptionOfferDuration) *(required)*: The length of time for each offer period. The total length of the offer is the duration multiplied by the period count.
- `offerMode` (SubscriptionOfferMode) *(required)*: The payment mode for the offer.
- `periodCount` (integer) *(required)*: The number of offer periods.
- `customerEligibilityPaidSubscriptionDurationInMonths` (integer) *(required)*: The minimum number of months of paid subscription that makes a person eligible for the offer. Possible values are 1 to 24, 36, 48, and 60.
- `customerEligibilityWaitBetweenOffersInMonths` (integer): The number of months a person waits before they can redeem another retention offer for the same subscription. Possible values are 2 to 24.
- `targetSubscriptionPlanType` (SubscriptionPlanType): The subscription plan type that people subscribe to after the offer ends. A subscription can have up to 10 active retention offers for each plan type.

## See Also

### Objects
- [object RetentionOfferCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionoffercreaterequest/data-data.dictionary/attributes-data.dictionary)*
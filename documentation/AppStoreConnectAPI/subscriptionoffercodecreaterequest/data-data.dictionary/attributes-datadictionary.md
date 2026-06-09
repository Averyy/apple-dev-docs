# SubscriptionOfferCodeCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a subscription offer code create request resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionOfferCodeCreateRequest.Data.Attributes
```

## Properties

- `autoRenewEnabled` (boolean)
- `customerEligibilities` ([SubscriptionCustomerEligibility]) *(required)*
- `duration` (SubscriptionOfferDuration) *(required)*
- `name` (string) *(required)*
- `numberOfPeriods` (integer) *(required)*
- `offerEligibility` (SubscriptionOfferEligibility) *(required)*
- `offerMode` (SubscriptionOfferMode) *(required)*
- `targetSubscriptionPlanType` (SubscriptionPlanType)

## See Also

- [object SubscriptionOfferCodeCreateRequest.Data.Relationships](subscriptionoffercodecreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffercodecreaterequest/data-data.dictionary/attributes-data.dictionary)*
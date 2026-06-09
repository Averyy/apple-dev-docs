# SubscriptionOfferCode.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a subscription offer code resource.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionOfferCode.Attributes
```

## Properties

- `active` (boolean)
- `autoRenewEnabled` (boolean)
- `customerEligibilities` ([SubscriptionCustomerEligibility])
- `duration` (SubscriptionOfferDuration)
- `name` (string)
- `numberOfPeriods` (integer)
- `offerEligibility` (SubscriptionOfferEligibility)
- `offerMode` (SubscriptionOfferMode)
- `productionCodeCount` (integer)
- `sandboxCodeCount` (integer)
- `targetSubscriptionPlanType` (SubscriptionPlanType)
- `totalNumberOfCodes` (integer)

## See Also

- [type SubscriptionOfferDuration](subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionOfferEligibility](subscriptionoffereligibility.md)
  A string that represents the eligibility of a subscription offer.
- [type SubscriptionCustomerEligibility](subscriptioncustomereligibility.md)
  A string that represents a customer’s eligibility for a subscription offer.
- [type SubscriptionOfferMode](subscriptionoffermode.md)
  A string that indicates the payment mode of a subscription offer.
- [object SubscriptionOfferCode.Relationships](subscriptionoffercode/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffercode/attributes-data.dictionary)*
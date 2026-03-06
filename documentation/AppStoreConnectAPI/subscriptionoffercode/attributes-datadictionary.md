# SubscriptionOfferCode.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

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
- `totalNumberOfCodes` (integer)

## See Also

- [type SubscriptionOfferDuration](subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionOfferEligibility](subscriptionoffereligibility.md)
- [type SubscriptionCustomerEligibility](subscriptioncustomereligibility.md)
- [type SubscriptionOfferMode](subscriptionoffermode.md)
  A string that indicates the payment mode of a subscription offer.
- [object SubscriptionOfferCode.Relationships](subscriptionoffercode/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffercode/attributes-data.dictionary)*
# SubscriptionOfferMode

**Framework**: App Store Connect API  
**Kind**: typealias

A string that indicates the payment mode of a subscription offer.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
string SubscriptionOfferMode
```

#### Discussion

##### Possible Alues

- **PAY_AS_YOU_GO**: A constant that indicates a subscription offer is billed over multiple billing periods.
- **PAY_UP_FRONT**: A constant that indicates a subscription offer is billed one time, up front.
- **FREE_TRIAL**: A constant that indicates a subscription offer is a free trial.

## See Also

- [object SubscriptionOfferCode.Attributes](subscriptionoffercode/attributes-data.dictionary.md)
- [type SubscriptionOfferDuration](subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionOfferEligibility](subscriptionoffereligibility.md)
- [type SubscriptionCustomerEligibility](subscriptioncustomereligibility.md)
- [object SubscriptionOfferCode.Relationships](subscriptionoffercode/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffermode)*
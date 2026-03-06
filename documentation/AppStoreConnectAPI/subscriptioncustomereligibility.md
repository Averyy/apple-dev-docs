# SubscriptionCustomerEligibility

**Framework**: App Store Connect API  
**Kind**: typealias

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
string SubscriptionCustomerEligibility
```

#### Possible Values

- **`NEW`**: A customer who has not previously subscribed to this subscription.
- **`EXISTING`**: A customer who is currently subscribed to this subscription.
- **`EXPIRED`**: A customer who was but is not currently subscribed to this subscription.

## See Also

- [object SubscriptionOfferCode.Attributes](subscriptionoffercode/attributes-data.dictionary.md)
- [type SubscriptionOfferDuration](subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionOfferEligibility](subscriptionoffereligibility.md)
- [type SubscriptionOfferMode](subscriptionoffermode.md)
  A string that indicates the payment mode of a subscription offer.
- [object SubscriptionOfferCode.Relationships](subscriptionoffercode/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptioncustomereligibility)*
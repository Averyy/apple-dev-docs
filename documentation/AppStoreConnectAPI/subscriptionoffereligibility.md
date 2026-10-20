# SubscriptionOfferEligibility

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

A string that represents the eligibility of a subscription offer.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
string SubscriptionOfferEligibility
```

## Possible Values

- `STACK_WITH_INTRO_OFFERS`: A subscription offer that customers can combine with an introductory offer.
- `REPLACE_INTRO_OFFERS`: A subscription offer that replaces an introductory offer.

## See Also

### Objects and types
- [object SubscriptionOfferCode.Attributes](./subscriptionoffercode/attributes-data.dictionary.md)
  Attributes that describe a subscription offer code resource.
- [type SubscriptionOfferDuration](./subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionCustomerEligibility](./subscriptioncustomereligibility.md)
  A string that represents a customer’s eligibility for a subscription offer.
- [type SubscriptionOfferMode](./subscriptionoffermode.md)
  A string that indicates the payment mode of a subscription offer.
- [object SubscriptionOfferCode.Relationships](./subscriptionoffercode/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffereligibility)*
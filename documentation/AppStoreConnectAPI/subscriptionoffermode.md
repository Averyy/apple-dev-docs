# SubscriptionOfferMode

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

A string that indicates the payment mode of a subscription offer.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
string SubscriptionOfferMode
```

## Possible Values

- `PAY_AS_YOU_GO`: A constant that indicates a subscription offer is billed over multiple billing periods.
- `PAY_UP_FRONT`: A constant that indicates a subscription offer is billed one time, up front.
- `FREE_TRIAL`: A constant that indicates a subscription offer is a free trial.

## Discussion

## See Also

### Objects and types
- [object SubscriptionOfferCode.Attributes](./subscriptionoffercode/attributes-data.dictionary.md)
  Attributes that describe a subscription offer code resource.
- [type SubscriptionOfferDuration](./subscriptionofferduration.md)
  A length of time that can be assigned to a subscription.
- [type SubscriptionOfferEligibility](./subscriptionoffereligibility.md)
  A string that represents the eligibility of a subscription offer.
- [type SubscriptionCustomerEligibility](./subscriptioncustomereligibility.md)
  A string that represents a customer’s eligibility for a subscription offer.
- [object SubscriptionOfferCode.Relationships](./subscriptionoffercode/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionoffermode)*
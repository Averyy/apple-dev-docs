# gracePeriodExpirationDate

**Framework**: StoreKit  
**Kind**: property

The date the billing grace period expires for the auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let gracePeriodExpirationDate: Date?
```

## Mentions

- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Discussion

This value is `nil` if the subscription is not in a billing grace period.

This date is present if you enable Billing Grace Period for your app and the subscription is in the billing grace period. Ensure that your app provides full service for the subscription throughout the grace period, which ends on the [`gracePeriodExpirationDate`](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md).

A billing grace period occurs at the start of a billing retry state. Throughout the billing grace period, the value of [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) is `true`, which indicates that Apple is attempting to automatically renew the subscription.

For information about supporting Billing Grace Period, see [`Enable Billing Grace Period for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev58bda3212) and [`Reducing Involuntary Subscriber Churn`](reducing-involuntary-subscriber-churn.md).

## See Also

- [let isInBillingRetry: Bool](product/subscriptioninfo/renewalinfo/isinbillingretry.md)
  A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/graceperiodexpirationdate)*
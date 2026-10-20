# isInBillingRetry

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let isInBillingRetry: Bool
```

## Mentions

- [Testing failing subscription renewals and Apple In-App Purchases](../../../testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Discussion

This field indicates whether Apple is attempting to automatically renew an expired subscription. If a subscription expires due to a billing issue, a value of `true` indicates that Apple is still trying to renew the subscription. If the subscription is in a billing grace period, the optional [`gracePeriodExpirationDate`](./graceperiodexpirationdate.md) contains a date.

Use the [`isInBillingRetry`](./isinbillingretry.md) value along with [`expirationReason`](./expirationreason-swift.property.md) for more insight, as the following table shows:

| Values | Description |
| --- | --- |
| [`isInBillingRetry`](./isinbillingretry.md) is `false,` ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png)  [`expirationReason`](./expirationreason-swift.property.md) is `nil` | The auto-renewable subscription is active and not in a billing retry period.  ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) The subscription is entitled to service. |
| [`isInBillingRetry`](./isinbillingretry.md) is `true,` ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) [`expirationReason`](./expirationreason-swift.property.md) is [`billingError`](./expirationreason-swift.struct/billingerror.md), ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) [`gracePeriodExpirationDate`](./graceperiodexpirationdate.md) has a date | The auto-renewable subscription is in a billing grace period.  ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) The subscription is entitled to service until the date in [`gracePeriodExpirationDate`](./graceperiodexpirationdate.md). |
| [`isInBillingRetry`](./isinbillingretry.md) is `true,` ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) [`expirationReason`](./expirationreason-swift.property.md) is [`billingError`](./expirationreason-swift.struct/billingerror.md), ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) [`gracePeriodExpirationDate`](./graceperiodexpirationdate.md) is `nil` | The auto-renewable subscription is in a billing retry period.  ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) The subscription is not entitled to service. |
| [`isInBillingRetry`](./isinbillingretry.md) is `false,`  ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) [`expirationReason`](./expirationreason-swift.property.md) is [`billingError`](./expirationreason-swift.struct/billingerror.md) | The auto-renewable subscription expired and billing retry wasn’t able to recover the subscription. ![](https://developer.apple.com/tutorials/images/com.apple.storekit/spacer.png) The subscription is not entitled to service. |

## See Also

### Getting billing status
- [let gracePeriodExpirationDate: Date?](./graceperiodexpirationdate.md)
  The date the billing grace period expires for the auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/isinbillingretry)*
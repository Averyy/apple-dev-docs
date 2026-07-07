# isInBillingRetry

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let isInBillingRetry: Bool
```

## Mentions

- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Discussion

This field indicates whether Apple is attempting to automatically renew an expired subscription. If a subscription expires due to a billing issue, a value of `true` indicates that Apple is still trying to renew the subscription. If the subscription is in a billing grace period, the optional [`gracePeriodExpirationDate`](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md) contains a date.

Use the [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) value along with [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) for more insight, as the following table shows:

| Values | Description |
| --- | --- |
| [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) is `false,` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)  [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) is `nil` | The auto-renewable subscription is active and not in a billing retry period.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is entitled to service. |
| [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) is `true,` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) is [`billingError`](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md), ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`gracePeriodExpirationDate`](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md) has a date | The auto-renewable subscription is in a billing grace period.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is entitled to service until the date in [`gracePeriodExpirationDate`](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md). |
| [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) is `true,` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) is [`billingError`](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md), ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`gracePeriodExpirationDate`](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md) is `nil` | The auto-renewable subscription is in a billing retry period.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is not entitled to service. |
| [`isInBillingRetry`](product/subscriptioninfo/renewalinfo/isinbillingretry.md) is `false,`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`expirationReason`](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md) is [`billingError`](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/billingerror.md) | The auto-renewable subscription expired and billing retry wasn’t able to recover the subscription. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The subscription is not entitled to service. |

## See Also

- [let gracePeriodExpirationDate: Date?](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md)
  The date the billing grace period expires for the auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/isinbillingretry)*
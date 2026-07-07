# revocationPercentage

**Framework**: StoreKit  
**Kind**: property

The percentage of the transaction amount that the App Store has refunded or revoked, expressed as a decimal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 26.4, macOS 26.4, tvOS 26.4, watchOS 26.4, visionOS 26.4)
var revocationPercentage: Decimal? { get }
```

#### Discussion

This property indicates the rounded percentage of the purchase amount that the App Store has refunded or revoked.

The value is present only for transactions with a non-reversed refund. Valid values range from 0.0 to 100.0:

- For auto-renewable subscriptions: 0.0-100.0% based on time remaining in the subscription period
- For consumables, non-consumables, and non-renewing subscriptions: 0.0-100.0% based on consumption data

If the purchase had a quantity greater than 1, this percentage applies to the full quantity. For example, if 1 of 3 items was refunded, the value would be approximately 33.333. The following table shows several examples of revocation percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

> **Note**: This property is not present for Advanced Commerce transactions, which use [`amount`](transaction/advancedcommerceinfo-swift.struct/refund/amount.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationpercentage)*
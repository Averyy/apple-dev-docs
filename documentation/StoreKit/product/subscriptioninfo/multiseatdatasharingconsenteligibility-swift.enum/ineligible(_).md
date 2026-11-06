# Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.ineligible(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A value that indicates that the person signed in to the App Store can’t choose whether to share group information with you.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
case ineligible(Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason)
```

## Mentions

- [Supporting multiseat purchases in your app](../../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

The associated value gives the reason, such as [`alreadyConsented`](./ineligibilityreason/alreadyconsented.md). Don’t present the data sharing consent sheet; presenting it throws [`StoreKitError.unsupported`](../../../storekiterror/unsupported.md).

## See Also

### Identifying the eligibility
- [Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.eligible](./eligible.md)
  A value that indicates that the person signed in to the App Store can choose whether to share group information with you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/ineligible(_:))*
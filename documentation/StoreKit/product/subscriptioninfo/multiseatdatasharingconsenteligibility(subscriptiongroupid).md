# multiSeatDataSharingConsentEligibility(subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Gets a value that indicates whether you can request consent to share group information for a subscription group.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
static func multiSeatDataSharingConsentEligibility(subscriptionGroupID: String) async throws -> Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility
```

## Return Value

The eligibility, with the reason if you can’t request consent.

## Discussion

> **Throws**: [`StoreKitError.unsupported`](../../storekiterror/unsupported.md) if the person isn’t signed in to the App Store or an iOS app runs in visionOS, or another error if StoreKit can’t determine the eligibility.

## Discussion

Check the eligibility each time before you present the data sharing consent sheet. To check it for a subscription product, use [`multiSeatDataSharingConsentEligibility`](./multiseatdatasharingconsenteligibility-swift.property.md). For more information, see [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility`](./multiseatdatasharingconsenteligibility-swift.enum.md).

## Parameters

- `subscriptionGroupID`: The identifier of the subscription group to check.

## See Also

### Checking data sharing consent eligibility
- [var multiSeatDataSharingConsentEligibility: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](./multiseatdatasharingconsenteligibility-swift.property.md)
  A value that indicates whether you can request consent to share group information for this subscription’s subscription group.
- [Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](./multiseatdatasharingconsenteligibility-swift.enum.md)
  Values that indicate whether you can request consent to share group information for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility(subscriptiongroupid:))*
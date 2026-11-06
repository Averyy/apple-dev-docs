# Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values that indicate whether you can request consent to share group information for a subscription group.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
enum MultiSeatDataSharingConsentEligibility
```

## Overview

Group information is the membership of a multiseat subscription’s group. Data sharing consent applies only to subscriptions that use Apple-hosted invitations. Only the group purchaser can choose whether to share group information with you, and they can change the choice at any time in Manage Subscriptions. While they share it, the group appears in the responses from [`Get Customer Groups`](../../../AppStoreServerAPI/get-customer-groups.md) and [`Get Group Members`](../../../AppStoreServerAPI/get-group-members.md) in the App Store Server API.

Check the eligibility each time before you present the data sharing consent sheet, so you ask only the group purchaser. If you haven’t checked it since the sheet was last presented, presenting the sheet throws [`StoreKitError.unsupported`](../../storekiterror/unsupported.md). If the value is [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.ineligible(_:)`](./multiseatdatasharingconsenteligibility-swift.enum/ineligible%28_%29.md), its associated value tells you the reason. StoreKit might add eligibility values in the future, so include an `@unknown default` case when you switch over the eligibility.

The following example checks the eligibility before it presents the sheet in UIKit:

```swift
func requestGroupInformationConsent(
    for subscription: Product.SubscriptionInfo,
    from viewController: UIViewController
) async throws {
    guard try await subscription.multiSeatDataSharingConsentEligibility == .eligible else {
        return
    }
    try await AppStore.presentMultiSeatDataSharingConsentSheet(
        from: viewController,
        subscriptionGroupID: subscription.subscriptionGroupID
    )
}
```

In AppKit, call [`presentMultiSeatDataSharingConsentSheet(from:subscriptionGroupID:)`](../../appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-3j1t4.md). In SwiftUI, use the [`multiSeatDataSharingConsentSheet(isPresented:subscriptionGroupID:onCompletion:)`](../../../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) view modifier. For more information, see [Show the group in your app](../../supporting-multiseat-purchases-in-your-app.md#Show-the-group-in-your-app).

## Topics

### Identifying the eligibility
- [Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.eligible](./multiseatdatasharingconsenteligibility-swift.enum/eligible.md)
  A value that indicates that the person signed in to the App Store can choose whether to share group information with you.
- [case ineligible(Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason)](./multiseatdatasharingconsenteligibility-swift.enum/ineligible%28_%29.md)
  A value that indicates that the person signed in to the App Store can’t choose whether to share group information with you.
### Getting the reason
- [Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.IneligibilityReason](./multiseatdatasharingconsenteligibility-swift.enum/ineligibilityreason.md)
  Reasons that you can’t request consent to share group information.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Checking data sharing consent eligibility
- [var multiSeatDataSharingConsentEligibility: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](./multiseatdatasharingconsenteligibility-swift.property.md)
  A value that indicates whether you can request consent to share group information for this subscription’s subscription group.
- [static func multiSeatDataSharingConsentEligibility(subscriptionGroupID: String) async throws -> Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](./multiseatdatasharingconsenteligibility%28subscriptiongroupid%29.md)
  Gets a value that indicates whether you can request consent to share group information for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum)*
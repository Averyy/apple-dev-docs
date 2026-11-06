# presentMultiSeatDataSharingConsentSheet(from:subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the sheet in which the group purchaser decides whether to share group information with you.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func presentMultiSeatDataSharingConsentSheet(from controller: UIViewController, subscriptionGroupID: String) async throws
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

> **Throws**: [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the view controller isn’t in a window hierarchy; [`StoreKitError.unsupported`](../storekiterror/unsupported.md) if the person isn’t signed in to the App Store or isn’t eligible, if you haven’t checked the eligibility since the sheet was last presented, or if an iOS app runs in visionOS; or another error if the system can’t present the sheet.

## Discussion

Use this method to ask the group purchaser of a multiseat subscription whether to share group information, the membership of their group, with you. Data sharing consent applies only to subscriptions that use Apple-hosted invitations. While the group purchaser shares group information, the group appears in the responses from [`Get Customer Groups`](../../AppStoreServerAPI/get-customer-groups.md) and [`Get Group Members`](../../AppStoreServerAPI/get-group-members.md) in the App Store Server API. The group purchaser can change the choice at any time in Manage Subscriptions.

Each time before you present the sheet, check [`multiSeatDataSharingConsentEligibility`](../product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md), and present the sheet only if the value is [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility.eligible`](../product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.enum/eligible.md).

The App Store records the choice and doesn’t return it to your app. The method returns after the group purchaser dismisses the sheet, whatever choice they make. To present the sheet in SwiftUI, use the [`multiSeatDataSharingConsentSheet(isPresented:subscriptionGroupID:onCompletion:)`](../../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) view modifier.

For more information, see [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md).

## Parameters

- `controller`: The view controller that StoreKit uses to present the sheet. The view controller needs to be in a window hierarchy.
- `subscriptionGroupID`: The identifier of the subscription group for which you’re requesting consent.

## See Also

### Requesting data sharing consent
- [static func presentMultiSeatDataSharingConsentSheet(from: NSWindow, subscriptionGroupID: String) async throws](./presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-3j1t4.md)
  Presents the sheet in which the group purchaser decides whether to share group information with you.
- [var multiSeatDataSharingConsentEligibility: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](../product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md)
  A value that indicates whether you can request consent to share group information for this subscription’s subscription group.
- [func multiSeatDataSharingConsentSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the data sharing consent sheet, where a subscriber decides whether to share account-level data with you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmultiseatdatasharingconsentsheet(from:subscriptiongroupid:)-9gr5s)*
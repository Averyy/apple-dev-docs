# multiSeatDataSharingConsentEligibility

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether you can request consent to share group information for this subscription’s subscription group.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
var multiSeatDataSharingConsentEligibility: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility { get async throws }
```

## Mentions

- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)
- [Managing the life cycle of multiseat subscriptions](../../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)

## Discussion

Data sharing consent applies only to subscriptions that use Apple-hosted invitations. Check this value each time before you present the data sharing consent sheet. Getting the value throws [`StoreKitError.unsupported`](../../storekiterror/unsupported.md) if the person isn’t signed in to the App Store or an iOS app runs in visionOS, or another error if StoreKit can’t determine the eligibility.

For more information, see [`Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility`](./multiseatdatasharingconsenteligibility-swift.enum.md).

## See Also

### Requesting data sharing consent
- [static func presentMultiSeatDataSharingConsentSheet(from: UIViewController, subscriptionGroupID: String) async throws](../../appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-9gr5s.md)
  Presents the sheet in which the group purchaser decides whether to share group information with you.
- [static func presentMultiSeatDataSharingConsentSheet(from: NSWindow, subscriptionGroupID: String) async throws](../../appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-3j1t4.md)
  Presents the sheet in which the group purchaser decides whether to share group information with you.
- [func multiSeatDataSharingConsentSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../../../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the data sharing consent sheet, where a subscriber decides whether to share account-level data with you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property)*
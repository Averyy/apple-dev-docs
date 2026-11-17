# presentMultiSeatDataSharingConsentSheet(from:originalTransactionID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the data sharing consent sheet from a view controller, where a subscriber decides whether to share account-level data with you.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func presentMultiSeatDataSharingConsentSheet(from controller: UIViewController, originalTransactionID: UInt64) async throws
```

## Discussion

Use this method to ask a subscriber whether to share account-level data with you as part of a membership in a multi-seat subscription. The App Store records the subscriber’s decision and doesn’t return it to your app. To display the sheet using SwiftUI, see `multiSeatDataSharingConsentSheet(isPresented:originalTransactionID:onCompletion:)`.

This method returns after the subscriber dismisses the sheet, whatever choice the subscriber makes.

> **Throws**: [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the view controller isn’t in a window hierarchy, [`StoreKitError.unsupported`](../storekiterror/unsupported.md) if the user isn’t signed in to the App Store, or if the subscriber isn’t eligible or eligibility hasn’t been checked using [`multiSeatDataSharingConsentEligibility(originalTransactionID:)`](../product/subscriptioninfo/multiseatdatasharingconsenteligibility%28originaltransactionid%29.md) since the sheet was last presented, or another error if the system can’t present the sheet.

## Parameters

- `controller`: The `UIViewController` that StoreKit uses to display the sheet. The view controller must be in a window hierarchy.
- `originalTransactionID`: The original transaction identifier of the multi-seat subscription for which consent is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmultiseatdatasharingconsentsheet(from:originaltransactionid:)-8pwjw)*
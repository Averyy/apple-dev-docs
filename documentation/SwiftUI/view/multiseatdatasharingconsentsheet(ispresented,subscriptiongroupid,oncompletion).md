# multiSeatDataSharingConsentSheet(isPresented:subscriptionGroupID:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents the data sharing consent sheet, where a subscriber decides whether to share account-level data with you.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func multiSeatDataSharingConsentSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View
```

## Discussion

Use this modifier to ask a subscriber whether to share account-level data with you as part of a membership in a multi-seat subscription. The App Store records the subscriber’s decision and doesn’t return it to your app. The system presents the sheet when `isPresented` changes to `true`. The system draws the sheet out of process, so setting `isPresented` to `false` doesn’t dismiss a sheet that’s already presented. Only the subscriber can dismiss the sheet.

To display the sheet using UIKit or AppKit, see `AppStore/presentMultiSeatDataSharingConsentSheet(from:subscriptionGroupID:)`.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to `true` to cause the system to display the sheet. The system sets it to `false` when the subscriber dismisses the sheet or the sheet fails to present.
- `subscriptionGroupID`: The identifier of the subscription group for which consent is being requested.
- `onCompletion`: A closure the system calls with the result of the presentation. The closure receives a success result when the subscriber dismisses the sheet, whatever choice the subscriber makes. On failure, it receives the error that prevented the system from presenting the sheet: `StoreKitError/unsupported` if the user isn’t signed in to the App Store, or if the subscriber isn’t eligible or eligibility hasn’t been checked using `Product/SubscriptionInfo/multiSeatDataSharingConsentEligibility` since the sheet was last presented, or another error if the system can’t present the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/multiseatdatasharingconsentsheet(ispresented:subscriptiongroupid:oncompletion:))*
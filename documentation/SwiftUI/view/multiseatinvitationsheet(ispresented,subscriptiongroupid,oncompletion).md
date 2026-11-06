# multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents the Apple-owned multi-seat invitation sheet, allowing the subscriber to invite others to join their multi-seat subscription.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func multiSeatInvitationSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View
```

## Discussion

Use this modifier to let a subscriber invite people to join their multi-seat subscription from within your app. The system presents the sheet when `isPresented` changes to `true`. The system draws the sheet out of process, so setting `isPresented` to `false` doesn’t dismiss a sheet that’s already presented. Your app doesn’t receive details about the invitations the subscriber sends.

To display the sheet using UIKit or AppKit, see `AppStore/presentMultiSeatInvitationSheet(from:subscriptionGroupID:)`.

The following code example shows a view that displays the invitation sheet when the subscriber taps a button:

```swift
struct InviteMembersView: View {
    let subscriptionGroupID: String
    @State private var isPresentingInvitationSheet = false

    var body: some View {
        Button("Invite Members") {
            isPresentingInvitationSheet = true
        }
        .multiSeatInvitationSheet(
            isPresented: $isPresentingInvitationSheet,
            subscriptionGroupID: subscriptionGroupID
        )
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to `true` to cause the system to display the sheet. The system sets it back to `false` when the sheet is dismissed or fails to present.
- `subscriptionGroupID`: The subscription group identifier of the multi-seat subscription being shared.
- `onCompletion`: A closure the system calls after the sheet is dismissed or fails to present. It receives `.success` if the subscriber completes the invitation flow, or `.failure` with `StoreKitError/userCancelled` if the subscriber dismisses the sheet without completing it, or with another error if the sheet can’t be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/multiseatinvitationsheet(ispresented:subscriptiongroupid:oncompletion:))*
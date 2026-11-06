# presentMultiSeatInvitationSheet(from:subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the invitation sheet that the group purchaser uses to invite people to join a multiseat subscription.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func presentMultiSeatInvitationSheet(from window: NSWindow, subscriptionGroupID: String) async throws
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

> **Throws**: [`StoreKitError.userCancelled`](../storekiterror/usercancelled.md) if the group purchaser dismisses the sheet without completing the invitation flow, [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the window isn’t visible, or another error if the system can’t present the sheet.

## Discussion

Use this method to let the group purchaser invite people to join their multiseat subscription from within your app, for a subscription that uses Apple-hosted invitations. For a subscription that uses developer-hosted invitations, the method throws an error. The sheet handles choosing contacts and sending invitations, and your app doesn’t receive details about the invitations that the group purchaser sends.

The method completes when the sheet is dismissed. It returns normally if the group purchaser completes the invitation flow.

After a multiseat purchase, the system presents the sheet automatically unless you turn it off with [`multiSeatInvitationSheetSuppressed(_:)`](../product/purchaseoption/multiseatinvitationsheetsuppressed%28_%29.md). To present the sheet in SwiftUI, use the [`multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)`](../../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) view modifier.

For more information, see [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md).

## Parameters

- `window`: The window that StoreKit uses to present the sheet. The window needs to be visible.
- `subscriptionGroupID`: The identifier of the subscription group that contains the multiseat subscription.

## See Also

### Inviting people to a group
- [static func presentMultiSeatInvitationSheet(from: UIViewController, subscriptionGroupID: String) async throws](./presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-5cmtd.md)
  Presents the invitation sheet that the group purchaser uses to invite people to join a multiseat subscription.
- [func multiSeatInvitationSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the Apple-owned multi-seat invitation sheet, allowing the subscriber to invite others to join their multi-seat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmultiseatinvitationsheet(from:subscriptiongroupid:)-ni0z)*
# presentMultiSeatInvitationSheet(from:originalTransactionID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the Apple-owned multi-seat invitation sheet from a window, so a subscriber can invite others to join their subscription.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func presentMultiSeatInvitationSheet(from window: NSWindow, originalTransactionID: UInt64) async throws
```

## Discussion

Use this method to let a subscriber invite people to join their multi-seat subscription from within your app. The sheet handles contact selection and invitation delivery. To display the sheet using SwiftUI, see `multiSeatInvitationSheet(isPresented:originalTransactionID:onCompletion:)`.

This method completes when the sheet is dismissed. It returns normally if the subscriber completes the invitation flow, and throws [`StoreKitError.userCancelled`](../storekiterror/usercancelled.md) if the subscriber dismisses the sheet without completing it. Your app doesn’t receive details about the invitations the subscriber sends.

> **Throws**: [`StoreKitError.userCancelled`](../storekiterror/usercancelled.md) if the subscriber dismisses the sheet without completing the invitation flow, [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the window isn’t visible, or another error if the system can’t present the sheet.

## Parameters

- `window`: The `NSWindow` that StoreKit uses to display the sheet. The window must be visible.
- `originalTransactionID`: The original transaction identifier of the multi-seat subscription being shared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/presentmultiseatinvitationsheet(from:originaltransactionid:)-6bty5)*
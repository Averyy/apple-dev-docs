# MultiSeatInvitationBehavior

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The behavior of the invitation sheet that the system presents after a customer buys a multiseat subscription in a StoreKit view.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
struct MultiSeatInvitationBehavior
```

## Overview

When a multiseat subscription uses Apple-hosted invitations, the system presents a sheet after the purchase that the group purchaser uses to invite people to join. To set the behavior for StoreKit views within a view hierarchy, use the [`multiSeatInvitationBehavior(_:)`](../SwiftUI/view/multiseatinvitationbehavior%28_%29.md) view modifier. Subscriptions that use developer-hosted invitations don’t show the sheet.

For purchases that you start with [`purchase(options:)`](./product/purchase%28options%29.md), use [`multiSeatInvitationSheetSuppressed(_:)`](./product/purchaseoption/multiseatinvitationsheetsuppressed%28_%29.md) instead.

For more information, see [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md).

## Topics

### Getting the behaviors
- [static let automatic: MultiSeatInvitationBehavior](./multiseatinvitationbehavior/automatic.md)
  A behavior in which the system presents the invitation sheet inline, right after the customer buys a multiseat subscription.
- [static let manual: MultiSeatInvitationBehavior](./multiseatinvitationbehavior/manual.md)
  A behavior in which the system doesn’t present the invitation sheet after a purchase.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inviting people to a group
- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [func multiSeatInvitationBehavior(MultiSeatInvitationBehavior) -> some View
](../SwiftUI/view/multiseatinvitationbehavior%28_%29.md)
  Sets the behavior of the Apple-owned invitation sheet that appears after a customer purchases a multi-seat subscription from a StoreKit view.
- [func multiSeatInvitationSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the Apple-owned multi-seat invitation sheet, allowing the subscriber to invite others to join their multi-seat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/multiseatinvitationbehavior)*
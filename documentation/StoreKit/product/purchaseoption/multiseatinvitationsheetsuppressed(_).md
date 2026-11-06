# multiSeatInvitationSheetSuppressed(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Turns off the invitation sheet that the system presents after a multiseat subscription purchase with Apple-hosted invitations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 27.3, macOS 27.3, tvOS 27.3, watchOS 27.3, visionOS 27.3)
static func multiSeatInvitationSheetSuppressed(_ isSuppressed: Bool) -> Product.PurchaseOption
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)

## Return Value

An instance of [`Product.PurchaseOption`](../purchaseoption.md) to use in [`purchase(options:)`](../purchase%28options%29.md).

## Discussion

When a multiseat subscription uses Apple-hosted invitations, the system presents a sheet after the purchase that the group purchaser uses to invite people to join. Add this option with a value of `true` to present the sheet at a time you choose instead. To present it, call [`presentMultiSeatInvitationSheet(from:subscriptionGroupID:)`](../../appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-5cmtd.md) in UIKit or [`presentMultiSeatInvitationSheet(from:subscriptionGroupID:)`](../../appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-ni0z.md) in AppKit, or use the [`multiSeatInvitationSheet(isPresented:subscriptionGroupID:onCompletion:)`](../../../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md) view modifier in SwiftUI. Subscriptions that use developer-hosted invitations don’t show the sheet.

For more information, see [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md).

To control the sheet after a purchase in a StoreKit view, use the [`multiSeatInvitationBehavior(_:)`](../../../SwiftUI/view/multiseatinvitationbehavior%28_%29.md) view modifier instead.

## Parameters

- `isSuppressed`: A Boolean value that indicates whether to turn off the invitation sheet. The default is `false`.

## See Also

### Purchasing multiseat subscriptions
- [static func seats(Int) -> Product.PurchaseOption](./seats%28_%29.md)
  Sets the total number of seats for a multiseat subscription purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/multiseatinvitationsheetsuppressed(_:))*
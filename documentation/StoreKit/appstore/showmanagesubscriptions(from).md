# showManageSubscriptions(from:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the App Store sheet for managing subscriptions.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func showManageSubscriptions(from window: NSWindow) async throws
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)

## Discussion

> **Throws**: [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the window isn’t visible, or another error if the system can’t present the sheet.

## Discussion

Use this method to display the manage subscriptions sheet within your Mac app. The sheet is the one that customers use to view and manage their subscriptions, including multiseat subscriptions, where the group purchaser can also change the number of seats. The method returns after the customer dismisses the sheet; dismissing the sheet isn’t an error.

If you’re using SwiftUI, call the [`manageSubscriptionsSheet(isPresented:)`](../../SwiftUI/view/managesubscriptionssheet%28ispresented%29.md) view modifier. On iOS and iPadOS, use [`showManageSubscriptions(in:)`](./showmanagesubscriptions%28in%29.md).

## Parameters

- `window`: The window that the system presents the sheet on. The window needs to be visible.

## See Also

### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene) async throws](./showmanagesubscriptions%28in%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28in,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
- [static func showManageSubscriptions(from: NSWindow, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28from,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(from:))*
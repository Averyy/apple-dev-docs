# showManageSubscriptions(from:subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the App Store sheet for managing subscriptions for a subscription group.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
static func showManageSubscriptions(from window: NSWindow, subscriptionGroupID: String) async throws
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

> **Throws**: [`StoreKitError.invalidPresentationContext`](../storekiterror/invalidpresentationcontext.md) if the window isn’t visible, or another error if the system can’t present the sheet.

## Discussion

Use this method to display the manage subscriptions sheet for the subscriptions in one subscription group, including multiseat subscriptions. The method returns after the customer dismisses the sheet; dismissing the sheet isn’t an error.

If you’re using SwiftUI, call the [`manageSubscriptionsSheet(isPresented:subscriptionGroupID:)`](../../SwiftUI/view/managesubscriptionssheet%28ispresented,subscriptiongroupid%29.md) view modifier. On iOS and iPadOS, use [`showManageSubscriptions(in:subscriptionGroupID:)`](./showmanagesubscriptions%28in,subscriptiongroupid%29.md).

## Parameters

- `window`: The window that the system presents the sheet on. The window needs to be visible.
- `subscriptionGroupID`: The subscription group identifier that the subscription belongs to.

## See Also

### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene) async throws](./showmanagesubscriptions%28in%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28in,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
- [static func showManageSubscriptions(from: NSWindow) async throws](./showmanagesubscriptions%28from%29.md)
  Presents the App Store sheet for managing subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(from:subscriptiongroupid:))*
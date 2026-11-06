# showManageSubscriptions(in:subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the App Store sheet for managing subscriptions for a subscription group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func showManageSubscriptions(in scene: UIWindowScene, subscriptionGroupID: String) async throws
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)
- [Choosing a StoreKit API for Apple In-App Purchases](../choosing-a-storekit-api-for-in-app-purchases.md)
- [Supporting monthly subscriptions with a 12-month commitment](../supporting-monthly-subscriptions-with-a-12-month-commitment.md)

## Discussion

The sheet includes multiseat subscriptions in the subscription group. In macOS 27.3 and later, AppKit apps use [`showManageSubscriptions(from:subscriptionGroupID:)`](./showmanagesubscriptions%28from,subscriptiongroupid%29.md).

## Parameters

- `scene`: The [`UIWindowScene`](../../UIKit/uiwindowscene.md) that the system displays the sheet on.
- `subscriptionGroupID`: The subscription group identifier that the subscription belongs to.

## See Also

### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene) async throws](./showmanagesubscriptions%28in%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(from: NSWindow) async throws](./showmanagesubscriptions%28from%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(from: NSWindow, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28from,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:subscriptiongroupid:))*
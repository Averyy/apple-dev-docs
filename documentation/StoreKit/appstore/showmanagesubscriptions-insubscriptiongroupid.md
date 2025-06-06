# showManageSubscriptions(in:subscriptionGroupID:)

**Framework**: StoreKit  
**Kind**: method

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

- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md)

## Parameters

- `scene`: The   that the system displays the sheet on.
- `subscriptionGroupID`: The subscription group identifier that the subscription belongs to.

## See Also

- [static func showManageSubscriptions(in: UIWindowScene) async throws](appstore/showmanagesubscriptions(in:).md)
  Presents the App Store sheet for managing subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:subscriptiongroupid:))*
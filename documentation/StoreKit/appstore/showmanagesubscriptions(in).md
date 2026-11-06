# showManageSubscriptions(in:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents the App Store sheet for managing subscriptions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func showManageSubscriptions(in scene: UIWindowScene) async throws
```

## Mentions

- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)
- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Supporting monthly subscriptions with a 12-month commitment](../supporting-monthly-subscriptions-with-a-12-month-commitment.md)
- [Testing at all stages of development with Xcode and the sandbox](../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
- [Testing failing subscription renewals and Apple In-App Purchases](../testing-failing-subscription-renewals-and-in-app-purchases.md)
- [Testing win-back offers in Xcode](../testing-win-back-offers-in-xcode.md)

## Discussion

Use this function to display the manage subscriptions sheet within your app. Consider adding a manage subscriptions option to your app. For design guidance on supporting this functionality, see [Human Interface Guidelines > Apple In-App Purchase > Helping People Manage Their Subscriptions](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/auto-renewable-subscriptions/#helping-people-manage-their-subscriptions).

The [`showManageSubscriptions(in:)`](./showmanagesubscriptions%28in%29.md) function presents a manage subscription sheet that’s the same as what customers can view in their account settings in the App Store app or by choosing Settings > Apple Account > Subscriptions on an iOS or iPadOS device. The sheet displays the customer’s currently active subscription for your app and the options to view, upgrade, downgrade, or cancel their subscription. For a multiseat subscription, the group purchaser can also change the number of seats and, with Apple-hosted invitations, manage the group’s members.

If you’re using SwiftUI, call the [`manageSubscriptionsSheet(isPresented:)`](../../SwiftUI/view/managesubscriptionssheet%28ispresented%29.md)view modifier.

Mac apps built with Mac Catalyst can use this method in Mac Catalyst 27.3 and later, and AppKit apps use [`showManageSubscriptions(from:)`](./showmanagesubscriptions%28from%29.md) in macOS 27.3 and later. Earlier versions of macOS don’t support the sheet, so avoid showing the user interface for this feature there:

- In Mac apps built with Mac Catalyst, check the version at runtime with `if #available(macCatalyst 27.3, *)`. For more information on Mac Catalyst, see [Creating a Mac version of your iPad app](../../UIKit/creating-a-mac-version-of-your-ipad-app.md).
- For iOS apps running on Apple silicon, if [`isiOSAppOnMac`](../../Foundation/processinfo/isiosapponmac.md) is `true,` avoid showing the user interface for this feature.

### Test managing subscriptions

Test the managing subscriptions functionality in the sandbox environment and StoreKit testing in Xcode. For more information about testing, see [Testing at all stages of development with Xcode and the sandbox](../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) and [Setting up StoreKit Testing in Xcode](../../Xcode/setting-up-storekit-testing-in-xcode.md).

## Parameters

- `scene`: The [`UIWindowScene`](../../UIKit/uiwindowscene.md) that the system displays the sheet on.

## See Also

### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28in,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
- [static func showManageSubscriptions(from: NSWindow) async throws](./showmanagesubscriptions%28from%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(from: NSWindow, subscriptionGroupID: String) async throws](./showmanagesubscriptions%28from,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:))*
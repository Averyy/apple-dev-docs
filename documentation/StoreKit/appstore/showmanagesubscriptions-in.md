# showManageSubscriptions(in:)

**Framework**: StoreKit  
**Kind**: method

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

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md)
- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Discussion

Use this function to display the manage subscriptions sheet within your app. Consider adding a manage subscriptions option to your app. For design guidance on supporting this functionality, see [`Human Interface Guidelines > In-App Purchase > Helping People Manage Their Subscriptions`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/auto-renewable-subscriptions/#helping-people-manage-their-subscriptions).

The [`showManageSubscriptions(in:)`](appstore/showmanagesubscriptions(in:).md) function presents a manage subscription sheet that’s the same as what customers can view in their account settings in the App Store app or by choosing Settings > Apple ID > Subscriptions on an iOS or iPadOS device. The sheet displays the customer’s currently active subscription for your app and the options to view, upgrade, downgrade, or cancel their subscription.

If you’re using SwiftUI, call the [`manageSubscriptionsSheet(isPresented:)`](https://developer.apple.com/documentation/SwiftUI/View/manageSubscriptionsSheet(isPresented:))view modifier.

Avoid showing the user interface for this feature in Mac apps built with Mac Catalyst and on iOS apps running on Mac computers with Apple silicon because this sheet isn’t supported in macOS.

- In Mac apps built with Mac Catalyst, enclose the code in a compilation conditional block that uses the `targetEnvironment():` platform condition. For more information on Mac Catalyst, see [`Creating a Mac version of your iPad app`](https://developer.apple.com/documentation/UIKit/creating-a-mac-version-of-your-ipad-app).
- For iOS apps running on Apple silicon, if [`isiOSAppOnMac`](https://developer.apple.com/documentation/Foundation/ProcessInfo/isiOSAppOnMac) is `true,` avoid showing the user interface for this feature.

##### Test Managing Subscriptions

Test the managing subscriptions functionality in the sandbox environment and StoreKit testing in Xcode. For more information about testing, see [`Testing at all stages of development with Xcode and the sandbox`](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) and [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

## Parameters

- `scene`: The   that the system displays the sheet on.

## See Also

- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](appstore/showmanagesubscriptions(in:subscriptiongroupid:).md)
  Presents the App Store sheet for managing subscriptions for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:))*
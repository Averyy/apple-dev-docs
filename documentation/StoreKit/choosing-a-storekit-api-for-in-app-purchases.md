# Choosing a StoreKit API for In-App Purchases

**Framework**: StoreKit

Use the latest API to support In-App Purchases in new or existing apps, or the original API to support In-App Purchases in earlier operating systems.

#### Overview

The StoreKit framework provides two APIs to implement a store in your app and offer in-app purchases:

- [`In-App Purchase`](in-app-purchase.md) is a Swift-based API that provides App Store-signed transactions in JSON Web Signature (JWS) format, available starting in iOS 15, macOS 12, tvOS 15, watchOS 8, and visionOS 1.
- [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) provides transaction information using App Store receipts, available starting in iOS 3, macOS 10.7, tvOS 9, watchOS 6.2, and visionOS 1.

> **Note**:  The [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) is deprecated.

If your app has a minimum required operating system that the [`In-App Purchase`](in-app-purchase.md) API supports, use this API to take advantage of Swift concurrency and simplified in-app purchase workflows. Use this API for visionOS apps that use multiple scenes.

Use the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) to maintain and update app versions that have a minimum required operating system of the following versions: macOS 11 or earlier, iOS 14 or earlier, iPadOS 14 or earlier, tvOS 14 or earlier, or watchOS 7 or earlier.

An app can use both the [`In-App Purchase`](in-app-purchase.md) API and the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) if the app runs in iOS 15, macOS 12, tvOS 15, watchOS 8, and visionOS 1 or later. However, only the [`In-App Purchase`](in-app-purchase.md) API supports multi-scene apps for visionOS.

Both APIs provide access to your data in the App Store, such as your configured in-app purchases and transaction information for your customers. In-app purchases that users make using either API are fully available to both APIs.

##### Use the in App Purchase Api to Access New Features

The following features are available only with the Swift-based [`In-App Purchase`](in-app-purchase.md) APIs:

- [`StoreKit views`](storekit-views.md), which provide the UI to build a store in your app
- Refund request sheets, such as [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-65tph.md), that enable customers to request refunds
- Information about a subscription’s renewal status, such as auto-renew preferences. For more information, see [`Product.SubscriptionInfo.Status`](product/subscriptioninfo/status-swift.struct.md).
- Information about available promotional offers and a subscriber’s eligibility for an introductory offer. For more information, see [`Product.SubscriptionInfo`](product/subscriptioninfo.md).
- Deferring or suppressing Billing Issue messages that the system displays. For more information, see [`Message`](message.md).
- Presenting the App Store sheet for managing subscriptions. For more information, see [`showManageSubscriptions(in:subscriptionGroupID:)`](appstore/showmanagesubscriptions(in:subscriptiongroupid:).md).
- Transaction information in JSON Web Signature (JWS) format. For more information, see [`Transaction`](transaction.md).

##### Use the Original Api to Support Certain Features

You might need to use the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md) for the following features, if your app supports them:

- Promoting in-app purchases in apps that run in iOS 11 through 16.3. For more informaton, see [`Promoting In-App Purchases`](promoting-in-app-purchases.md). For information about this feature in iOS 16.4, see [`Supporting promoted In-App Purchases in your app`](supporting-promoted-in-app-purchases-in-your-app.md).
- The Volume Purchase Program (VPP). For more information, see [`Device Management`](https://developer.apple.com/documentation/DeviceManagement).

## See Also

- [Original API for In-App Purchase](original-api-for-in-app-purchase.md)
  Offer additional content and services in your app using the Original In-App Purchase API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/choosing-a-storekit-api-for-in-app-purchases)*
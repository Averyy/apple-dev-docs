# StoreKit

**Framework**: StoreKit  
**Kind**: module

Support In-App Purchases and interactions with the App Store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.2+

#### Overview

Use the StoreKit framework to provide the following features and services for your apps and In-App Purchases:

The StoreKit framework also provides functionality for [`External Purchase`](external-purchase.md), [`External link account`](external-link-account.md), [`PaymentMethodBinding`](paymentmethodbinding.md), and [`StoreDownloaderExtension`](storedownloaderextension.md).

## Topics

### In-App Purchase
- [In-App Purchase](in-app-purchase.md)
  Offer content and services in your app across Apple platforms using a Swift-based interface.
- [Understanding StoreKit workflows](understanding-storekit-workflows.md)
  Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](getting-started-with-in-app-purchases-using-storekit-views.md)
  Set up an in-app store using SwiftUI and StoreKit views.
### App transaction
- [Supporting business model changes by using the app transaction](supporting-business-model-changes-by-using-the-app-transaction.md)
  Access the app transaction to learn when a customer first purchased an app, to determine the app features they’re entitled to.
- [struct AppTransaction](apptransaction.md)
  Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.
### Messages
- [struct Message](message.md)
  An instance for receiving and displaying App Store messages in your app.
- [Message.Reason](message/reason-swift.struct.md)
  Reasons for the App Store messages.
- [struct DisplayMessageAction](displaymessageaction.md)
  An instance that asks StoreKit to display an App Store message, if appropriate.
### Reviews
- [Requesting App Store reviews](requesting-app-store-reviews.md)
  Implement best practices for prompting users to review your app in the App Store.
- [struct RequestReviewAction](requestreviewaction.md)
  An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- [class SKStoreReviewController](skstorereviewcontroller.md)
  An object that controls the process of requesting App Store ratings and reviews from customers.
### Recommendations
- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md)
  Allow users to purchase media in the App Store from within your app.
- [class SKStoreProductViewController](skstoreproductviewcontroller.md)
  A view controller that provides a page where customers can purchase media from the App Store.
- [class SKOverlay](skoverlay.md)
  A class that displays an overlay you can use to recommend another app or an App Clip’s corresponding full app.
### Background assets extension
- [protocol StoreDownloaderExtension](storedownloaderextension.md)
  A protocol to which a downloader extension for Apple-Hosted Background Assets must conform.
### Payment method binding
- [struct PaymentMethodBinding](paymentmethodbinding.md)
  A binding that makes payment methods available in apps for an Apple ID.
### Ad network attribution
- [Ad network attribution](ad-network-attribution.md)
  Validate advertisement-driven app installations.
### External Purchase
- [External Purchase](external-purchase.md)
  Enable qualifying apps to offer external purchases.
### External link account
- [External link account](external-link-account.md)
  Enable qualifying apps to link to an external website for account creation or management.
### Deprecated
- [class SKCloudServiceSetupViewController](skcloudservicesetupviewcontroller.md)
  A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.
- [class SKCloudServiceController](skcloudservicecontroller.md)
  An object that determines the current capabilities of a person’s Music library.

## See Also

- [App Store Server API](../AppStoreServerAPI/AppStoreServerAPI.md)
  Manage your customers’ App Store transactions from your server.
- [StoreKit Test](../StoreKitTest/StoreKitTest.md)
  Create and automate tests in Xcode for your app’s subscription and in-app purchase transactions, and SKAdNetwork implementations.
- [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md)
  Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.
- [App Store Connect API](../AppStoreConnectAPI/AppStoreConnectAPI.md)
  Automate the tasks you perform on the Apple Developer website and in App Store Connect.
- [App Store Receipts](../appstorereceipts/appstorereceipts.md)
  Validate app and In-App Purchase receipts with the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit)*
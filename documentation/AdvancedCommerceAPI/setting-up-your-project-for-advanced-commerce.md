# Setting up your project for Advanced Commerce API

**Framework**: Advanced Commerce API

Configure your app in App Store Connect, set up your server, and prepare your SKUs.

#### Overview

This framework enables you to offer a large catalog of one-time purchases, subscriptions, and bundled content while using the App Store commerce system. To request access to the API, see the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page. After your app receives access, complete the setup to start using the API in your app and on your server.

##### Set Up Generic Product Identifiers

The Advanced Commerce API relies on two generic product identifiers that you configure in App Store Connect:

- A consumable In-App Purchase to represent all one-time purchases
- An auto-renewable subscription in a new subscription group to represent all auto-renewable subscriptions

To create the consumable In-App Purchase, follow the instructions in [`Create consumable or non-consumable In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-consumable-or-non-consumable-in-app-purchases/). To create the subscription group and an auto-renewable subscription, follow the instructions in [`Offer auto-renewable subscriptions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions).

> 💡 **Tip**: Use the Reference name “Enabled for Advanced Commerce” when you create the In-App Purchases, to differentiate them from other products you define.

Send the generic product identifiers that you create for Advanced Commerce to Apple using the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

Be sure to set the generic products’ availability for each storefront that you support. For more information, see [`Set availability for In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases) and [`Set availability for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription).

##### Review Tax Codes for Your Skus

Review the tax codes you’ll use for your SKUs from the list in [`Choosing tax codes for your SKUs`](taxcodes.md). If you need to request additional tax codes, send your request using the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

##### Set Up Your Server

Set up your server to do the following:

- Support Transport Layer Security (TLS) protocol 1.2 or later.
- Receive [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) to get up-to-date transaction data. For setup information, see [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications).

##### Create a Deep Link to Manage Subscriptions in Your App

Create a deep link into your app that opens a page for customers to manage their subscriptions. For more information, see [`Setting up a link to manage subscriptions`](setupmanagesubscriptions.md). Send the deep link to Apple using the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

##### Define and Manage Your Skus

Define your SKUs using the best practices for naming and design. For more information, and to learn where the system displays the SKU data you provide, see [`Creating SKUs for your In-App Purchases`](creating-your-purchases.md). For more design guidance, see Human Interface Guidelines > [`In-app purchase`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase).

When you implement the Advanced Commerce API in your app and on your server, you can test in the sandbox environment before sending it to App Review. For more information, see [`Testing In-App Purchases with sandbox`](https://developer.apple.com/documentation/StoreKit/testing-in-app-purchases-with-sandbox).

## See Also

- [Creating SKUs for your In-App Purchases](creating-your-purchases.md)
  Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Setting up a link to manage subscriptions](setupmanagesubscriptions.md)
  Create a deep link to a subscription-management page for your app.
- [Advanced Commerce API changelog](changelog.md)
  Learn about new features and updates in the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-your-project-for-advanced-commerce)*
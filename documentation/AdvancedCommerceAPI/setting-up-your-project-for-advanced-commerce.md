# Setting up your project for Advanced Commerce API

**Framework**: Advanced Commerce API  
**Role**: Article

Configure your app in App Store Connect, set up your server, and prepare your SKUs.

#### Overview

This framework enables you to offer a large catalog of one-time purchases, subscriptions, and bundled content while using the App Store commerce system. To request access to the API, see the Advanced Commerce API Access form on the [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page. After your app receives access, complete the setup to start using the API in your app and on your server.

##### Create generic product identifiers

The Advanced Commerce API relies on up to four generic product identifiers that you create in App Store Connect. See [Setting up generic product identifiers](./setting-up-generic-product-identifiers.md) to determine which generic product IDs you need, and how to create them. Send the generic product identifiers to Apple using the Advanced Commerce API Access form on the [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

##### Set up your server

Set up your server to do the following:

- Support Transport Layer Security (TLS) protocol 1.2 or later.
- Receive [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) to get up-to-date transaction data. For setup information, see [Enabling App Store Server Notifications](../AppStoreServerNotifications/enabling-app-store-server-notifications.md).

##### Create a deep link to manage subscriptions in your app

Create a deep link into your app that opens a page for customers to manage their subscriptions. For more information, see [Setting up a link to manage subscriptions](./setupmanagesubscriptions.md). Send the deep link to Apple using the Advanced Commerce API Access form on the [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

##### Review tax codes for your SKUs

Review the tax codes you use for your SKUs from the list in [Choosing tax codes for your SKUs](./taxcodes.md). If you need to request additional tax codes, send your request using the Advanced Commerce API Access form on the [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

##### Define and manage your SKUs

Define your SKUs using the best practices for naming and design. For more information, and to learn where the system displays the SKU data you provide, see [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md). For more design guidance, see Human Interface Guidelines > [Apple In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase). To define SKUs for the Mini Apps Partner Program, see [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md).

##### Test your app

When you implement the Advanced Commerce API in your app and on your server, you can test in the sandbox environment before sending it to App Review. For more information, see [Testing Apple In-App Purchases with sandbox](../StoreKit/testing-in-app-purchases-with-sandbox.md).

##### Set up an image for the payment sheet to display

When customers make a purchase, the payment sheet displays your app icon by default. You can optionally provide an image to use instead, in App Store Connect. To set it up, see the [Add or remove an Image ](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information) topic. Set up one image for the generic product ID that represents your subscriptions, and one for the generic product ID that represents your one-time purchases. For more information on the payment sheet and SKU information that the system displays to customers, see [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md).

## See Also

### Essentials
- [Setting up a link to manage subscriptions](./setupmanagesubscriptions.md)
  Create a deep link to a subscription-management page for your app.
- [Advanced Commerce API changelog](./changelog.md)
  Learn about new features and updates in the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-your-project-for-advanced-commerce)*
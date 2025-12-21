# Setting up generic product identifiers

**Framework**: Advanced Commerce API

Configure the generic product IDs in App Store Connect that the Advanced Commerce API requires.

#### Overview

A generic product ID is an identifier you set up in App Store Connect and use when you call Advanced Commerce APIs.  The generic product IDs tell the API whether your SKU is a one-time purchase or a subscription, and whether it’s a SKU for the Mini Apps Partner Program.

You may need to create up to four generic product IDs, based on the product types your app offers:

- One-time purchases
- Subscriptions
- One-time purchases for the Mini Apps Partner Program
- Subscriptions for the Mini Apps Partner Program

Generic product IDs aren’t the same as the SKUs for products you offer in your app. Generic product IDs only contain placeholder information for prices, localizations, and subscription periods and don’t contain tax information. You provide price, localization, and tax information for each SKU when you call the Advanced Commerce APIs. For more information about SKUs, see [`Creating SKUs for your In-App Purchases`](creating-your-purchases.md).

> ❗ **Important**: Send the generic product IDs you create to Apple, using the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

You need one of these roles: Account Holder, Admin, App Manager, Developer, or Marketing in App Store Connect to add and edit product IDs. For more information, see [`Role permissions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/role-permissions).

##### Create a Generic Product Id for One Time Purchases

To offer one-time purchases using Advanced Commerce API, create a generic product ID in App Store Connect, as follows:

1. Sign in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) and select your app.
2. In the sidebar under Monetization, select In-App Purchases and click the add button (+). The Create an In-App Purchase dialog appears.
3. Create the in-app purchase by entering the following: - : Consumable
- : Enabled for Advanced Commerce
- : {your app bundle identifier}.aca.generic.consumable. Replace {your app bundle identifier} with your app’s bundle ID.
4. Click Create to open the details page.

On the details page, configure the following settings:

1. : Select the App Store countries or regions that your app supports. For more information, see [`Set availability for In-App Purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases).
2. : Choose your base country or region and select the lowest available price.
3. : - : English (U.S.)
- : Generic Consumable Product
- : Use the same text as the display name.

##### Create a Generic Product Id for One Time Purchases for the Mini Apps Partner Program

To offer one-time purchases within the Mini Apps Partner Program, create a generic product ID following the instructions for one-time purchases as described above, and enter the following values in the respective topics within the Create an In-App Purchase dialog:

- : Enabled for Mini Apps Partner Program
- : {your app bundle identifier}.aca.mini.consumable

On the details page, enter these values:

- : Mini App Consumable Product
- : Mini App Consumable Product

##### Create a Generic Product Id for Subscriptions

To offer subscriptions using Advanced Commerce API, you first need to create a dedicated subscription group, and then create the generic product ID for a subscription.

To create a dedicated subscription group:

1. Sign in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) and select your app.
2. In the sidebar under Monetization, click Subscriptions and click the add button (+).
3. For , enter Group for Advanced Commerce and click create.

Next, create the generic product ID for subscriptions:

1. Select the subscription group you created.
2. Under Subscriptions, click Create.
3. Configure the subscription as follows: - : Enabled for Advanced Commerce
- : {your app bundle identifier}.aca.generic.subscription
4. Click Create to open the details page.

On the details page, configure the following settings:

- : 1 month
- : Don’t enable.
- : Select the App Store countries or regions your app supports. For more information, see [`Set availability for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription).
- : Choose your base country or region and select the lowest available price.
- : - : English (U.S.)
- : For Advanced Commerce
- : For Advanced Commerce

##### Create a Generic Product Id for Subscriptions for the Mini Apps Partner Program

To offer subscriptions within the Mini Apps Partner Program, follow the same process to create a dedicated subscription group and subscription as above, but use the following values:

- For the  of the dedicated subscription group, enter Group for Mini Apps Partner Program.
- For the  of the subscription, enter Enabled for Mini Apps Partner Program subscription.
- For the  of the subscription, enter {your app bundle identifier}.aca.mini.generic.subscription.
- For the  and  of the localization, enter For Mini Apps Partner Program.

## See Also

- [Creating SKUs for your In-App Purchases](creating-your-purchases.md)
  Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Creating SKUs for the Mini Apps Partner Program](creating-skus-for-the-mini-app-partner-program.md)
  Define display names and SKUs for one-time charges and subscriptions in the Mini Apps Partner Program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-generic-product-identifiers)*
# Creating SKUs for your In-App Purchases

**Framework**: Advanced Commerce API

Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.

#### Overview

For each purchase you plan to offer, create a product identifier, or SKU, in your system along with corresponding text such as display name and price. The App Store displays this information on the payment sheet when a customer initiates a purchase, which helps them understand the transaction before confirming their purchase. You also use this information in additional communication to the customer, including email receipts and invoices from Apple, as well as in their Apple Account Settings under Subscriptions.

To ensure your purchases display properly and provide a quality experience, follow these guidelines:

- Be clear, concise, and descriptive.
- Use proper capitalization and punctuation, and avoid using all capitals.
- Create localized information for any regions where your app is available.
- Consider how you use special characters (for example, hyphens, periods, and underscores) and diacritics. You can use special characters, but avoid using them excessively or beginning strings with them.
- Don’t use markup language, emoticons, diacritics, or control characters (for example, null, new lines, carriage returns, escape, or other invisible characters) that cause strings to exceed a single line.

Review the Human Interface Guidelines for additional best practices for [`writing`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/writing) and designing your [`in-app purchases`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase). If you offer subscriptions, get additional best practices for [`clearly describing subscriptions`](https://developer.apple.comhttps://developer.apple.com/app-store/subscriptions/#clear-description) in your paywalls and payment sheets.

#### Create One Time Charges

Manage one-time purchases — such as one-time rentals, books, or courses — by using the [`OneTimeChargeCreateRequest`](onetimechargecreaterequest.md) API to provide information to the App Store when the customer initiates a purchase. After a one-time charge is complete, customers receive an email receipt from Apple.

![A screenshot of a bookstore app in iOS with an in-app purchase payment sheet open to buy a book. A callout indicates the location on the sheet for the title of the item the customer is purchasing.](https://docs-assets.developer.apple.com/published/4656718ddf593301b5dca63af7cd96ae/one-time-purchase-example%402x.png)

The following details appear in the App Store payment sheet as well as your email receipt; you set both of these values in the [`OneTimeChargeItem`](onetimechargeitem.md) of the [`OneTimeChargeCreateRequest`](onetimechargecreaterequest.md):

- item.[`displayName`](displayname.md): The name of the item the customer is purchasing.
- item.[`price`](price.md): The price of the item the customer is purchasing.

![A diagram of two iOS screens in portrait orientation. The first screen shows a payment sheet for a generic in-app purchase for an item with a one-time charge, with callouts showing where the item display name and item price appear on the sheet. The second screen shows the email confirmation for the purchase, with callouts showing where the app icon, item display name, and item price appear in the email.](https://docs-assets.developer.apple.com/published/cc6dea6b82a8f0a00538c81e8a7d41fa/one-time-purchase-text-field-mapping%402x.png)

#### Create Subscriptions

Use the [`SubscriptionCreateRequest`](subscriptioncreaterequest.md) API to provide information to the App Store when the customer initiates a purchase for each subscription SKU you offer. After a successful purchase, Apple sends customers an email receipt. Apple also sends subscription invoice emails to customers before the subscription renewal date. Customers can go to their Apple Account Subscription Settings to manage their subscription at any time.

![A screenshot of a streaming app in iOS with an in-app purchase payment sheet open to subscribe to a creator. Callouts indicate the locations on the sheet for the name of the subscription the customer is purchasing, and the description of the subscription tier.](https://docs-assets.developer.apple.com/published/a508dad3b84834d488d815436fa8f07a/subscription-creator-app%402x.png)

The following details appear in the App Store payment sheet, email communications from Apple, and the customer’s Apple Account Subscription Settings; you set the values of these details in [`SubscriptionCreateRequest`](subscriptioncreaterequest.md):

- [`descriptors`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/Descriptors).[`displayName`](displayname.md): The name of the subscription the customer is purchasing.
- [`items`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[`displayName`](displayname.md): The tier of the subscription service the customer is purchasing, which needs to be different from your `descriptors.displayName`. For example, if your app includes creator subscriptions and a creator offers multiple subscription tiers, the `displayName` represents the tier the customer is purchasing.
- [`items`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[`price`](price.md): The price of the item the customer is purchasing.
- [`period`](period.md): The duration of the subscription’s billing cycle.
- [`currency`](currency.md): The currency that your app uses to charge the customer.
- App link: A dedicated link for customers to manage their subscription within your app. This link appears in the customer’s Apple Account Subscription Settings as a “Manage in [Your App Name]” button. For setup information, see [`Setting up a link to manage subscriptions`](setupmanagesubscriptions.md). You must also provide a way for customers to [`resubscribe`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest) to a subscription that has expired or has automatic renewals turned off.

![A diagram of two iOS screens in portrait orientation. The first screen shows a payment sheet for a generic in-app purchase for a subscription, with callouts showing where the app icon, subscription tier, currency, price, name, and billing frequency appear on the sheet. The second screen shows the subscription management page in Apple Account Subscriptions, with a callout indicating the link back to the related app.](https://docs-assets.developer.apple.com/published/159e8e9a58e6555ae0d426690eb9c69f/subscription-creator-app-text-field-mapping%402x.png)

#### Create Bundled Subscriptions

For subscription-specific services that are bundled with additional add-on content or services (all of which auto-renews as a single subscription), create a SKU for each service or content offering. Use the [`SubscriptionCreateRequest`](subscriptioncreaterequest.md) API to provide information to the App Store when the customer initiates a purchase. After a successful purchase, Apple sends customers an email receipt. Apple also sends subscription invoice emails to customers before their subscription renewal date. Customers can go to their Apple Account Subscription Settings to manage their subscription at any time.

![An image with two iOS screenshots side by side. The first shows a media app with an in-app purchase payment sheet open to subscribe to a video streaming service bundle, and the second shows the subscription confirmation receipt in email. Callouts on the first image indicate the locations on the sheet for the items included in the subscription bundle, and the subscription plan name.](https://docs-assets.developer.apple.com/published/c91bf2203a80159384802459c93d6f66/subscription-bundle-destination-video%402x.png)

The following details appear in the App Store payment sheet, email communications from Apple, and customer’s Subscription Settings; you set the values of these details in [`SubscriptionCreateRequest`](subscriptioncreaterequest.md):

- [`descriptors`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/Descriptors).[`displayName`](displayname.md): The name of the subscription SKU a customer is purchasing. This needs to represent your overall subscription as well as be relevant for any combination of SKUs someone might choose to bundle.
- [`items`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[`displayName`](displayname.md): The name of the add-on a customer is purchasing. For example, for a streaming app with multiple channel add-ons, this string might be “Live Sports”.
- [`items`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/SubscriptionCreateItem).[`price`](price.md): The price for each add-on within the bundled subscription purchase. When your app or email displays multiple bundle items, it sorts them from highest to lowest price.
- [`period`](period.md): The duration of the subscription’s billing cycle.
- [`currency`](currency.md): The currency that your app uses to charge the customer.
- App link: A dedicated link for customers to manage their subscription within your app. This link appears in the customer’s Apple Account Subscription Settings as a “Manage in [Your App Name]” button. For setup information, see [`Setting up a link to manage subscriptions`](setupmanagesubscriptions.md). You must also provide a way for customers to [`resubscribe`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest) to a subscription that has expired or has automatic renewals turned off.

![A diagram of two iOS screens in portrait orientation. The first screen shows a payment sheet for a generic in-app purchase for a bundle of subscription items, with callouts showing where the subscription plan name and app icon appear on the sheet, along with the bundle item names, currencies, prices, and billing frequencies. The second screen shows the subscription management page in Apple Account Subscriptions, with callouts indicating the subscription plan name and the link back to the related app.](https://docs-assets.developer.apple.com/published/35d790b8b047e06b9def03cd6ac3de99/subscription-bundle-text-field-mapping%402x.png)

## See Also

- [Setting up your project for Advanced Commerce API](setting-up-your-project-for-advanced-commerce.md)
  Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Setting up a link to manage subscriptions](setupmanagesubscriptions.md)
  Create a deep link to a subscription-management page for your app.
- [Advanced Commerce API changelog](changelog.md)
  Learn about new features and updates in the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/creating-your-purchases)*
# Setting up a link to manage subscriptions

**Framework**: Advanced Commerce API

Create a deep link to a subscription-management page for your app.

#### Overview

Customers use the Settings > Apple Account > Subscriptions page in iOS to manage their subscriptions, including upgrading, downgrading, resubscribing, and canceling. When you offer subscriptions through the Advanced Commerce API, the Subscriptions page displays a “Manage in App” button.

![A diagram of an iOS screen in portrait orientation.  The screen shows the subscription-management page in Apple Account Subscriptions, with a callout indicating the button that uses a deep link back to the related app.](https://docs-assets.developer.apple.com/published/ff08444d776659e7c1efbff76c83e98e/subscription-management-app-link%402x.png)

You implement a subscription-management page in your app, and create a deep link URL to it that you submit to Apple. The Settings > Apple Account  > Subscriptions page then uses your deep link for the “Manage in App” button.

> ❗ **Important**: To submit the subscription-management deep link URL for your eligible Advanced Commerce API app, use the Advanced Commerce API Access form on the [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) page.

Create the deep link by following these guidelines:

- Follow universal link guidelines for the URL. For more information, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).
- Ensure the deep link lands on a page in your app that provides information about the subscription’s state and options for the customer to manage their subscription, for example, to change the plan, or resubscribe.
- Optionally, provide a unique subscription-management deep link URL for each storefront.

## See Also

- [Setting up your project for Advanced Commerce API](setting-up-your-project-for-advanced-commerce.md)
  Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Advanced Commerce API changelog](changelog.md)
  Learn about new features and updates in the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/setupmanagesubscriptions)*
# Testing introductory offers

**Framework**: StoreKit

Test your introductory pricing in a variety of user scenarios.

#### Overview

To test introductory offers, verify that users see the same subscription and introductory offer prices in your app as they do in the App Store. As part of your test, make sure your app presents introductory offers only to users that are eligible for them.

To test introductory offers:

1. Configure test accounts, as described in [`Create a sandbox tester account`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev8b997bee1). Create a variety of accounts that are eligible or ineligible for offers.
2. Initiate in-app purchases from within the app for each test user.
3. Verify that the user experience and pricing information dynamically represent the accurate price of your subscription.

Introductory offers are only offered once, but when testing your app, you can reset the status of the test account to allow you to redeem an introductory offer more than once. To reset offer eligibility for the sandbox account:

1. On the test iOS device, open Settings > Apple Account > Media & Purchases (or iTunes & App Store for iOS 13 and earlier). Under the Sandbox Account section, tap your highlighted Sandbox Apple Account then tap Manage to open the sandbox Subscription Management page.
2. Tap the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.
3. If the test account used an introductory offer, then the system diplays a Reset Eligibility button that lets you reset and redeem another introductory offer.

![A screenshot of the edit subscriptions sheet for an app’s subscriptions. The sheet shows the app’s subscription options and the currently selected subscription. Below the subscription options, the sheet displays a Reset Eligibility button and a Cancel Free Trial button.](https://docs-assets.developer.apple.com/published/718f2e24fd660ccad2dfed18105033b6/media-3866189%402x.png)

## See Also

- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md)
  Offer introductory pricing for auto-renewable subscriptions to eligible users.
- [class SKProductDiscount](skproductdiscount.md)
  The details of an introductory offer or a promotional offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-introductory-offers)*
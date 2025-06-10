# Handling subscription price changes

**Framework**: Advanced Commerce API

Provide necessary customer communications to notify and gather applicable consent before you initiate a price change.

#### Overview

Before you initiate a price increase, you must notify affected subscribers and gather applicable consent. To increase the price of a subscription:

1. Determine whether your price increase requires consent, based on the criteria described in [`Request consent for price increases`](handling-subscription-price-changes#Request-consent-for-price-increases.md).
2. Design your in-app sheet to notify or receive subscriber consent.
3. Communicate with affected subscribers via email, price increase sheet, and push notification, following the timelines specified in the Subscription interval table below.
4. If consent is required, record subscriber consent in your system for reference.
5. Use the [`Change Subscription Price`](change-subscription-price.md) endpoint in the Advanced Commerce API to initiate a price change for the individual subscription item.

Once you notify customers using all required communications and gather applicable consent, you can call the API to change the price. After a successful API call to increase the price, Apple sends a push notification to subscribers notifying them of the increase.

![A screenshot of the top half of the iOS Home Screen. A notification at the top of the screen displays information about a subscription price increase, including its new cost and frequency and the date when the subscription increases.](https://docs-assets.developer.apple.com/published/7fe872eaf43b2eaefbce11e6c9b9f2af/subscription-price-increase-notification%402x.png)

> **Note**: When you decrease the price of a SKU, you don’t need to provide any additional communications.

#### Request Consent for Price Increases

If any of the following apply, you must request consent from the subscriber:

- The subscriber is located in a region that requires consent for any price changes. For more information about these regions, see [`Auto-renewable subscription price increase thresholds`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devf3e625675).
- The price increase is: - More than 50 percent of the current price; and
- The difference in price exceeds 5 United States Dollars (USD) per period for non-annual subscriptions, or 50 USD per year for annual subscriptions. International equivalents for prices not in USD are based on current exchange rates with specific thresholds subject to change based on changes in taxes or foreign exchange rates.
- The subscriber had a price increase for the same subscription within the past 12 months.
- The subscriber is located in South Korea and is converting from a free trial to a paid subscription, or from a discounted offer to a standard subscription price.

When consent is required, you must notify subscribers via email, price increase sheet, and push notification, according to the timelines below. If a subscriber doesn’t take any action, you can continue to request consent no more than once per week for each method. You may not raise the price until you receive the subscriber’s consent.

The following notification timeline applies to all cases, except for subscribers in South Korea who are converting from free trials and discount offers:

| Subscription interval | Email, price increase sheet, and push notification timelines |
| --- | --- |
| For 2-month, 3-month, 6-month, and annual subscriptions | 60 days before the renewal date |
| Monthly subscriptions | 27 days before the renewal date |
| Weekly subscriptions | 7 days before the renewal date |

For subscribers in South Korea who are converting from a free trial to a paid subscription, or from a discounted offer to a standard subscription price, use the following notification timelines:

| Subscription interval | Email, price increase sheet, and push notification timelines for South Korea |
| --- | --- |
| For 2-month, 3-month, 6-month, and annual subscriptions | Within 30 days from the day before the payment or conversion |
| Monthly subscriptions | Within 30 days from the day before the payment or conversion |
| Weekly subscriptions | Within 30 days from the day before the payment or conversion |

> **Note**: For free trial or discounted offer conversions in South Korea, the 30-day window for notifications doesn’t include the conversion or payment date. For example, if a two-month free trial starts on March 1 and the payment or conversion date is May 1, you’re required to obtain the consent from the person between April 1 and April 30, the 30-day window before the payment or conversion date.

#### Notify About Price Increases When Consent Isnt Needed

When consent isn’t needed, you only need to notify subscribers about the new price. When increasing the price of multiple items within a bundle and none of the increases require consent, use a single API request so the customer receives a summary of the price increases, and combine notifications into a single communication per method (a single email, one price increase sheet, and a single push notification).

Use the following communications and timelines to notify subscribers:

| Email | Price increase sheet | Push notification |
| --- | --- | --- |
| All subscription durations: Send 27 days before renewal date. Note that for weekly subscriptions, you call the [`Change Subscription Price`](change-subscription-price.md) endpoint on the fourth consecutive renewal to increase the price. | Display upon first app launch after entering notice period. | Display 7 days before renewal date, if someone hasn’t viewed the price increase sheet in-app. |

> **Note**: Unlike when requesting consent, you can omit sending a push notification if the customer acknowledges the increase on the price increase sheet first. Notifying via email is still required in either case.

#### Design Your Price Increase Communications

To ensure customers understand your price increase, provide the details in a clear and conspicuous manner in your email and in-app notifications. For a smooth customer experience, consider including a deep link in your push notification that directs to the price increase sheet within your app. Review the Human Interface Guidelines for best practices on [`helping people manage their subscriptions`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase#Helping-people-manage-their-subscriptions), as well as [`designing`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/notifications) and [`managing`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/managing-notifications) push notifications. Include these elements in your email and in-app notifications:

- A header that makes it clear the communication is about a subscription price increase
- Old price of the subscription
- New price of the subscription
- Date of the price increase
- An easy way for subscribers to review or cancel their subscription. To do this, use the [`showManageSubscriptions(in:)`](https://developer.apple.com/documentation/StoreKit/AppStore/showManageSubscriptions(in:)) API.
- For price increases that require consent, provide an “Agree to New Price” button.

Design your subscription price increase sheet so it includes the proper information and is integrated with the look and feel of your app.

![An illustration of a subscription price increase notice sheet for an iOS creator streaming app. Callouts indicate the messaging of the price increase, a button for the customer to acknowledge the price change, and a link for the customer to manage their subscription.](https://docs-assets.developer.apple.com/published/3372b1f9080f4db062c1d1727b1f546f/subscription-price-increase-consent-not-needed%402x.png)

For price increases that don’t require consent, include a header on your sheet that makes it clear the subscriber’s price is increasing, along with the required information above. Be sure to also provide an “OK” button so people can acknowledge the price increase notice before resuming other activity within your app.

![An illustration of a subscription price increase confirmation dialog for an iOS creator streaming app. Callouts indicate a button to dismiss the sheet, the new subscription price, and a button for the customer to consent to the new price.](https://docs-assets.developer.apple.com/published/96fb34ef7a8e3685ca54d8ccb1805f3d/subscription-price-increase-consent-needed%402x.png)

If consent is required, include a clear “Agree to New Price” button so customers can provide consent. You also need to provide a way for customers to access their Apple Account Subscription Settings, so they can review or cancel their subscription. You must also include a way for customers to close or dismiss the sheet.

## See Also

- [Specifying prices for Advanced Commerce SKUs](prices.md)
  Provide prices for SKUs with the supported number of decimal places, in milliunits of currency.
- [Choosing tax codes for your SKUs](taxcodes.md)
  Select a tax code for each SKU that represents a product your app offers as an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/handling-subscription-price-changes)*
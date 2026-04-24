# Handling subscription price changes

**Framework**: Advanced Commerce API

Initiate a price change and manage communications with your subscribers through the App Store.

#### Overview

The Advanced Commerce API provides a standard UI to facilitate price increases for subscriptions and manage the subscriber consent process.

> **Note**: The AppStore doesn’t currently support the Advanced Commerce price increase mechanism in India.

#### Implement the Advanced Commerce Subscription Price Change Api

Use the [`Change Subscription Price`](change-subscription-price.md) endpoint in the Advanced Commerce API (ACA) to initiate a price change for an individual subscription item. The UI the framework provides manages all of the necessary interactions and communication with a person using your app, including:

- Consent management for price increases.
- Notifications about price increases when the price increase doesn’t requite explicit consent.
- A standard UI sheet that App Store displays to obtain explicit user consent, if required, or an acknowledgment of the price increase if explicit consent isn’t required. Examples of these sheets and an explanation of the information they display about your app and the subscription are shown below.

![An illustration of a subscription price increase confirmation dialog for an iOS creator streaming app. The image depicts a Cancel Subscription button to dismiss the sheet, the new subscription price, and a button for the subscriber to consent to the new price.](https://docs-assets.developer.apple.com/published/e6558d26f3f80fab8cec8190d07c88a8/subscription-price-increase-consent-needed%402x.png)

![An illustration of a subscription price increase notice sheet for an iOS creator streaming app. The image shows the messaging of the price increase, a button for the subscriber to acknowledge the price change, and a link for the subscriber to manage their subscription.](https://docs-assets.developer.apple.com/published/ed99a482f89be475319d2673237a1d72/subscription-price-increase-consent-not-needed%402x.png)

#### Understand Consent Management and Price Change Communication

The App Store checks if a price increase requires consent, and follows different paths depending on whether a subscriber needs to explicitly consent to a price increase or not.

##### Follow the Consent Needed Path

The App Store requests explicit consent from the subscriber if the price increase meets any of the following criteria:

- The subscriber is located in a region that requires consent for any price changes. For more information about these regions, see [`Auto-renewable subscription price increase thresholds`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devf3e625675).
- The price increase is: - More than 50 percent of the current price; and
- The difference in price exceeds 5 United States Dollars (USD) per period for nonannual subscriptions, or 50 USD per year for annual subscriptions. International equivalents for prices not in USD are based on current exchange rates with specific thresholds subject to change based on changes in taxes or foreign exchange rates.
- The subscriber had a price increase for the same subscription within the past 12 months.
- The subscriber converts from trials or offers in South Korea. In these cases, Apple collects consent via email, in-app sheets, or push notifications. The timing and frequency of these communications may differ from those shown for standard subscription price increases, as noted in [`Consent for subscription offer conversions`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/consent-for-subscription-offer-conversions).

When conditions require consent, the App Store notifies subscribers via email, price increase sheet, and push notification, according to the timelines below. If a subscriber doesn’t take any action, the App Store continues to request consent no more than once per week for each method. You can’t raise the price until you receive the subscriber’s consent.

| Subscription interval | Email, price increase sheet, and push notification timelines |
| --- | --- |
| For 2-month, 3-month, 6-month, and annual subscriptions | 60 days before the renewal date |
| Monthly subscriptions | 27 days before the renewal date |
| Weekly subscriptions | 7 days before the renewal date |

![An illustration that describes the timeline of communications the App Store sends regarding subscription price increases, representing a developer changing the price in middle of month. The subscriber receives communication based on communication timelines.](https://docs-assets.developer.apple.com/published/8e27c4d3dcca379999416ca4eadde283/price-increase-notification-timeline%402x.png)

##### Follow the Consent Not Needed Path

When a price increase doesn’t need the subscriber’s consent, the App Store only notifies subscribers about the new price. When the App Store increases the price of multiple items within a bundle, none of which require consent, it uses a single API request so the subscriber receives a summary of the price increases. The App Store combines notifications into a single communication per method (a single email, one price increase sheet, and a single push notification).

The App Store uses the following communication methods and timelines to notify subscribers:

- **Email**: For all subscription durations, the App Store sends an email 27 days before the renewal date. Note that for weekly subscriptions, the App Store calls the [`Change Subscription Price`](change-subscription-price.md) endpoint on the fourth consecutive renewal to increase the price.
- **Price increase sheet**: The App Store displays a price increase sheet at the first app launch after the subscriber enters the notice period.
- **Push notification**: The App Store displays a push notification seven days before the renewal date if the subscriber hasn’t viewed the price increase sheet in-app.

> **Note**: Unlike when requesting consent, the App Store doesn’t send a push notification if the subscriber acknowledges the price increase on the sheet. Notifying via email is still a requirement in either case.

#### Understand Change Subscription Conditions and Limitations

Several conditions may affect your ability to change or update a subscription, including:

- During the price increase window, the renewal uses the increased price that the developer has specified  using [`Change Subscription Price`](Change-Subscription-Price.md) if you make any of the following changes to the subscription: - Add an item
- Remove an item
- Change an item
- Resubscribe using the [`Subscription Modification API`](https://developer.apple.comhttps://developer.apple.com/documentation/advancedcommerceapi#Subscription-modification-in-the-app)  or the [`Subscription Reactivation API`](https://developer.apple.comcom.apple.documentation/documentation/advancedcommerceapi#Subscription-reactivation-in-the-app)
- If the subscription status is auto-renew = `false` or if the subscription is in a grace period or billing retry state, you can’t call the [`Change Subscription Price`](Change-Subscription-Price.md) endpoint.
- If the `SubscriptionPriceChangeItem` is currently in the offer period, you can’t call [`Change Subscription Price`](Change-Subscription-Price.md).

#### Understand Interactions with Other Aca Operations

Several conditions can affect your ability to update a subscription. There may be specific interactions and rules that apply to price increases, depending on which Advanced Commerce API you need to use.

If you need to reactivate items, call the [`SubscriptionReactivateInAppRequest`](SubscriptionReactivateInAppRequest.md) API. The following conditions apply to reactivations:

- If the App Store communicated the price increase, it reactivates the items you provide through the `items` key in the properties you supply to the [`SubscriptionReactivateInAppRequest`](SubscriptionReactivateInAppRequest.md) request at the higher price. Failing to explicitly reactivate an item doesn’t result in the App Store activating the higher price because the App Store needs to communicate the price increase and receive consent through the normal process.
- If the App Store hasn’t communicated the price increase, it schedules the price increase communications for the next eligible date.

If you need to  modify a subscription, call the  [`SubscriptionModifyInAppRequest`](SubscriptionModifyInAppRequest.md) API. Price increases interact with the ACA in a specific way depending on if the call resets or retains the billing cycle.

If the price increase takes place during a retain billing cycle, the following rules apply:

- If the App Store communicated the price increase: - If the price increase is pending consent, the Payment Sheet shows the higher price, and the user must consent to the price increase via the in-app sheet that appears, or via Manage Subscriptions.
- If the subscriber consented to the  price increase, or the price increase doesn’t require consent,  the Payment Sheet shows the higher price.
- If the  subscriber declined the price increase, the item doesn’t appear in the Payment Sheet.
- If the item’s SKU is changing to a different product SKU (such as from SKU `BASIC` to SKU `PREMIUM`), the change invalidates the price increase because the new SKU represents a different product.
- When the App Store sends an offer with an item subject to a price increase, it’s a *special consideration*; in this case, you send the higher price of the item, and the App Store reschedules the price increase for after the offer period completes, at which point, the item renews at the higher price.

If the price increase takes place during a reset billing cycle, the following rules apply:

- If the App Store hasn’t communicated the  price increase, the price increase is invalidated.
- If the the App Store communicated the price increase, the App Store applies the new price only if the item is sent with the higher price, using the [`SubscriptionModifyChangeItem`](SubscriptionModifyChangeItem.md). - As described above, changing the item to a different product (such as changing from *BASIC* SKU  to a *Premium* SKU) invalidates the price increase, as the item represents a different product.

If you need to change a subscription’s metadata, call the [`Change Subscription Metadata`](Change-Subscription-Metadata.md). Metadata-only changes, such as changing the SKU from SKU A to SKU B, preserve the price increase because it isn’t a change in product, but rather a change to the product SKU.

If you need to call the ACA Migration API to migrate a subscription that a subscriber purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API, the following rules apply:

- If the In-App purchase product has a pending price increase through App Store Connect, the App Store doesn’t allow the migration if it already communicated the price increase to the subscriber.
- The App Store doesn’t allow migrations if the item is currently subject to a price increase, and the App Store already sent price increase communications to the subscriber.
- If there’s an upcoming price increase, the App Store migrates the pending price increase as well.

#### Understand Price Increase Status and Update Values

The following table describes the meaning of price increase status values:

| Price increase info status | Description |
| --- | --- |
| `priceIncreaseInfo.SCHEDULED` | Indicates the App Store scheduled the price increase for the [`SubscriptionPriceChangeItem`](SubscriptionPriceChangeItem.md). |
| `priceIncreaseInfo.PENDING` | Indicates there’s a pending price increase for the `SubscriptionPriceChangeItem` that requires subscriber consent, and the subscriber hasn’t yet consented. If the subscriber doesn’t consent, the `SubscriptionPriceChangeItem` expires at the end of the billing cycle. |
| `priceIncreaseInfo.ACCEPTED` | Indicates that the subscriber consented to a price increase for the [`SubscriptionPriceChangeItem`](SubscriptionPriceChangeItem.md). |

The following table describes the notifications and status values for a subscription price change item that requires consent:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | `priceIncreaseInfo.SCHEDULED` | Indicates that you called the [`Change Subscription Price`](Change-Subscription-Price.md)  endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `PRICE_INCREASE` | `PENDING` | `priceIncreaseInfo.PENDING` | Indicates there’s a pending price increase for the SKU that requires subscriber consent, and the subscriber hasn’t yet consented. If the subscriber doesn’t consent, the SKU expires at the end of the billing cycle. |
| `PRICE_INCREASE` | `ACCEPTED` | `priceIncreaseInfo.ACCEPTED` | Indicates that the subscriber consented to a price increase for the SKU. |
| `EXPIRED` | `PRICE_INCREASE` | - | Indicates that the auto-renewable subscription expired because the subscriber didn’t consent to the price increase, and allowed the subscription to expire. |
| `EXPIRED` | `VOLUNTARY` | - | Indicates that the subscriber voluntarily canceled the auto-renewable subscription. This notification type and subtype aren’t specific to price increases. |
| `DID_RENEW` | - | - | Indicates the SKU renewed. Use the data in the [`JWSRenewalInfo`](JWSRenewalInfo.md) and the [`JWSTransaction`](JWSTransaction.md) to provide service for the SKU. |

The following table describes the notifications and status values for a subscription price change item that doesn’t require consent:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | `priceIncreaseInfo.SCHEDULED` | Indicates that you called the [`Change Subscription Price`](Change-Subscription-Price.md) endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `PRICE_INCREASE` | `ACCEPTED` | `priceIncreaseInfo.ACCEPTED` | Indicates that the App Store informed the subscriber for the subscription price increase for the item, and it’s subject to the price increase. |
| `EXPIRED` | `VOLUNTARY` | - | Indicates that the subscriber voluntarily canceled the auto-renewable subscription. This notification type and subtype isn’t specific to price increases. |
| `DID_RENEW` | - | - | The SKU renewed. Always check  [`JWSRenewalInfo`](JWSRenewalInfo.md) and the [`JWSTransaction`](JWSTransaction.md) information to provide service to the list items. |

The following table describes the notifications and status values for a subscription price change item that decreases a price:

| Notification type | Subtype | Property details | Description |
| --- | --- | --- | --- |
| `PRICE_CHANGE` | - | - | Indicates that you called the [`Change Subscription Price`](Change-Subscription-Price.md) endpoint. This notification only applies to apps that use the Advanced Commerce API. |
| `DID_RENEW` | - | - | Indicates the SKU renewed. Always to check to ensure [`JWSRenewalInfo`](JWSRenewalInfo.md) and the [`JWSTransaction`](JWSTransaction.md) information to provide service to the list items. |

#### Understand Conditional Cancellations and Dependent Skus

To create a contingency for a situation in which a person doesn’t agree to a price increase and the App Store cancels other bundled services (the “dependent SKUs”), you can provide an array of the SKUs through the `dependentSKUs` property. If the price increase requires a person’s consent, and they don’t consent to the price increase (through a cancellation from the Manage Subscriptions view, or by failing to consent before the renewal date), the App Store cancels the dependent SKUs.

> ❗ **Important**: You can’t have chains of dependent SKUs. For example, if SKU *A* has dependent SKU *B*, *B* can’t have its own dependent SKU, *C*. However, *B* can have its own price increase.

#### Test Price Increases in the Sandbox

To test subscription price increases, call the [`Change Subscription Price`](Change-Subscription-Price.md) API in the sandbox to test the API responses. The sandbox environment — and TestFlight — support the full price increase cycle, with the exception of the email and push notifications. The in-app sheet still appears, and price increase management appears on the Manage Subscriptions page.

> **Note**: After you call the [`Change Subscription Price`](Change-Subscription-Price.md) API, the subscription renews on the higher price after one renewal, giving you time to test in the sandbox environment.

You can test granting consent or declining a price increase through the in-app sheet or by navigating to the Manage Subscription page in the sandbox. For more information, see [`Testing disabling auto-renew`](https://developer.apple.com/documentation/StoreKit/testing-disabling-auto-renew).

In the sandbox, the first renewal after calling [`Change Subscription Price`](Change-Subscription-Price.md) uses the existing price to assist in testing states prior to when the App Store communicates the price increase. After the first renewal, the App Store simulates communicating the price increase for the next appropriate renewal.

## See Also

- [Specifying prices for Advanced Commerce SKUs](prices.md)
  Provide prices for SKUs with the supported number of decimal places, in milliunits of currency.
- [Choosing tax codes for your SKUs](taxcodes.md)
  Select a tax code for each SKU that represents a product your app offers as an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/handling-subscription-price-changes)*
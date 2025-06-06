# Change Subscription Price

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Handling subscription price changes](handling-subscription-price-changes.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

Call this endpoint as the final step in changing the price of a subscription or any bundle or item within it. Based on the type of price change, you might need to communicate the change to customers or get their consent. For information about the communication requirements including their timing, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

Only active subscriptions that aren’t in a billing retry state are eligible for price changes. When you call this endpoint, the price change takes effect at the next subscription renewal. Call the endpoint no later than 24 hours before the renewal date to have it take effect at the renewal.

For information about providing prices, see [`Specifying prices for Advanced Commerce SKUs`](prices.md).

##### Inform Customers and Get Consent If Needed

Determine whether you need to communicate a price change to the customer, as follows:

- Decreasing the price doesn’t require any communications with the customer. You can call this endpoint anytime you want to decrease prices.
- Increasing subscription prices requires you to notify the customer in advance. Some price increases also require you to obtain the customer’s consent. To determine whether you need price consent and for information about customer communications and their timing, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

> ❗ **Important**: You need to communicate price increases to your customer, including through email, in-app messaging, and push notifications. To determine whether you need price consent and for information about customer communications and their timing, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

You need to communicate price increases to your customer, including through email, in-app messaging, and push notifications. To determine whether you need price consent and for information about customer communications and their timing, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

##### Increase Price of a Sku

If you’re increasing the price of any SKU associated with a subscription (such as the subscription itself, a bundle, or an individual item), follow these steps:

1. Determine whether the price increase requires customer consent.
2. If the increase doesn’t require customer consent, notify the customer of the price increase in advance, as described in [`Handling subscription price changes`](handling-subscription-price-changes.md). Then, call this endpoint after you notify the customer.
3. If the increase requires customer consent, call this endpoint only if you’ve obtained the customer’s consent.  If you don’t obtain the customer’s consent to increase the price, don’t call this endpoint, and preserve the existing price.

##### Example Request and Response

In the following request:

- The subscription includes multiple items, and only one item has a price increase to USD 12.99.
- The price increase takes effect at the next subscription renewal.
- The decoded signed transaction shows price in the current period, before the increase.
- The decoded signed renewal information shows the increased price, which takes effect at the next renewal period.

## Request Body

The request body that contains the details of the price change.

## See Also

- [object SubscriptionPriceChangeRequest](subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price)*
# Change Subscription Price

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Handling subscription price changes](handling-subscription-price-changes.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Advanced Commerce API changelog](changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

Call this endpoint when you change the price of a subscription or any bundle or item within it. For information about the customer communication, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

Only active subscriptions that aren’t in a billing retry state are eligible for price changes. When you call this endpoint, the price change takes effect at the next subscription renewal. Call the endpoint no later than 24 hours before the renewal date to have it take effect at the renewal.

For information about providing prices, see [`Specifying prices for Advanced Commerce SKUs`](prices.md).

##### Example Request and Response

In the following request:

- The subscription includes multiple items, and only one item has a price increase to USD 12.99.
- The price increase takes effect at the next subscription renewal.
- The decoded signed transaction shows price in the current period, before the increase.
- The decoded signed renewal information shows the increased price, which takes effect at the next renewal period if consented to.
- The item has a dependent SKU, which will be cancelled if the price increase is not agreed to.
- In this example, the price increase has been communicated, so the status is marked as pending.

## Request Body

The request body that contains the details of the price change.

## See Also

- [object SubscriptionPriceChangeRequest](subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price)*
# Unpreserving prices after volume pricing takes effect

**Framework**: App Store Connect API  
**Role**: Article

Schedule a single price to replace in-effect volume pricing, so you can unpreserve earlier subscriber prices in App Store Connect.

## Overview

When you raise a subscription’s price, you can preserve the price that existing subscribers pay by setting `preserveCurrentPrice` to `true`. Each earlier price you preserve stays in effect for the subscribers who already pay it. Unpreserving a price ends that protection for those subscribers. When you set up volume pricing in the API, you can’t configure pricing for that subscription in App Store Connect. Before the price takes effect, you can delete the price to restore that access. After it takes effect, you can’t delete it, so you need another way to remove the tiers.

This article explains why App Store Connect blocks pricing changes and how to remove the tiers by using the API. For more information about creating prices with tiers, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md). For more information about preserved prices and subscriber consent, see [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md).

### Understand what blocks you

App Store Connect blocks pricing changes for a subscription, including unpreserving a price, whether the price with tiers is scheduled or in effect. The API has no operation that unpreserves a price. You can only create a price with [`Create a subscription price change`](./post-v1-subscriptionprices.md) or delete a scheduled one with [`Delete subscription prices`](./delete-v1-subscriptionprices-_id_.md).

This timeline shows how a subscription with volume pricing gets into this state and how to get out of it. In the example, the subscription starts with three preserved or current prices, A, B, and C, and you schedule a price with additional tiers, D, then replace it with a single price, E.

| Day | What happens |
| --- | --- |
| 0 | A ($4.99) and B ($6.99) are preserved. C ($7.99) is the current price. |
| 1 | You schedule D to start on day 3, with a $9.99 single-seat price, additional tiers for more seats, and `preserveCurrentPrice` set to `true`. A, B, and C don’t change. App Store Connect blocks pricing changes for this subscription. |
| 3 | D takes effect: $9.99 for 1–4 seats, $9.49 for 5–19 seats, and $8.99 for 20 or more seats. A, B, and C are all preserved. |
| 4 | You want to unpreserve A, B, or C, but App Store Connect blocks you, and you can’t delete D because it’s in effect. Instead, you schedule E, a single $9.99 price that starts on day 6. |
| 6 | The single price you scheduled on day 4, E, takes effect at $9.99 for every number of seats. A, B, and C are still preserved. |

### Delete the price before it takes effect

Until a price takes effect, you can delete it to return to the state you had before you created it. On day 1 or day 2 of the example, delete D by using `DELETE /v1/subscriptionPrices/{id}` ([`Delete subscription prices`](./delete-v1-subscriptionprices-_id_.md)), where `{id}` is the ID of price D. Get it from the response to `GET /v1/subscriptions/{id}/prices` ([`List all prices for a subscription`](./get-v1-subscriptions-_id_-prices.md)). For example:

```other
DELETE /v1/subscriptionPrices/eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiRCJ9
```

A successful request returns `204` with no content. The subscription returns to its day 0 state. To change scheduled tiers, delete the price and create a new one that has all the tiers you want.

### Schedule a single price after it takes effect

When D is in effect, you can’t delete it. To remove its tiers, schedule a new price without `additionalPriceTiers` by using `POST /v1/subscriptionPrices` ([`Create a subscription price change`](./post-v1-subscriptionprices.md)). Set `startDate` to a date at least two days after the current date, because prices take time to roll out around the world. Use the price point you want for every number of seats, and set `preserveCurrentPrice` to `false`. For more information about finding price point IDs, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md). For example:

```other
{
  "data": {
    "type": "subscriptionPrices",
    "attributes": {
      "startDate": "2027-03-06",
      "preserveCurrentPrice": false
    },
    "relationships": {
      "subscription": {
        "data": { "type": "subscriptions", "id": "6447497832" }
      },
      "territory": {
        "data": { "type": "territories", "id": "USA" }
      },
      "subscriptionPricePoint": {
        "data": {
          "type": "subscriptionPricePoints",
          "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ"
        }
      }
    }
  }
}
```

Because the request doesn’t include `additionalPriceTiers`, the new price has a single tier. Setting `preserveCurrentPrice` to `false` means the new price replaces D for every subscriber who pays it. Repeat the request for each territory where you set tiers.

> ❗ **Important**:  Subscribers who pay a lower per-seat tier price get a price increase when E takes effect. In the example, subscribers who pay $9.49 or $8.99 per seat move to $9.99. Before you schedule the price, use [`Create a subscription price change preview`](./post-v1-subscriptionpricechangepreviews.md) to see how the change affects existing subscribers in each territory. For more information, see [Subscription price change previews](./subscription-price-change-previews.md).

### Unpreserve prices in App Store Connect

After E takes effect, App Store Connect no longer blocks pricing changes for the subscription. In the example, you can unpreserve A, B, and C on day 6 or later. You unpreserve prices by territory, so repeat the change in each territory where you scheduled the single price. Unpreserving takes effect immediately and you can’t undo it. For more information about managing prices in App Store Connect, see [Manage pricing for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions/).

To confirm which price is in effect and whether it’s preserved before you open App Store Connect, use `GET /v1/subscriptions/{id}/prices` ([`List all prices for a subscription`](./get-v1-subscriptions-_id_-prices.md)). Filter by territory, and include `additionalPriceTiers` to see whether a price has tiers. For example:

```other
GET /v1/subscriptions/6447497832/prices?filter[territory]=USA&include=additionalPriceTiers
```

Each price in the response has a `startDate` and a `preserved` attribute that reflects whether the price is preserved. A price with an empty `additionalPriceTiers` relationship has no volume pricing tiers.

To read the minimum quantity and price point for each tier of a price, use `GET /v1/subscriptionPrices/{id}/additionalPriceTiers` ([`List additional price tiers for a subscription price`](./get-v1-subscriptionprices-_id_-additionalpricetiers.md)), where `{id}` is the price’s ID from the previous response. Add `include=subscriptionPricePoint` to read each tier’s price point. For example:

```other
GET /v1/subscriptionPrices/{priceId}/additionalPriceTiers?include=subscriptionPricePoint
```

## See Also

### Managing Auto-Renewable Subscriptions
- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](./working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Querying adjusted subscription price equalizations](./querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)
  Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
  Offer lower per-seat prices to groups and organizations that buy an auto-renewable subscription in larger quantities.
- [Subscription Versions](./subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](./subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](./subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](./subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription price tiers](./subscription-price-tiers.md)
  Read the volume pricing tiers that set a per-seat price from a minimum number of seats.
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/removing-price-preservation-after-volume-pricing-takes-effect)*
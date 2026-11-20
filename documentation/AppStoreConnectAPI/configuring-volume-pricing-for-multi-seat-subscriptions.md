# Configuring volume pricing for multiseat subscriptions

**Framework**: App Store Connect API  
**Role**: Article

Offer lower per-seat prices to groups and organizations that buy an auto-renewable subscription in larger quantities.

## Overview

Use the App Store Connect API to add volume pricing tiers to a subscription’s price in each territory. For an overview of volume pricing, how multiseat purchasing affects it, and the limits of managing prices in App Store Connect after you add tiers, see [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md). To learn more about configuring prices for your subscriptions, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md).

### Review App Store Connect API usage

If you’re new to the App Store Connect API, start with [Creating API Keys for App Store Connect API](./creating-api-keys-for-app-store-connect-api.md), [Generating Tokens for API Requests](./generating-tokens-for-api-requests.md), and [Identifying Rate Limits](./identifying-rate-limits.md).

Volume pricing uses the same permissions as subscription prices. To configure it, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

People with the `MARKETING` role can view volume pricing but can’t change it. For the full list of App Store Connect user roles, see [`UserRole`](./userrole.md) and [Program Roles](https://developer.apple.com/support/roles).

### Understand how volume tiers work

A price has up to five tiers, each defined by the lowest seat count it applies to. The first tier always starts at one seat and uses the subscription price’s own `subscriptionPricePoint`. Each additional tier is a `subscriptionPriceTiers` resource with a `minQuantity` and its own `subscriptionPricePoint`. A tier covers every seat from its `minQuantity` up to, but not including, the next tier’s `minQuantity`. The last tier has no upper limit.

Each seat costs the per-seat price of the tier it falls into, so a larger purchase doesn’t lower the price of the seats in earlier tiers. For example, given the following tiers:

| Tier | Seats | Price per seat (USD) | Defined by |
| --- | --- | --- | --- |
| 1 | 1 | 9.99 | The price’s `subscriptionPricePoint` |
| 2 | 2–9 | 8.99 | Tier with `minQuantity` of `2` |
| 3 | 10–49 | 7.99 | Tier with `minQuantity` of `10` |
| 4 | 50 or more | 6.99 | Tier with `minQuantity` of `50` |

A customer who buys 12 seats pays 9.99 USD for seat 1, 8.99 USD each for seats 2 through 9, and 7.99 USD each for seats 10 through 12. The total for 12 seats is 105.88 USD.

A valid set of tiers follows these rules:

- A price has at most five tiers: the single-seat price and up to four additional tiers.
- The first additional tier has a `minQuantity` of `2` or more.
- Each tier has a distinct `minQuantity`. List the tiers in ascending order of `minQuantity`, because the equalization endpoint rejects tiers that are out of order.
- Each tier has a strictly lower per-seat price than the tier before it. The server rejects a tier that costs the same as, or more than, the previous tier.
- The price has a `planType` of `UPFRONT`. Customers can’t buy a `MONTHLY` plan in quantity, so a `MONTHLY` price always has a single tier.

When you equalize tiers, every territory gets your base territory’s seat ranges with equalized prices. You can give a territory different prices, a different number of tiers, or different seat ranges, as long as its tiers follow these rules.

In the App Store, the total number of seats a customer holds on a subscription can’t exceed 100, and the App Store blocks a purchase or seat addition that would go over that limit. Purchases through [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/) and [Apple School Manager](https://support.apple.com/guide/apple-school-manager/) don’t have this limit. You can create tiers that start above 100 seats, but only Apple Business Manager and Apple School Manager customers can reach them.

### Find price points for each tier

Look up the price points for your base territory by using `GET /v1/subscriptions/{id}/pricePoints` ([`List all price points for a subscription`](./get-v1-subscriptions-_id_-pricepoints.md)), filtered by territory:

```other
GET /v1/subscriptions/6447497832/pricePoints?filter[territory]=USA&limit=200
```

Choose one price point for each tier, starting with the single-seat price and working down to the lowest-priced tier. Note the `id` of each price point you choose.

### Equalize tiers across territories

Rather than equalizing each tier’s price point separately, you can convert all of your tiers from your base territory into every other territory in one request. Use `POST /v1/subscriptionPriceTierEqualizations` ([`Create a subscription price tier equalization`](./post-v1-subscriptionpricetierequalizations.md)). Provide the base territory’s single-seat price point as the `basePricePoint` relationship and the remaining tiers in `additionalPriceTiers`. The base territory is the territory of `basePricePoint`. Add `include=priceTierPricePoints` to get the `customerPrice` and `proceeds` for the returned price points in the same response. The response includes only the first 10 price points by default, so add `limit[priceTierPricePoints]` to return more.

This request doesn’t save anything. It only calculates the equalized tiers.

```other
POST /v1/subscriptionPriceTierEqualizations?include=priceTierPricePoints
```

For example:

```other
{
  "data": {
    "type": "subscriptionPriceTierEqualizations",
    "attributes": {
      "additionalPriceTiers": [
        { "minQuantity": 2,  "subscriptionPricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMTUifQ" },
        { "minQuantity": 10, "subscriptionPricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMDMifQ" },
        { "minQuantity": 50, "subscriptionPricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAwOTEifQ" }
      ]
    },
    "relationships": {
      "subscription": {
        "data": { "type": "subscriptions", "id": "6447497832" }
      },
      "basePricePoint": {
        "data": {
          "type": "subscriptionPricePoints",
          "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ"
        }
      }
    }
  }
}
```

The response contains an `equalizedPrices` array with one entry for each territory other than the base territory. Each entry has a `territoryId`, the equalized single-seat `basePricePointId`, and `additionalPriceTiers` that keep the same `minQuantity` values. Here’s the example response, truncated for clarity:

```other
{
  "data": {
    "type": "subscriptionPriceTierEqualizations",
    "attributes": {
      "equalizedPrices": [
        {
          "territoryId": "CAN",
          "basePricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ",
          "additionalPriceTiers": [
            { "minQuantity": 2,  "subscriptionPricePointId": "..." },
            { "minQuantity": 10, "subscriptionPricePointId": "..." },
            { "minQuantity": 50, "subscriptionPricePointId": "..." }
          ]
        }
      ]
    }
  },
  "included": [
    {
      "type": "subscriptionPricePoints",
      "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ",
      "attributes": { "customerPrice": "12.99", "proceeds": "9.09" }
    }
  ]
}
```

### Preview the effect of a price change

If a subscription already has a price in a territory, new tiers can raise some seat ranges and lower others. Before you schedule the change, preview it with `POST /v1/subscriptionPriceChangePreviews` ([`Create a subscription price change preview`](./post-v1-subscriptionpricechangepreviews.md)), as [Preview the effect of a price change](./configuring-subscription-prices-across-territories.md#Preview-the-effect-of-a-price-change) describes. To preview tiers, list them in each entry’s `additionalPriceTiers`, and send every territory in one `proposedChanges` array. Like equalization, this request doesn’t save anything.

For example:

```other
{
  "data": {
    "type": "subscriptionPriceChangePreviews",
    "attributes": {
      "proposedChanges": [
        {
          "territoryId": "CAN",
          "startDate": "2027-03-01",
          "basePricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ",
          "additionalPriceTiers": [
            { "minQuantity": 2,  "subscriptionPricePointId": "..." },
            { "minQuantity": 10, "subscriptionPricePointId": "..." },
            { "minQuantity": 50, "subscriptionPricePointId": "..." }
          ]
        }
      ]
    },
    "relationships": {
      "subscription": {
        "data": { "type": "subscriptions", "id": "6447497832" }
      }
    }
  }
}
```

For a price with tiers, the preview compares the current and proposed prices at every seat count. The response’s `changeType` value for each territory describes the result. `INCREASE_PRESERVABLE` means the proposed price is higher than or equal to the current price at every seat, and higher at one or more seats. `MIXED_NOT_PRESERVABLE` means the proposed price is higher for some seats and lower for others, or the seat ranges change so that the prices can’t be compared in one direction. To learn more about the other values, how `preserveCurrentPrice` works, and how price increases, notice, and consent affect existing subscribers, see [Preview the effect of a price change](./configuring-subscription-prices-across-territories.md#Preview-the-effect-of-a-price-change) and [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md).

### Schedule a price with volume tiers

Create the price and its tiers together in a single `POST /v1/subscriptionPrices` ([`Create a subscription price change`](./post-v1-subscriptionprices.md)) request. As with any subscription price, set the `subscription` and single-seat `subscriptionPricePoint` relationships. List each additional tier in the `additionalPriceTiers` relationship by using a local ID, and define each tier in the `included` array. Each included `subscriptionPriceTiers` resource provides a `minQuantity` and a `subscriptionPricePoint` relationship.

You don’t need to create the single-seat price first. The request sets the single-seat price and its tiers together, as the following example shows. Make the subscription available in the territory first. Otherwise, the request fails with `UNSUPPORTED_TERRITORY`. For more information about single-seat prices and availability, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md).

For example, this payload schedules four tiers in the United States:

```other
{
  "data": {
    "type": "subscriptionPrices",
    "attributes": {
      "startDate": "2027-03-01",
      "planType": "UPFRONT",
      "preserveCurrentPrice": false
    },
    "relationships": {
      "subscription": {
        "data": { "type": "subscriptions", "id": "6447497832" }
      },
      "subscriptionPricePoint": {
        "data": {
          "type": "subscriptionPricePoints",
          "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ"
        }
      },
      "additionalPriceTiers": {
        "data": [
          { "type": "subscriptionPriceTiers", "id": "${tier-2}" },
          { "type": "subscriptionPriceTiers", "id": "${tier-10}" },
          { "type": "subscriptionPriceTiers", "id": "${tier-50}" }
        ]
      }
    }
  },
  "included": [
    {
      "type": "subscriptionPriceTiers",
      "id": "${tier-2}",
      "attributes": { "minQuantity": 2 },
      "relationships": {
        "subscriptionPricePoint": {
          "data": { "type": "subscriptionPricePoints", "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMTUifQ" }
        }
      }
    },
    {
      "type": "subscriptionPriceTiers",
      "id": "${tier-10}",
      "attributes": { "minQuantity": 10 },
      "relationships": {
        "subscriptionPricePoint": {
          "data": { "type": "subscriptionPricePoints", "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMDMifQ" }
        }
      }
    },
    {
      "type": "subscriptionPriceTiers",
      "id": "${tier-50}",
      "attributes": { "minQuantity": 50 },
      "relationships": {
        "subscriptionPricePoint": {
          "data": { "type": "subscriptionPricePoints", "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAwOTEifQ" }
        }
      }
    }
  ]
}
```

Repeat this request for each territory, using the equalized price points from the equalization response.

To schedule prices for several territories in one request, use `PATCH /v1/subscriptions/{id}` ([`Modify an auto-renewable subscription`](./patch-v1-subscriptions-_id_.md)). Include each price in the subscription’s `prices` relationship, and include its tiers in the same `included` array.

To add tiers without changing what existing single-seat subscribers pay, use the subscription’s current single-seat price point as the price’s `subscriptionPricePoint`.

The API saves a price and its tiers as a single unit, and you can’t edit a subscription price or its tiers after you create them. To change scheduled tiers, delete the scheduled price by using `DELETE /v1/subscriptionPrices/{id}` ([`Delete subscription prices`](./delete-v1-subscriptionprices-_id_.md)), then create a new price that contains all of the tiers you want. A price you create without `additionalPriceTiers` has a single tier.

A territory can have only one scheduled price at a time, so a second request fails with a `409` error until you delete the first. You can’t delete a price that’s already in effect. To remove the tiers from one, schedule a new price without `additionalPriceTiers`. A price with tiers also blocks you from stopping preservation of earlier prices in App Store Connect. For more information, see [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md).

Invalid tiers fail with a `409` error. These error codes identify the cause:

| Code | Cause |
| --- | --- |
| `PRICE_TIERS_NOT_DECREASING` | A tier costs the same as, or more than, the tier before it. |
| `PRICE_TIERS_NOT_ASCENDING` | A `minQuantity` is duplicated or out of order. |
| `INVALID_PRICE_TIER_QUANTITY` | A `minQuantity` is less than `2`. |
| `TOO_MANY_PRICE_TIERS` | The price has more than four additional tiers. |
| `MULTIPLE_PRICE_TIERS_NOT_SUPPORTED` | The price has a `planType` of `MONTHLY` and additional tiers. |

### Verify your tiers

The `201` response to a create request returns the price with a link to its tiers, not the tiers themselves. To read back a single price’s tiers along with each tier’s price point, use `GET /v1/subscriptionPrices/{id}/additionalPriceTiers` ([`List additional price tiers for a subscription price`](./get-v1-subscriptionprices-_id_-additionalpricetiers.md)):

```other
GET /v1/subscriptionPrices/{priceId}/additionalPriceTiers?include=subscriptionPricePoint
```

To read the tiers of every price on a subscription in one request, use `GET /v1/subscriptionPriceTiers` ([`List subscription price tiers`](./get-v1-subscriptionpricetiers.md)). The `filter[subscription]` parameter is required. Tiers don’t identify their territory, so add `filter[territory]` to know which territory the results belong to:

```other
GET /v1/subscriptionPriceTiers?filter[subscription]=6447497832&filter[territory]=USA&include=subscriptionPricePoint
```

Here’s the example response, truncated for clarity:

```other
{
  "data": [
    {
      "type": "subscriptionPriceTiers",
      "id": "...",
      "attributes": { "minQuantity": 2 },
      "relationships": {
        "subscriptionPricePoint": {
          "data": { "type": "subscriptionPricePoints", "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMTUifQ" }
        }
      }
    }
  ]
}
```

You can also add `include=additionalPriceTiers` when you list prices with `GET /v1/subscriptions/{id}/prices` ([`List all prices for a subscription`](./get-v1-subscriptions-_id_-prices.md)). This include returns each tier’s `minQuantity` but not its price point, so use one of the tier endpoints in this section to get the price for each tier. A price without volume tiers returns an empty `additionalPriceTiers` relationship.

## See Also

### Managing Auto-Renewable Subscriptions
- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](./working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md)
  Schedule a single price to replace in-effect volume pricing, so you can unpreserve earlier subscriber prices in App Store Connect.
- [Querying adjusted subscription price equalizations](./querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)
  Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-volume-pricing-for-multi-seat-subscriptions)*
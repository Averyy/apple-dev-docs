# Configuring subscription prices across territories

**Framework**: App Store Connect API  
**Role**: Article

Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.

## Overview

The App Store Connect API lets you choose which plan type — monthly or up-front — is available for an auto-renewable subscription in each territory, and then set a consistent price for that subscription everywhere you offer it. Rather than calculating a comparable price for every territory yourself, you can read the *adjusted equalizations* of a base price point and reuse the equalized price points the API returns. This workflow assumes you already created a subscription in a subscription group. To create one, see [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md).

### Review App Store Connect API usage

If you’re new to the App Store Connect API, start with [Creating API Keys for App Store Connect API](./creating-api-keys-for-app-store-connect-api.md), [Generating Tokens for API Requests](./generating-tokens-for-api-requests.md), and [Identifying Rate Limits](./identifying-rate-limits.md).

To configure subscription plan types and prices, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

People with the `MARKETING` role can view subscription prices but can’t change them. For the full list of App Store Connect user roles, see [`UserRole`](./userrole.md) and [Program Roles](https://developer.apple.com/support/roles).

### Plan your pricing

Before you set prices, decide which plan type you offer in each territory and which territory’s price anchors the rest.

A subscription plan type controls how a customer pays for the subscription period:

- `MONTHLY` — the customer pays month to month over a 12-month commitment.
- `UPFRONT` — the customer pays the full subscription price up front.

For the complete definition, see [`SubscriptionPlanType`](./subscriptionplantype.md).

Equalization keeps a subscription’s price comparable across currencies. When you pick a price in your base territory, the API can return the *equalized* price point in every other territory — the closest local-currency equivalent. Adjusted equalizations extend this to plan types, so the equalized prices stay consistent whether a territory offers the monthly or the up-front plan.

Map out your offering before you start. The following example plans a single subscription across three territories.

| Territory | Plan type | Price (local currency) |
| --- | --- | --- |
| United States (USA) | `MONTHLY` | 9.99 USD |
| Canada (CAN) | `MONTHLY` | equalized from USA |
| Japan (JPN) | `MONTHLY` | equalized from USA |

### Set plan type availability

Declare which plan type is available for the subscription in each territory by using `POST /v1/subscriptionPlanAvailabilities` ([`Create a subscription plan availability`](./post-v1-subscriptionplanavailabilities.md)). The request requires a `planType` attribute and relationships to the `subscription` and the `availableTerritories` the plan type applies to.

Here’s an example payload:

```other
{
  "data": {
    "type": "subscriptionPlanAvailabilities",
    "attributes": {
      "planType": "MONTHLY",
      "availableInNewTerritories": true
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6447497832"
        }
      },
      "availableTerritories": {
        "data": [
          { "type": "territories", "id": "USA" },
          { "type": "territories", "id": "CAN" },
          { "type": "territories", "id": "JPN" }
        ]
      }
    }
  }
}
```

To review or change which territories offer a plan type later, use [`List plan availabilities for a subscription`](./get-v1-subscriptions-_id_-planavailabilities.md) to list the plan availabilities on a subscription, then [`Replace the available territories for a subscription plan availability`](./patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md) to update the territories. For more detail, see [Subscription plan availability](./subscription-plan-availability.md).

### Look up a base price point

Choose the base price for your subscription in your anchor territory, then look up the price point ID that represents it. Use `GET /v1/subscriptions/{id}/pricePoints` ([`List all price points for a subscription`](./get-v1-subscriptions-_id_-pricepoints.md)) and filter by territory to keep the response small.

```other
GET /v1/subscriptions/6447497832/pricePoints?filter[territory]=USA&include=territory&limit=200
```

> 💡 **Tip**:  Filter the endpoint by territory to reduce the amount of data you review. Always include `filter[territory]` on this endpoint — it’s required in a future release.

Here’s an example response, truncated for clarity:

```other
{
  "data": [
    {
      "type": "subscriptionPricePoints",
      "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ",
      "attributes": {
        "customerPrice": "9.99",
        "proceeds": "6.99"
      },
      "relationships": {
        "territory": {
          "data": { "type": "territories", "id": "USA" }
        }
      }
    }
  ]
}
```

Note the `id` of the price point whose `customerPrice` matches the base price you planned. You use it as the base price point in the next step.

### Equalize the price across territories

With your base price point, read its adjusted equalizations to get the comparable price point in every other territory. Use `GET /v1/subscriptionPricePoints/{id}/adjustedEqualizations` ([`List adjusted equalizations for a subscription price point`](./get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)), where `{id}` is the base price point ID from the previous step.

> **Note**:  Use this endpoint with filters to identify a specific adjusted equalization. Provide the `filter[upfrontPricePointId]` and `filter[planType]` query parameters:
>
> ```
> GET /v1/subscriptionPricePoints/{pricePointId}/adjustedEqualizations?filter[upfrontPricePointId]=$id&filter[planType]=MONTHLY
> ```

Add `include=territory` so each returned price point carries its territory, and filter by territory when you only need a subset:

```other
GET /v1/subscriptionPricePoints/eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ/adjustedEqualizations?filter[upfrontPricePointId]=eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ&filter[planType]=MONTHLY&include=territory&limit=200
```

Here’s an example response, truncated for clarity:

```other
{
  "data": [
    {
      "type": "subscriptionPricePoints",
      "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ",
      "attributes": {
        "customerPrice": "12.99",
        "proceeds": "9.09"
      },
      "relationships": {
        "territory": {
          "data": { "type": "territories", "id": "CAN" }
        }
      }
    },
    {
      "type": "subscriptionPricePoints",
      "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJKUE4iLCJwIjoiMTAxNTUifQ",
      "attributes": {
        "customerPrice": "1500",
        "proceeds": "1050"
      },
      "relationships": {
        "territory": {
          "data": { "type": "territories", "id": "JPN" }
        }
      }
    }
  ]
}
```

Each entry is the equalized price point for one territory. Note the `id` of each price point — you assign these when you set prices.

### Preview the effect of a price change

If a subscription already has a price in a territory, a new price can raise or lower what existing subscribers pay. Before you schedule the change, use `POST /v1/subscriptionPriceChangePreviews` to see how the proposed price compares with the current price in each territory. Send every territory in one `proposedChanges` array. Each entry lists the `territoryId`, `startDate`, and `basePricePointId`. This request doesn’t save anything.

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
          "basePricePointId": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ"
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

The response returns a `changeResults` array, with one `territoryId` and `changeType` for each proposed territory:

| `changeType` | Meaning | Effect on existing subscribers |
| --- | --- | --- |
| `INCREASE_PRESERVABLE` | The new price is higher than the current price. | They keep their current price until they cancel if you set `preserveCurrentPrice` to `true`. Otherwise, they move to the new price at their next renewal, after any required notice or consent. |
| `DECREASE_NOT_PRESERVABLE` | The new price is lower than the current price. | They move to the new price at their next renewal. Apple notifies them after that renewal. |
| `MIXED_NOT_PRESERVABLE` | The new price is higher for some seat counts and lower for others. This applies only to prices with volume pricing tiers. | They move to the new price at their next renewal, after any required notice or consent. |
| `NO_CHANGE` | The new price equals the current price. | None. |

> ❗ **Important**:  Setting `preserveCurrentPrice` to `true` keeps existing subscribers on their current price, but only when the change type is `INCREASE_PRESERVABLE`. Check the preview result for each territory before you set `preserveCurrentPrice` on a new price.

To learn more about price increases, notice, and consent, see [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md). To preview prices with volume pricing tiers, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md).

### Set prices per territory

Assign a price point to the subscription in each territory by using `POST /v1/subscriptionPrices` ([`Create a subscription price change`](./post-v1-subscriptionprices.md)). The request requires relationships to the `subscription` and the `subscriptionPricePoint`. Set `startDate` to `null` to apply the price immediately, or to a future date to schedule the change. Include `planType` to match the plan you made available. To keep existing subscribers on their current price when the change is an increase, set `preserveCurrentPrice` to `true`. Make the subscription available in the territory first. Otherwise, the request fails with `UNSUPPORTED_TERRITORY`. For more about territory availability, see [Subscription availability](./subscription-availability.md).

> ❗ **Important**:  Review price changes carefully. Once a price change goes into effect, you can’t revert it. For guidance on price changes, see [App Store Connect for iPhone and iPad](https://developer.apple.com/help/app-store-connect/).

Here’s an example payload that sets the equalized Canadian price point:

```other
{
  "data": {
    "type": "subscriptionPrices",
    "attributes": {
      "startDate": null,
      "planType": "MONTHLY"
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6447497832"
        }
      },
      "subscriptionPricePoint": {
        "data": {
          "type": "subscriptionPricePoints",
          "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ"
        }
      }
    }
  }
}
```

Repeat this call for each territory, using the equalized price point ID you noted for that territory. To schedule prices for several territories in one request instead, use `PATCH /v1/subscriptions/{id}` ([`Modify an auto-renewable subscription`](./patch-v1-subscriptions-_id_.md)). Include each price in the subscription’s `prices` relationship, and define each price in the same request’s `included` array.

The API saves each price as a single unit, and you can’t edit a subscription price after you create it. To change a scheduled price, delete it, then create a new one. A territory can have only one scheduled price at a time, so a second request fails with a `409` error until you delete the first. You can’t delete a price that’s already in effect. To change one, schedule a new price.

### Verify your prices

Confirm the prices you set by using `GET /v1/subscriptions/{id}/prices` ([`List all prices for a subscription`](./get-v1-subscriptions-_id_-prices.md)). Filter by plan type and territory to check a specific configuration.

```other
GET /v1/subscriptions/6447497832/prices?filter[planType]=MONTHLY&filter[territory]=CAN&include=subscriptionPricePoint,territory
```

If you set a price you no longer want — for example, a scheduled change that hasn’t taken effect — remove it with `DELETE /v1/subscriptionPrices/{id}` ([`Delete subscription prices`](./delete-v1-subscriptionprices-_id_.md)). You can’t delete a price that’s already in effect. To remove the tiers from one, see [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md).

For more information about subscription price points and prices, see [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md). To offer lower per-seat prices for larger purchases, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md).

## See Also

### Managing Auto-Renewable Subscriptions
- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](./working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md)
  Schedule a single price to replace in-effect volume pricing, so you can unpreserve earlier subscriber prices in App Store Connect.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-subscription-prices-across-territories)*
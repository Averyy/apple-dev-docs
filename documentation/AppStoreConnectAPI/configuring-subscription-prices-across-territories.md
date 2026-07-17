# Configuring subscription prices across territories

**Framework**: App Store Connect API

Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.

#### Overview

The App Store Connect API lets you choose which plan type — monthly or up-front — is available for an auto-renewable subscription in each territory, and then set a consistent price for that subscription everywhere you offer it. Rather than calculating a comparable price for every territory yourself, you can read the *adjusted equalizations* of a base price point and reuse the equalized price points the API returns. This workflow assumes you already created a subscription in a subscription group. To create one, see [`Managing auto-renewable subscriptions`](managing-auto-renewable-subscriptions.md).

##### Review App Store Connect Api Usage

To manage auto-renewable subscriptions with the App Store Connect API, you need to understand key concepts for using the API. If you’re new to using the App Store Connect API, make sure to read the documentation in the Essentials section of [`App Store Connect API`](AppStoreConnectAPI.md) and learn how to create API keys, generate JWTs, identify rate limits, and more.

To configure subscription plan types and prices, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles).

##### Plan Your Pricing

Before you set prices, decide which plan type you offer in each territory and which territory’s price anchors the rest.

A subscription plan type controls how a customer pays for the subscription period:

- `MONTHLY` — the customer pays month to month over a 12-month commitment.
- `UPFRONT` — the customer pays the full subscription price up front.

For the complete definition, see [`SubscriptionPlanType`](subscriptionplantype.md).

Equalization keeps a subscription’s price comparable across currencies. When you pick a price in your base territory, the API can return the *equalized* price point in every other territory — the closest local-currency equivalent. Adjusted equalizations extend this to plan types, so the equalized prices stay consistent whether a territory offers the monthly or the up-front plan.

Map out your offering before you start. The following example plans a single subscription across three territories.

| Territory | Plan type | Price (local currency) |
| --- | --- | --- |
| United States (USA) | `MONTHLY` | 9.99 USD |
| Canada (CAN) | `MONTHLY` | equalized from USA |
| Japan (JPN) | `MONTHLY` | equalized from USA |

##### Set Plan Type Availability

Declare which plan type is available for the subscription in each territory by using `POST /v1/subscriptionPlanAvailabilities` ([`Create a subscription plan availability`](post-v1-subscriptionplanavailabilities.md)). The request requires a `planType` attribute and relationships to the `subscription` and the `availableTerritories` the plan type applies to.

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

To review or change which territories offer a plan type later, use [`List plan availabilities for a subscription`](get-v1-subscriptions-_id_-planavailabilities.md) to list the plan availabilities on a subscription, then [`Replace the available territories for a subscription plan availability`](patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md) to update the territories. For more detail, see [`Subscription plan availability`](subscription-plan-availability.md).

##### Look Up a Base Price Point

Choose the base price for your subscription in your anchor territory, then look up the price point ID that represents it. Use `GET /v1/subscriptions/{id}/pricePoints` ([`List all price points for a subscription`](get-v1-subscriptions-_id_-pricepoints.md)) and filter by territory to keep the response small.

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

##### Equalize the Price Across Territories

With your base price point, read its adjusted equalizations to get the comparable price point in every other territory. Use `GET /v1/subscriptionPricePoints/{id}/adjustedEqualizations` ([`List adjusted equalizations for a subscription price point`](get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)), where `{id}` is the base price point ID from the previous step.

> **Note**:  Use this endpoint with filters to identify a specific adjusted equalization. Provide the `filter[upfrontPricePointId]` and `filter[planType]` query parameters: ```None
GET /v1/subscriptionPricePoints/{pricePointId}/adjustedEqualizations?filter[upfrontPricePointId]=$id&filter[planType]=MONTHLY
```

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

##### Set Prices Per Territory

Assign a price point to the subscription in each territory by using `POST /v1/subscriptionPrices` ([`Create a subscription price change`](post-v1-subscriptionprices.md)). The request requires relationships to the `subscription` and the `subscriptionPricePoint`. Set `startDate` to `null` to apply the price immediately, or to a future date to schedule the change. Include `planType` to match the plan you made available.

> ❗ **Important**:  Review price changes carefully. Once a price change goes into effect, you can’t revert it. For guidance on price changes, see [`App Store Connect for iPhone and iPad`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

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

Repeat this call for each territory, using the equalized price point ID you noted for that territory. There’s no bulk endpoint that applies equalized prices in a single call.

##### Verify Your Prices

Confirm the prices you set by using `GET /v1/subscriptions/{id}/prices` ([`List all prices for a subscription`](get-v1-subscriptions-_id_-prices.md)). Filter by plan type and territory to check a specific configuration.

```other
GET /v1/subscriptions/6447497832/prices?filter[planType]=MONTHLY&filter[territory]=CAN&include=subscriptionPricePoint,territory
```

If you set a price you no longer want — for example, a scheduled change that hasn’t taken effect — remove it with `DELETE /v1/subscriptionPrices/{id}` ([`Delete subscription prices`](delete-v1-subscriptionprices-_id_.md)).

For more information about subscription price points and prices, see [`Subscription price points and subscription prices`](subscription-price-points-and-subscription-prices.md).

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Querying adjusted subscription price equalizations](querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Subscription Versions](subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.
- [Subscription images (v1)](subscription-images-v1.md)
  Create, modify, and delete promotion images for your auto-renewable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-subscription-prices-across-territories)*
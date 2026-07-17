# Managing auto-renewable subscriptions

**Framework**: App Store Connect API

Create and manage subscriptions with the App Store Connect API.

#### Overview

Before you create an auto-renewable subscription, create an auto-renewable subscription group, as described in [`Creating auto-renewable subscription groups`](creating-auto-renewable-subscription-groups.md).

##### Create Your Auto Renewable Subscription

To create a subscription in your existing subscription group, use `POST /v1/subscriptions` ([`Create an auto-renewable subscription`](post-v1-subscriptions.md)) with a payload that specifies a `name` (internal only), `productId` (without spaces), and `subscriptionGroup id`. If you’re adding more subscriptions to the same group, you can also specify `groupLevel` to set the display order of subscriptions within a group. There are other attributes you can add when creating your subscription; for more information, see [`SubscriptionCreateRequest.Data.Attributes`](subscriptioncreaterequest/data-data.dictionary/attributes-data.dictionary.md).

Here’s an example payload:

```other
{
  "data": {
    "type": "subscriptions",
    "attributes": {
      "name": "All Access One Month",
      "productId": "ALLACCESS1MONTH",
      "subscriptionPeriod": "ONE_MONTH",
      "familySharable": true,
      "reviewNote": "This is the all-access tier for 1 month of ukulele lessons.",
      "groupLevel": 1,
      "availableInAllTerritories": true
    },
    "relationships": {
      "group": {
        "data": {
          "type": "subscriptionGroups",
          "id": "2000037020"
        }
      }
    }
  }
}
```

##### Localize Metadata for Your Auto Renewable Subscription

Like subscription groups, subscriptions need at least one localization. To add a localization, use `POST /v1/subscriptionLocalizations` ([`Create a subscription localization (v1)`](post-v1-subscriptionlocalizations.md)).

Here’s an example payload:

```other
{
  "data": {
    "type": "subscriptionLocalizations",
    "attributes": {
      "name": "All Access",
      "locale": "en-US",
      "description": "1 month access to all ukulele lessons."
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6446671421"
        }
      }
    }
  }
}

```

##### Configure Your Auto Renewable Subscription Pricing

The next item to configure for your subscription is pricing. First, determine the price for your subscription. You can set a unique price for each territory. To look up the price points available for the subscription, use `GET /v1/subscriptions/{id}/pricePoints` ([`List all price points for a subscription`](get-v1-subscriptions-_id_-pricepoints.md)), where the `id` is the identifier of the subscription.

Here’s an example request:

```other
GET /v1/subscriptions/6446671421/pricePoints?include=territory&filter[territory]=USA
```

> 💡 **Tip**:  This API endpoint returns many values, so filtering by territory can save you time.

Here’s an example response, truncated for clarity and sampled from the middle of the full response. This portion shows two price points:

```other
  "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDgifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDgifQ/equalizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDgifQ"
    }
  }, {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDkifQ",
    "attributes" : {
      "customerPrice" : "24.49",
      "proceeds" : "17.14",
      "proceedsYear2" : "20.82"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "USA"
        }
      },
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDkifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDkifQ/equalizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNDkifQ"
    }
  }, {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNTAifQ",
    "attributes" : {
      "customerPrice" : "24.99",
      "proceeds" : "17.49",
      "proceedsYear2" : "21.24"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "USA"
        }
      },
```

After you select the subscription price point, use `GET /v1/subscriptionPricePoints/{id}/equalizations` ([`List all subscription price point equalizations`](get-v1-subscriptionpricepoints-_id_-equalizations.md)), where the `id` is the subscription price point. In this example, the selected price point is `24.99`, which has an `id` of `eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNTAifQ`.

Here’s an example request using that price point `id`, with the additional included `territory`:

```other
GET /v1/subscriptionPricePoints/
eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNTAifQ
/equalizations?include=territory
```

Here’s an example response, truncated for clarity:

```other
{
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJNRVgiLCJwIjoiNzEifQ",
    "attributes" : {
      "customerPrice" : "499.0",
      "proceeds" : "349.3",
      "proceedsYear2" : "424.15"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "MEX"
        }
      },
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJNRVgiLCJwIjoiNzEifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJNRVgiLCJwIjoiNzEifQ/equalizations"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJNRVgiLCJwIjoiNzEifQ"
    }
  }, {
    "type" : "subscriptionPricePoints",
    "id" : "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJMVVgiLCJwIjoiNDEifQ",
    "attributes" : {
      "customerPrice" : "20.49",
      "proceeds" : "14.34",
      "proceedsYear2" : "17.42"
    },
    "relationships" : {
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "LUX"
        }
      },
```

The following example shows the equalized price points for Mexico (`MEX`) and Luxembourg (`LUX`). The three price points (`USA`, `MEX`, and `LUX`) are now identified.

| Territory | `customerPrice` | `id` |
| --- | --- | --- |
| `USA` | `24.99` | `eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNTAifQ` |
| `MEX` | `499.0` | `eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJNRVgiLCJwIjoiNzEifQ` |
| `LUX` | `20.49` | `eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJMVVgiLCJwIjoiNDEifQ` |

The `customerPrice` shows in the local currency for that territory. Because Luxembourg uses the Euro and Mexico uses the Mexican peso, the `customerPrice` number isn’t exactly the `24.99` of the base currency from the equalization lookup (US dollars).

Use `POST /v1/subscriptionPrices` ([`Create a subscription price change`](post-v1-subscriptionprices.md)) with a payload like in the following example, in which the `subscriptionPricePoint` is set for `USA`:

```other
{
  "data": {
    "type": "subscriptionPrices",
    "attributes": {
      "startDate": "2022-06-29",
      "preserveCurrentPrice": true
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6446659888"
        }
      },
      "subscriptionPricePoint": {
        "data": {
          "type": "subscriptionPricePoints",
          "id": "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiNTAifQ"
        }
      }
    }
  }
}
```

> **Note**:  The territory isn’t necessary to include because the price point is unique to the territory.

To set a price point for another territory, use `POST /v1/subscriptionPrices` ([`Create a subscription price change`](post-v1-subscriptionprices.md)) again, replacing the `subscriptionPricePoint` ID with the other values you obtain from `GET /v1/subscriptionPricePoints/{id}/equalizations` ([`List all subscription price point equalizations`](get-v1-subscriptionpricepoints-_id_-equalizations.md)). If the subscription is available in all territories, an individual `POST /v1/subscriptionPrices` call is necessary for each territory. You might consider automating this step.

> ❗ **Important**:  Review carefully because after a price goes into effect, you can’t revert it. Be sure to review information about price increases and changes at [`Add a new app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

##### Configure Billing Grace Period for Your App

After adding support for Billing Grace Period to your app, you can set the state for subscriptions. When you support Billing Grace Period in your app, it lets subscribers retain access to your app’s paid content for a period of time if their subscription expires due to a billing issue. If Apple successfully recovers the subscription within the grace period, you don’t experience any interruption in your revenue. Before you turn on Billing Grace Period in App Store Connect, you need to update your entitlement logic to ensure you’re providing service to customers within the grace period. For more information, see [`Reducing Involuntary Subscriber Churn`](https://developer.apple.com/documentation/StoreKit/reducing-involuntary-subscriber-churn) and [`Enable Billing Grace Period for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev58bda3212).

To change the status of Billing Grace Period for your app, use `PATCH /v1/subscriptionGracePeriods/{id}` ([`Modify the billing grace period opt-in status and duration`](patch-v1-subscriptiongraceperiods-_id_.md)), where the `id` in the URL and in the payload is the app’s Apple ID.

> **Note**:  This change applies to all subscriptions within an app.

Here’s an example payload:

```other
{
  "data": {
    "id": "6446148572",
    "type": "subscriptionGracePeriods",
    "attributes": {
      "optIn": true
    }
  }
}
```

You can provide additional attributes to control the duration of the grace period and the type of subscribers that are eligible, as well as set the state for the sandbox environment. For more information, see [`SubscriptionGracePeriodUpdateRequest.Data.Attributes`](subscriptiongraceperiodupdaterequest/data-data.dictionary/attributes-data.dictionary.md).

##### Promote Your Auto Renewable Subscriptions

You can promote an auto-renewable subscription to users who visit your app listing in the App Store. Use `POST /v1/promotedPurchases` ([`Promote a purchase`](post-v1-promotedpurchases.md)) with a payload that includes your Apple ID and the ID for your auto-renewable subscription. The response confirms the state is `"Waiting for Review"`. You can also look up the state of a specific promoted purchase by using `GET /v1/promotedPurchases` ([`Read promoted purchase information for an in-app purchase`](get-v2-inapppurchases-_id_-promotedpurchase.md)), or look up the status of all your promoted purchases for an app by using `GET /v1/apps/{id}/promotedPurchases` ([`List all promoted purchases for an app`](get-v1-apps-_id_-promotedpurchases.md)).

Here’s an example payload:

```other
{
  "data": {
    "type": "promotedPurchases",
    "attributes": {
      "visibleForAllUsers": true,
      "enabled": true
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6446148572"
        }
      },
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6446671421"
        }
      }
    }
  }
}

```

## See Also

- [Working with subscription versions](working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/managing-auto-renewable-subscriptions)*
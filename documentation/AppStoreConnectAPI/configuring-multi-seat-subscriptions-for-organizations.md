# Configuring multi-seat subscriptions for organizations

**Framework**: App Store Connect API

Control whether organizations can purchase an auto-renewable subscription for multiple people, and which markets offer it.

#### Overview

Organizations can buy your auto-renewable subscriptions in quantities greater than one through Apple Business Manager (Enterprise) and Apple School Manager (Education). To learn more, see [`Apple School Manager and Apple Business APIs`](https://developer.apple.com/documentation/apple-school-and-business-manager-api). Use the `multiSeatStatus` and `marketSettings` attributes on the subscriptions resource to control whether a subscription supports these multi-seat purchases and which markets offer it. Both attributes apply only to auto-renewable subscriptions; updating them on any other in-app purchase type returns an error.

Before you configure multi-seat settings, create an auto-renewable subscription as described in [`Managing auto-renewable subscriptions`](managing-auto-renewable-subscriptions.md). To update these attributes, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

API keys with the `MARKETING` role have read-only access to both attributes.

##### Turn Multi Seat Purchasing on or Off

Every auto-renewable subscription defaults to `multiSeatStatus` of `ENABLED`, so you only need to set this attribute when you want to change a subscription’s current state. To update it, use [`Modify an auto-renewable subscription`](patch-v1-subscriptions-_id_.md) with a payload that sets the `multiSeatStatus`.

Here’s an example payload that turns multi-seat purchasing on for a subscription:

```other
{
  "data": {
    "type": "subscriptions",
    "id": "6446671421",
    "attributes": {
      "multiSeatStatus": "ENABLED"
    }
  }
}
```

The `multiSeatStatus` attribute accepts the following values:

| Value | Description |
| --- | --- |
| `ENABLED` | An organization can purchase the subscription in quantities greater than one. This is the default for every auto-renewable subscription. |
| `DISABLED` | Restricts the subscription to single-seat (quantity of one) purchases. New multi-seat purchases stop, and Apple Business Manager and Apple School Manager no longer offer the SKU. Existing multi-seat subscribers keep renewing at their current seat count but can’t add seats. |

> **Note**:  Turning on Family Sharing for a subscription automatically sets `multiSeatStatus` to `DISABLED`. If you turn multi-seat purchasing back on for a family-shareable subscription, Family Sharing only applies when the a single seat is purchased.

##### Choose Which Markets Offer Multi Seat Purchases

After you turn on multi-seat purchasing, use the `marketSettings` attribute to choose which markets support multi-seat purchases of the subscription. Update it with the same `PATCH /v1/subscriptions/{id}` ([`Modify an auto-renewable subscription`](patch-v1-subscriptions-_id_.md)) endpoint, providing an array of markets.

Here’s an example payload that makes a subscription available for multi-seat purchase on the App Store and through Apple Business Manager, but not Apple School Manager:

```other
{
  "data": {
    "type": "subscriptions",
    "id": "6446671421",
    "attributes": {
      "marketSettings": [
        "APP_STORE",
        "APPLE_BUSINESS"
      ]
    }
  }
}
```

`marketSettings` accepts an array containing any of the following values:

| Value | Description |
| --- | --- |
| `APP_STORE` | The subscription is available for multi-seat purchase directly on the App Store. |
| `APPLE_BUSINESS` | The subscription is available for purchase in quantity through Apple Business Manager, for enterprise organizations. |
| `APPLE_SCHOOL` | The subscription is available for purchase in quantity through Apple School Manager, for education institutions. |

> ❗ **Important**:  `marketSettings` only has an effect while `multiSeatStatus` is `ENABLED`. If `multiSeatStatus` is `DISABLED`, the subscription isn’t available for multi-seat purchase in any market, regardless of which values you set in `marketSettings`.

##### Verify Your Configuration

To confirm the current settings, use `GET /v1/subscriptions/{id}` ([`Read subscription information`](get-v1-subscriptions-_id_.md)) and check the `multiSeatStatus` and `marketSettings` values in the response.

For example:

```other
GET /v1/subscriptions/6446671421
```

Here’s the example response, truncated for clarity:

```other
{
  "data" : {
    "type" : "subscriptions",
    "id" : "6446671421",
    "attributes" : {
      "multiSeatStatus" : "ENABLED",
      "marketSettings" : [ "APP_STORE", "APPLE_BUSINESS" ]
    }
  }
}
```

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-multi-seat-subscriptions-for-organizations)*
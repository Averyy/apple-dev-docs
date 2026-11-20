# Configuring multiseat subscriptions for organizations

**Framework**: App Store Connect API  
**Role**: Article

Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.

## Overview

Organizations can buy your auto-renewable subscriptions in quantities greater than one through [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/) (Enterprise) and [Apple School Manager](https://support.apple.com/guide/apple-school-manager/) (Education). To learn more, see [Apple School Manager and Apple Business APIs](../apple-school-and-business-manager-api/apple-school-and-business-manager-api.md). Use the `multiSeatStatus` and `marketSettings` attributes on the subscriptions resource to control whether a subscription supports these multiseat purchases and which markets offer it. Both attributes apply only to auto-renewable subscriptions; updating them on any other in-app purchase type returns an error. To choose whether Apple or your app hosts seat invitations for multiseat purchases on the App Store, use the `groupPurchaseInvitationMode` attribute on the apps resource.

Before you configure multiseat settings, create an auto-renewable subscription as described in [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md). To update these attributes, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`

API keys with the `MARKETING` role have read-only access to all three attributes.

### Turn multiseat purchasing on or off

Every auto-renewable subscription defaults to `multiSeatStatus` of `ENABLED`, so you only need to set this attribute when you want to change a subscription’s current state. To update it, use [`Modify an auto-renewable subscription`](./patch-v1-subscriptions-_id_.md) with a payload that sets the `multiSeatStatus`.

Here’s an example payload that turns multiseat purchasing on for a subscription:

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
| `DISABLED` | Restricts the subscription to single-seat (quantity of one) purchases. New multiseat purchases stop, and Apple Business Manager and Apple School Manager no longer offer the SKU. Existing multiseat subscribers keep renewing at their current seat count but can’t add seats. |

> **Note**:  Turning on Family Sharing for a subscription automatically sets `multiSeatStatus` to `DISABLED`. If you turn multiseat purchasing back on for a family-shareable subscription, Family Sharing only applies when the a single seat is purchased.

### Choose which markets offer multiseat purchases

After you turn on multiseat purchasing, use the `marketSettings` attribute to choose which markets support multiseat purchases of the subscription. Update it with the same `PATCH /v1/subscriptions/{id}` ([`Modify an auto-renewable subscription`](./patch-v1-subscriptions-_id_.md)) endpoint, providing an array of markets.

Here’s an example payload that makes a subscription available for multiseat purchase on the App Store and through Apple Business Manager, but not Apple School Manager:

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
| `APP_STORE` | The subscription is available for multiseat purchase directly on the App Store. |
| `APPLE_BUSINESS` | The subscription is available for purchase in quantity through Apple Business Manager, for enterprise organizations. |
| `APPLE_SCHOOL` | The subscription is available for purchase in quantity through Apple School Manager, for education institutions. |

> ❗ **Important**:  `marketSettings` only has an effect while `multiSeatStatus` is `ENABLED`. If `multiSeatStatus` is `DISABLED`, the subscription isn’t available for multiseat purchase in any market, regardless of which values you set in `marketSettings`.

### Choose who hosts seat invitations

When a customer buys multiple seats of a subscription on the App Store, they invite other people to use those seats. The `groupPurchaseInvitationMode` attribute on the apps resource controls who hosts those invitations. You set it once for your app, and it applies to every multiseat subscription in the app. It doesn’t affect single-seat purchases or seats that organizations assign through [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/) and [Apple School Manager](https://support.apple.com/guide/apple-school-manager/).

`groupPurchaseInvitationMode` accepts the following values:

| Value | Description |
| --- | --- |
| `APPLE_HOSTED` | Apple sends seat invitations and manages how members accept them. This is the default for every app. |
| `DEVELOPER_HOSTED` | Your app hosts its own invitation and seat acceptance flow. The flow can run outside Apple platforms, such as on the web, and members don’t need an Apple Account to accept a seat. |

To change it, use `PATCH /v1/apps/{id}` ([`Modify an app`](./patch-v1-apps-_id_.md)). Here’s an example payload that switches an app to developer-hosted invitations:

```other
{
  "data": {
    "type": "apps",
    "id": "6446671400",
    "attributes": {
      "groupPurchaseInvitationMode": "DEVELOPER_HOSTED"
    }
  }
}
```

A change applies only to multiseat purchases made after you save it. Existing subscriptions keep the invitation mode that was in effect when the customer bought them. Changing the mode doesn’t require App Review, and you can switch back at any time.

> ❗ **Important**:  If you set `DEVELOPER_HOSTED`, your app is responsible for verifying the age of invited members and getting any required parental consent before they accept an invitation. To learn more, see [Declared Age Range](../DeclaredAgeRange/DeclaredAgeRange.md).

### Verify your configuration

To confirm the current settings, use `GET /v1/subscriptions/{id}` ([`Read subscription information`](./get-v1-subscriptions-_id_.md)) and check the `multiSeatStatus` and `marketSettings` values in the response.

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

To confirm the invitation mode, use `GET /v1/apps/{id}` ([`Read app information`](./get-v1-apps-_id_.md)) and check the `groupPurchaseInvitationMode` value in the response:

```other
GET /v1/apps/6446671400?fields[apps]=groupPurchaseInvitationMode
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-multi-seat-subscriptions-for-organizations)*
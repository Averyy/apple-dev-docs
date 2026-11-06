# Setting up retention messaging for auto-renewable subscriptions

**Framework**: App Store Connect API  
**Role**: Article

Create a retention message, write its localized content, and assign it and any retention offers to a subscription.

## Overview

When people start to cancel an auto-renewable subscription, a retention message gives them a reason to stay subscribed. You can pair a message with retention offers, which are discounted offers for the same subscription.

The examples use a coffee-subscription app named Example App (`exa`). For information about choosing which message and offer people see in real time from your server, see [Retention Messaging API](../RetentionMessaging/RetentionMessaging.md).

### Understand the resources

Retention messaging uses these resources:

- **retentionMessages**: The container for a message, which belongs to one app and has a `referenceName` that you use in App Store Connect. See [Retention messages](./retention-messages.md).
- **`retentionMessageVersions`**: A version of the message content that you submit to App Review. See [Retention message versions](./retention-message-versions.md).
- **retentionMessageLocalizations**: The `header` and `body` text of a version for one locale. See [Retention message localizations](./retention-message-localizations.md).
- **retentionOffers**: A discounted offer for a subscription that you present alongside a message. See [Retention offers](./retention-offers.md).

An app can have at most 10 retention messages, and a subscription has at most one retention message.

### Create a retention message

To create a message, send `POST /v1/retentionMessages` ([`Create a retention message`](./post-v1-retentionmessages.md)) with a `referenceName` of up to 64 characters and the app it belongs to. People don’t see the reference name when the retention message appears.

```json
{
  "data": {
    "type": "retentionMessages",
    "attributes": {
      "referenceName": "exa-winter-stay-with-us"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6446671421"
        }
      }
    }
  }
}
```

The response contains the new message’s resource ID. To find the messages that already exist for an app, use [`List retention messages for an app`](./get-v1-apps-_id_-retentionmessages.md). You can’t change a message’s `referenceName` after you create it. To remove a message you no longer need, use [`Delete a retention message`](./delete-v1-retentionmessages-_id_.md).

### Create a version of the message

A message holds its content in versions. To create one, send `POST /v1/retentionMessageVersions` ([`Create a retention message version`](./post-v1-retentionmessageversions.md)) with the `retentionMessage` relationship. The `placement` relationship is optional; include it to show an image from your app’s asset library, or leave it out for a text-only message.

```json
{
  "data": {
    "type": "retentionMessageVersions",
    "relationships": {
      "retentionMessage": {
        "data": {
          "type": "retentionMessages",
          "id": "9137205548"
        }
      },
      "placement": {
        "data": {
          "type": "appAssetLibraryPlacements",
          "id": "c3a1f0e2-6b7d-4e55-9a0c-2f4d8b1e7a90"
        }
      }
    }
  }
}
```

A new version starts in the `PREPARE_FOR_SUBMISSION` state. To create the placement, see [Placing assets on your App Store surfaces](./placing-assets-on-your-app-store-surfaces.md).

> ❗ **Important**:  You can’t modify or delete a version after you create it, and you can’t add localizations to a version that’s `APPROVED`. To change approved content, create a new version of the message.

### Add localized text

Add a localization for each locale that you support. Send `POST /v1/retentionMessageLocalizations` ([`Create a retention message localization`](./post-v1-retentionmessagelocalizations.md)) with the `locale`, the `header` and `body` text, and the version it belongs to. The `header` can contain up to 66 characters, and the `body` can contain up to 144 characters.

```json
{
  "data": {
    "type": "retentionMessageLocalizations",
    "attributes": {
      "locale": "en-US",
      "header": "Your cortado is waiting",
      "body": "Stay subscribed and keep your daily cortado coming."
    },
    "relationships": {
      "retentionMessageVersion": {
        "data": {
          "type": "retentionMessageVersions",
          "id": "4820193376"
        }
      }
    }
  }
}
```

To edit the text of an existing localization, use [`Modify a retention message localization`](./patch-v1-retentionmessagelocalizations-_id_.md). You can update the `header` and `body`, but not the `locale`. To remove a locale, use [`Delete a retention message localization`](./delete-v1-retentionmessagelocalizations-_id_.md).

### Create retention offers

To present a discount with your message, create a retention offer for the subscription with [`Create a retention offer`](./post-v1-retentionoffers.md). Every offer requires the following attributes:

- `referenceName`
- `offerId`, which identifies the offer in StoreKit
- `duration`
- `offerMode`
- `periodCount`
- `customerEligibilityPaidSubscriptionDurationInMonths`

An offer also requires the `subscription` it belongs to and the `prices` relationship. The `customerEligibilityPaidSubscriptionDurationInMonths` attribute is the minimum number of months of paid subscription that makes a person eligible. It accepts 1 to 24, 36, 48, and 60. To set how long people wait before they can redeem another retention offer for the same subscription, use the optional `customerEligibilityWaitBetweenOffersInMonths` attribute, which accepts 2 to 24.

The `duration` attribute accepts `THREE_DAYS`, `ONE_WEEK`, `TWO_WEEKS`, `ONE_MONTH`, `TWO_MONTHS`, `THREE_MONTHS`, `SIX_MONTHS`, and `ONE_YEAR`.

The `offerMode` attribute accepts `PAY_AS_YOU_GO`, `PAY_UP_FRONT`, and `FREE_TRIAL`.

The optional `targetSubscriptionPlanType` attribute is the plan type that people subscribe to after the offer ends. It accepts `MONTHLY` and `UPFRONT`. A subscription can have at most 10 active retention offers for each `targetSubscriptionPlanType`.

An offer’s prices are subscription prices. To find the price points for a subscription, use [`List all price points for a subscription`](./get-v1-subscriptions-_id_-pricepoints.md). For more information about subscription prices across territories, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md).

You create the prices with the offer. For each price, add a [`RetentionOfferPrice`](./retentionofferprice.md) resource to the top-level `included` array and reference it in the `prices` relationship. Give each price a local ID in the form `${local-id}` to link the relationship to the included resource. Each included price needs only the `subscriptionPricePoint` relationship, you don’t specify a territory.

For example:

```json
{
  "data": {
    "type": "retentionOffers",
    "attributes": {
      "referenceName": "exa-winter-one-month-offer",
      "offerId": "exa_winter_one_month",
      "duration": "ONE_MONTH",
      "offerMode": "PAY_UP_FRONT",
      "periodCount": 1,
      "customerEligibilityPaidSubscriptionDurationInMonths": 3,
      "customerEligibilityWaitBetweenOffersInMonths": 6,
      "targetSubscriptionPlanType": "UPFRONT"
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6446671421"
        }
      },
      "prices": {
        "data": [
          {
            "type": "retentionOfferPrices",
            "id": "${price1}"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "retentionOfferPrices",
      "id": "${price1}",
      "relationships": {
        "subscriptionPricePoint": {
          "data": {
            "type": "subscriptionPricePoints",
            "id": "eyJzIjoiNjQ0NjY3MTQyMSIsInQiOiJVU0EiLCJwIjoiMTAwMDEifQ"
          }
        }
      }
    }
  ]
}
```

To set a price for another territory, add another price resource with that territory’s price point.

After you create an offer, you can update its eligibility rules with [`Modify a retention offer`](./patch-v1-retentionoffers-_id_.md). The eligibility attributes are the only attributes you can change. To find a subscription’s offers, use [`List retention offers for a subscription`](./get-v1-subscriptions-_id_-retentionoffers.md).

> **Note**:  Creating a retention offer doesn’t present it to people. To present an offer with a subscription’s retention message, assign it to the subscription’s retention message offers.

### Assign the message and offers to a subscription

To assign a message to a subscription, send `PATCH /v1/subscriptions/{id}/relationships/retentionMessage` ([`Replace the retention message for a subscription`](./patch-v1-subscriptions-_id_-relationships-retentionmessage.md)) with the message’s resource ID. If successful, the endpoint returns `204` with no response body.

```json
{
  "data": {
    "type": "retentionMessages",
    "id": "9137205548"
  }
}
```

Assigning a message replaces the subscription’s existing retention message.

To choose which offers to present, send `POST /v1/subscriptions/{id}/relationships/retentionMessageOffers` ([`Add retention message offers to a subscription`](./post-v1-subscriptions-_id_-relationships-retentionmessageoffers.md)) with the offers to add:

```json
{
  "data": [
    {
      "type": "retentionOffers",
      "id": "7710428835"
    }
  ]
}
```

To remove offers, send the same body with [`Remove retention message offers from a subscription`](./delete-v1-subscriptions-_id_-relationships-retentionmessageoffers.md).

### Submit the version for review

All retention messages go through App Review before people can see them. To submit, create a review submission item that references the version. Send `POST /v1/reviewSubmissionItems` ([`Create a Review Submission Item`](./post-v1-reviewsubmissionitems.md)) with the `reviewSubmission` and `retentionMessageVersion` relationships:

```json
{
  "data": {
    "type": "reviewSubmissionItems",
    "relationships": {
      "reviewSubmission": {
        "data": {
          "type": "reviewSubmissions",
          "id": "e1d9a3c4-0f52-4b8a-bb71-5c3a9d2e6f08"
        }
      },
      "retentionMessageVersion": {
        "data": {
          "type": "retentionMessageVersions",
          "id": "4820193376"
        }
      }
    }
  }
}
```

For information about creating and submitting a review submission, see [Review submissions](./review-submissions.md) and [Review submission items](./review-submission-items.md).

### Check the review state

To follow the version through review, use [`Read a retention message version`](./get-v1-retentionmessageversions-_id_.md) and read its `state` attribute. A version moves through `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED` or `REJECTED`, and then `APPROVED`. If you withdraw a version from review, its state is `DEVELOPER_REJECTED`.

Here’s the example response, truncated for clarity:

```json
{
  "data": {
    "type": "retentionMessageVersions",
    "id": "4820193376",
    "attributes": {
      "state": "WAITING_FOR_REVIEW"
    }
  }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/setting-up-retention-messaging)*
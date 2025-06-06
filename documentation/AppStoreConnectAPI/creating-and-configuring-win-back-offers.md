# Creating and configuring win-back offers

**Framework**: Appstoreconnectapi

Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.

#### Overview

The App Store Connect API lets you create and configure win-back offers for your auto-renewable subscriptions. You can create win-back offers for approved subscriptions. After creation, you can make changes to start date, end date and eligibility parameters, and edit some metadata for your win-back offer. You can have multiple win-back offers for a single subscription.

##### Review App Store Connect Api Usage

To manage auto-renewable subscriptions with the App Store Connect API, you need to understand key concepts for using the API. If youʼre new to using the App Store Connect API, make sure to read the documentation in the Essentials section of App Store Connect API and learn how to create API keys, generate JWTs, identify rate limits, and more.

To create and manage win-back offers, be sure you have one of the following user roles:

- `ACCOUNT_HOLDER`
- `ADMIN`
- `APP_MANAGER`
- `MARKETING`

For the full list of App Store Connect user roles, see [`UserRole`](userrole.md) and [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles).

##### Prepare Your App for Win Back Offers

Your app and subscriptions need to be approved before you can create a win-back offer. If you are using App Store promotion, you need an approved promoted-purchase image. To learn more, see [`Create an image for a subscription`](post-v1-subscriptionimages.md).

> **Note**:  The `familySharable` field is editable only for auto-renewable subscriptions and non-consumable in-app purchases before the subscription or in-app purchase is approved by App Review.

##### Plan Your Win Back Offer

Begin by determining the subscription that needs the win-back offer. Get the subscriptionID by calling List All Subscriptions for a Subscription Group. Next, look up the price points you want in your win-back offer for your subscription by using List All Price Points for a Subscription. When you create your win-back offer, you choose the territories where it is available and prices for those territories, after creation you cannot change the territory availability or prices.

> 💡 **Tip**:  It is helpful to filter by territory when looking up price points. Use includes and filters like this: `v1/subscriptions/id/pricePoints?include=territory&filter[territory]=CAN`

When setting up your win-back offer, a large part of configuration is determining eligibility. This list details the eligibility parameters available:

| Attribute Name | Description |
| --- | --- |
| `customerEligibilityPaidSubscriptionDurationInMonths` | How long a customer was a subscriber. |
| `customerEligibilityTimeSinceLastSubscribedInMonths` | How long since the subscriber last had an active subscription. |
| `customerEligibilityWaitBetweenOffersInMonths` (optional) | How much time must pass between the end of their offer period and redeeming the same offer again. |

##### Create Your Win Back Offer

After you plan your win-back offer, you can create it by using Create a win-back offer with a payload. For more information about each attribute in this payload, see [`WinBackOfferCreateRequest.Data.Attributes`](winbackoffercreaterequest/data-data.dictionary/attributes-data.dictionary.md).

> ❗ **Important**:  Use a unique referenceName and offerId that you have not used for a promotional offer, offer code, or introductory offer, when you create your win-back offer.

Here’s an example request:

```json
POST https://api.appstoreconnect.apple.com/v1/winBackOffers
{
  "data": {
    "type": "winBackOffers",
    "attributes": {
      "referenceName": "6 Months for 3 A",
      "offerId": "6Monthfor3_a",
      "startDate": "2024-07-01",
      "endDate": "2024-07-31",
      "priority": "HIGH",
      "promotionIntent": "USE_AUTO_GENERATED_ASSETS",
      "customerEligibilityPaidSubscriptionDurationInMonths": 6,
      "customerEligibilityTimeSinceLastSubscribedInMonths": {
        "minimum": 2,
        "maximum": 24
      },
      "customerEligibilityWaitBetweenOffersInMonths": 2,
      "duration": "SIX_MONTHS",
      "offerMode": "PAY_UP_FRONT",
      "periodCount": 1
    },
    "relationships": {
      "subscription": {
        "data": {
          "type": "subscriptions",
          "id": "6447497832"
        }
      },
      "prices": {
        "data": [
          {
            "id": "${winbackOfferPrice-0}",
            "type": "winBackOfferPrices"
          },
          {
            "id": "${winbackOfferPrice-1}",
            "type": "winBackOfferPrices"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "winBackOfferPrices",
      "id": "${winbackOfferPrice-0}",
      "relationships": {
        "subscriptionPricePoint": {
          "data": {
            "type": "subscriptionPricePoints",
            "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJVU0EiLCJwIjoiMTAxMjcifQ"
          }
        }
      }
    },
    {
      "type": "winBackOfferPrices",
      "id": "${winbackOfferPrice-1}",
      "relationships": {
        "subscriptionPricePoint": {
          "data": {
            "type": "subscriptionPricePoints",
            "id": "eyJzIjoiNjQ0NzQ5NzgzMiIsInQiOiJDQU4iLCJwIjoiMTAxNDIifQ"
          }
        }
      }
    }
  ]
}

```

Here’s a sample response, truncated for clarity:

```json
{
  "data": {
    "type": "winBackOffers",
    "id": "10778326500",
    "attributes": {
      "referenceName": "6 Months for 3 A",
      "offerId": "6Monthfor3_a",
      "duration": "SIX_MONTHS",
      "offerMode": "PAY_UP_FRONT",
      "periodCount": 1,
      "customerEligibilityPaidSubscriptionDurationInMonths": 6,
      "customerEligibilityTimeSinceLastSubscribedInMonths": {
        "minimum": 2,
        "maximum": 24
      },
      "customerEligibilityWaitBetweenOffersInMonths": 2,
      "startDate": "2024-07-01",
      "endDate": "2024-07-31",
      "priority": "HIGH",
      "promotionIntent": "USE_AUTO_GENERATED_ASSETS"
    },
    "relationships": {
      "promotion": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/relationships/promotion",
          "related": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/promotion"
        }
      },

```

##### Share and Promote Your Win Back Offer

After your create your win-back offer, you can promote the offer in multiple ways. Your appʼs page in App Store promotes your win-back offer if you set `promotionIntent` to `USE_AUTO_GENERATED_ASSETS` and if you also have an approved promoted-purchase image, beginning on the `startDate` you set for your win-back offer. Your win-back offer displays with the priority chosen, `NORMAL` or `HIGH`, in accordance with any other offers or In-App Events.

You can also use a URL to promote your win-back offer. To construct a url like this https://apps.apple.com/win-back/{Offer Apple ID}, use the ID (numerical value created by Apple) of the win-back offer that is in the responses from Create a win-back offer or List win-back offers. For the win-back offer example above, the URL is https://apps.apple.com/win-back/10778326500.

##### Read Information About and Update Your Win Back Offer

You can review your win-back offers by using List win-back offers. Once you create your offer, you can update many of the attributes, including eligibility requirements, start and end dates, priority, and promotion intent, by using Modify a win-back offer. After your offer is live, you can modify the priority attribute. You aren’t able to update the territories that are included in an existing win-back offer. To add more territories, you need to create a new win-back offer.

## See Also

- [List win-back offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [Read win-back offer information](get-v1-winbackoffers-_id_.md)
  Read details about a specific win-back offer.
- [List win-back offer prices](get-v1-winbackoffers-_id_-prices.md)
  List all prices for specific win-back offers.
- [Create a win-back offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a win-back offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.
- [Delete a win-back offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/creating-and-configuring-win-back-offers)*
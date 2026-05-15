# Create a Win-Back Offer

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a win-back offer for a specific subscription.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

> **Note**: Important Use a unique referenceName and offerId that you have not used for a promotional offer, offer code, or introductory offer, when you create your win-back offer.

##### Example Request and Response

**Request**:

```None
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

**Response**:

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
      "prices": {
        "meta": {
          "paging": {
            "total": 2,
            "limit": 10
          }
        },
        "data": [
          {
            "type": "winBackOfferPrices",
            "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiQ0FOIiwicCI6IjEwMTQyIn0"
          },
          {
            "type": "winBackOfferPrices",
            "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiVVNBIiwicCI6IjEwMTI3In0"
          }
        ],
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/relationships/prices",
          "related": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/prices"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500"
    }
  },
  "included": [
    {
      "type": "winBackOfferPrices",
      "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiQ0FOIiwicCI6IjEwMTQyIn0",
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/winBackOfferPrices/eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiQ0FOIiwicCI6IjEwMTQyIn0"
      }
    },
    {
      "type": "winBackOfferPrices",
      "id": "eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiVVNBIiwicCI6IjEwMTI3In0",
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/winBackOfferPrices/eyJvIjoiMTA3NzgzMjY1MDAiLCJ0IjoiVVNBIiwicCI6IjEwMTI3In0"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers"
  }
}

```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/winBackOffers`

## See Also

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List Win-Back Offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/winBackOffers](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [Read Win-Back Offer Information](get-v1-winbackoffers-_id_.md)
  Read details about a specific win-back offer.
- [List Win-Back Offer Prices](get-v1-winbackoffers-_id_-prices.md)
  List all prices for specific win-back offers.
- [GET /v1/winBackOffers/{id}/relationships/prices](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Modify a Win-Back Offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.
- [Delete a Win-Back Offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-winbackoffers)*
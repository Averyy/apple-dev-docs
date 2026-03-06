# Read win-back offer information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read details about a specific win-back offer.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500       
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
      "promotionIntent": "NOT_PROMOTED"
    },
    "relationships": {
      "promotion": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/relationships/promotion",
          "related": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500/promotion"
        }
      },
      "prices": {
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
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/winBackOffers/10778326500"
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/winBackOffers/{id}`

## Parameters

- `fields[winBackOfferPrices]` ([string])
- `fields[winBackOffers]` ([string])
- `include` ([string])
- `limit[prices]` (integer)

## See Also

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)
  Configure win-back offers for your auto-renewable subscriptions with the App Store Connect API.
- [List win-back offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/winBackOffers](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
- [List win-back offer prices](get-v1-winbackoffers-_id_-prices.md)
  List all prices for specific win-back offers.
- [GET /v1/winBackOffers/{id}/relationships/prices](get-v1-winbackoffers-_id_-relationships-prices.md)
- [Create a win-back offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Modify a win-back offer](patch-v1-winbackoffers-_id_.md)
  Edit details for a specific win-back offer.
- [Delete a win-back offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-winbackoffers-_id_)*
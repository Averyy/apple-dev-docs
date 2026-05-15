# Modify a Win-Back Offer

**Framework**: App Store Connect API  
**Kind**: httpRequest

Edit details for a specific win-back offer.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/winBackOffers/10759170294
{
  "data": {
    "type": "winBackOffers",
    "id": "10778326500",
    "attributes": {
      "promotionIntent": "USE_AUTO_GENERATED_ASSETS",
      "startDate": "2024-07-04",
      "endDate": "2024-07-31"
    }
  }
}        
```

**Response**:

```json
"data": {
  "type": "winBackOffers",
  "id": "10778326500",
  "attributes": {
    "referenceName": "6 Months for 3 A",
    "offerId": "6Monthfor3_a",
    "duration": "SIX_MONTHS",
    "offerMode": "PAY_UP_FRONT",
    "periodCount": 1,
    "customerEligibilityPaidSubscriptionTenureInMonths": null,
    "customerEligibilityPaidSubscriptionDurationInMonths": 6,
    "customerEligibilityTimeSinceLastSubscribedInMonths": {
      "minimum": 2,
      "maximum": 24
    },
    "customerEligibilityWaitBetweenOffersInMonths": 2,
    "startDate": "2024-07-04",
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

`PATCH https://api.appstoreconnect.apple.com/v1/winBackOffers/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `winBackOffers` resource ID from the [`List Win-Back Offers`](get-v1-subscriptions-_id_-winbackoffers.md) response.

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
- [Create a Win-Back Offer](post-v1-winbackoffers.md)
  Create a win-back offer for a specific subscription.
- [Delete a Win-Back Offer](delete-v1-winbackoffers-_id_.md)
  Remove a win-back offer for a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-winbackoffers-_id_)*
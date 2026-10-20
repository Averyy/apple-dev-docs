# List all promoted purchases for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of promoted In-App Purchases, including promoted auto-renewable subscriptions, for an app.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/1000001234/promotedPurchases
```

**Response**:

```json
{
  "data": [
    {
      "type": "promotedPurchases",
      "id": "bec0022d-99b1-69b6-7524-e051b51f1976",
      "attributes": {
        "visibleForAllUsers": true,
        "enabled": true,
        "state": "APPROVED"
      },
      "relationships": {
        "promotionImages": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/bec0022d-99b1-69b6-7524-e051b51f1976/relationships/promotionImages",
            "related": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/bec0022d-99b1-69b6-7524-e051b51f1976/promotionImages"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/bec0022d-99b1-69b6-7524-e051b51f1976"
      }
    },
    {
      "type": "promotedPurchases",
      "id": "c5eb5306-0c66-eb2f-ee6a-7f4100536144",
      "attributes": {
        "visibleForAllUsers": true,
        "enabled": false,
        "state": "PREPARE_FOR_SUBMISSION"
      },
      "relationships": {
        "promotionImages": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/c5eb5306-0c66-eb2f-ee6a-7f4100536144/relationships/promotionImages",
            "related": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/c5eb5306-0c66-eb2f-ee6a-7f4100536144/promotionImages"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/promotedPurchases/c5eb5306-0c66-eb2f-ee6a-7f4100536144"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/1000001234/promotedPurchases"
  },
  "meta": {
    "paging": {
      "total": 2,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/promotedPurchases`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[inAppPurchases]` ([string]): Additional fields to include for each In-App Purchase resource returned by the response.

  **Allowed Values**: `name`, `productId`, `inAppPurchaseType`, `state`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[promotedPurchases]` ([string]): Additional fields to include for each promoted purchase resource returned by the response.

  **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.

  **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `inAppPurchaseV2`, `subscription`
- `limit` (integer): The maximum number of promoted purchase resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`PromotedPurchasesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting In-App Purchase information
- [Read In-App Purchase information](./get-v1-inapppurchases-_id_.md)
  Get information about an In-App Purchase.
- [List all In-App Purchases for an app v1](./get-v1-apps-_id_-inapppurchases.md)
  List the In-App Purchases that are available for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-promotedpurchases)*
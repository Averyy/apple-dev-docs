# Read In-App Purchase Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an in-app purchase.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [Managing in-app purchases](managing-in-app-purchases.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/inAppPurchases/6446998023
```

**Response**:

```json
{
  "data": [
    {
      "type": "inAppPurchases",
      "id": "6447027998",
      "attributes": {
        "name": "YNC1",
        "productId": "YNCNC1",
        "inAppPurchaseType": "NON_CONSUMABLE",
        "state": "MISSING_METADATA",
        "reviewNote": null,
        "familySharable": false,
        "contentHosting": false,
        "availableInAllTerritories": true
      },
      "relationships": {
        "inAppPurchaseLocalizations": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/inAppPurchaseLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/inAppPurchaseLocalizations"
          }
        },
        "pricePoints": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/pricePoints",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/pricePoints"
          }
        },
        "content": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/content",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/content"
          }
        },
        "appStoreReviewScreenshot": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/appStoreReviewScreenshot",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/appStoreReviewScreenshot"
          }
        },
        "promotedPurchase": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/promotedPurchase",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/promotedPurchase"
          }
        },
        "iapPriceSchedule": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/iapPriceSchedule",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/iapPriceSchedule"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchasesV2"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchases/{id}`

## Parameters

- `fields[inAppPurchases]` ([string])
- `include` ([string])
- `limit[apps]` (integer)

## See Also

- [List All Promoted Purchases for an App](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.
- [List All In-App Purchases for an App V1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchases-_id_)*
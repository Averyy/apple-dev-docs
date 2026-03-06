# List All Promoted Purchases for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
- [Managing in-app purchases](managing-in-app-purchases.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[inAppPurchases]` ([string])
- `fields[promotedPurchases]` ([string])
- `fields[subscriptions]` ([string])
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Promoted Purchases resources to return.

## See Also

- [Read In-App Purchase Information](get-v1-inapppurchases-_id_.md)
  Get information about an in-app purchase.
- [List All In-App Purchases for an App V1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-promotedpurchases)*
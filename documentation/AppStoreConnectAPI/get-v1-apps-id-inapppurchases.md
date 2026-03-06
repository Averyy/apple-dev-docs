# List All In-App Purchases for an App V1

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the in-app purchases that are available for your app.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 2.0 release notes](app-store-connect-api-2-0-release-notes.md)
- [App Store Connect API 2.2 release notes](app-store-connect-api-2-2-release-notes.md)
- [Managing in-app purchases](managing-in-app-purchases.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases
```

**Response**:

```json
{
    "data": [
        {
            "type": "inAppPurchases",
            "id": "ca38ea26-b7d5-4989-9615-c678cb05aabd",
            "attributes": {
                "referenceName": "YNC1",
                "productId": "YNCNC1",
                "inAppPurchaseType": "NON_CONSUMABLE",
                "state": "WAITING_FOR_SCREENSHOT"
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/inAppPurchases/ca38ea26-b7d5-4989-9615-c678cb05aabd"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/inAppPurchases`

## Parameters

- `fields[apps]` ([string])
- `fields[inAppPurchases]` ([string])
- `filter[canBeSubmitted]` ([string])
- `filter[inAppPurchaseType]` ([string])
- `include` ([string])
- `limit` (integer)
- `sort` ([string])
- `limit[apps]` (integer)

## See Also

- [Read In-App Purchase Information](get-v1-inapppurchases-_id_.md)
  Get information about an in-app purchase.
- [List All Promoted Purchases for an App](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-inapppurchases)*
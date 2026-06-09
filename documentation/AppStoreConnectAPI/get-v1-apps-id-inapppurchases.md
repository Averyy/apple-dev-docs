# List all in-app purchases for an app v1

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

- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[inAppPurchases]` ([string]): Additional fields to include for each in-app purchase resource returned by the response.
- `filter[canBeSubmitted]` ([string]): Filter the returned in-app purchases by whether they can be submitted.
- `filter[inAppPurchaseType]` ([string]): Filter the returned in-app purchases by in-app purchase type.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of in-app purchase resources to return.
- `sort` ([string]): Attributes by which to sort.
- `limit[apps]` (integer): The maximum number of related apps resources to return.

## See Also

- [Read in-app purchase information](get-v1-inapppurchases-_id_.md)
  Get information about an in-app purchase.
- [List all promoted purchases for an app](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-inapppurchases)*
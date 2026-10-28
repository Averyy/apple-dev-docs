# Read information about the availability of an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the territory availablity for an In-App Purchase.

**Availability**:
- App Store Connect API 2.4+

## Mentions

- [App Store Connect API 2.4 release notes](./app-store-connect-api-2-4-release-notes.md)

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v2/inAppPurchases/6448262365/inAppPurchaseAvailability
```

**Response**:

```json
{
  “data”: {
    “type”: “inAppPurchaseAvailabilities”,
    “id”: “6448262365”,
    “attributes”: {
      “availableInNewTerritories”: true
    },
    “relationships”: {
      “availableTerritories”: {
        “links”: {
          “self”: “https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6448262365/relationships/availableTerritories”,
          “related”: “https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6448262365/availableTerritories”
        }
      }
    },
    “links”: {
      “self”: “https://api.appstoreconnect.apple.com/v1/inAppPurchaseAvailabilities/6448262365”
    }
  },
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v2/inAppPurchases/6448262365/inAppPurchaseAvailability”
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}/inAppPurchaseAvailability`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the In-App Purchase resource ID from the [`List all In-App Purchases for an app`](./get-v1-apps-_id_-inapppurchasesv2.md) response.

### Query Parameters

- `fields[inAppPurchaseAvailabilities]` ([string]): **Allowed Values**: `availableInNewTerritories`, `availableTerritories`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `include` ([string]): **Allowed Values**: `availableTerritories`
- `limit[availableTerritories]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`InAppPurchaseAvailabilityResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an In-App Purchase](./post-v2-inapppurchases.md)
  Create an In-App Purchase, including a consumable, non-consumable, or non-renewing subscription.
- [Read In-App Purchase information](./get-v2-inapppurchases-_id_.md)
  Get information about a specific In-App Purchase.
- [List all In-App Purchases for an app](./get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the In-App Purchases for a specific app.
- [Modify an In-App Purchase](./patch-v2-inapppurchases-_id_.md)
  Update the reference name of a specific In-App Purchase.
- [Delete an In-App Purchase](./delete-v2-inapppurchases-_id_.md)
  Delete a specific In-App Purchase from your app.
- [List all price points for an In-App Purchase](./get-v2-inapppurchases-_id_-pricepoints.md)
  Get a list of possible price points for an In-App Purchase.
- [List price point IDs for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-pricepoints.md)
  Get a list of price point IDs for a specific In-App Purchase.
- [List All In-App Purchase Price Point Equalizations](./get-v1-inapppurchasepricepoints-_id_-equalizations.md)
  Get a list of In-App Purchase price points and their equivalent in a specified currency.
- [List equalization IDs for an In-App Purchase price point](./get-v1-inapppurchasepricepoints-_id_-relationships-equalizations.md)
- [Read promoted purchase information for an In-App Purchase](./get-v2-inapppurchases-_id_-promotedpurchase.md)
  Get details about the promoted purchase of an In-App Purchase.
- [Read the promoted purchase ID for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-promotedpurchase.md)
  Get the promoted purchase ID for a specific In-App Purchase.
- [List all localizations for an In-App Purchase](./get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific In-App Purchase.
- [List localization IDs for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-inapppurchaselocalizations.md)
  Get a list of localization IDs for a specific In-App Purchase.
- [Read review screenshot information for an In-App Purchase](./get-v2-inapppurchases-_id_-appstorereviewscreenshot.md)
  Get information about a review screenshot for a specific In-App Purchase.
- [Read the App Store review screenshot ID for an In-App Purchase](./get-v2-inapppurchases-_id_-relationships-appstorereviewscreenshot.md)
  Get the App Store review screenshot ID for a specific In-App Purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_-inapppurchaseavailability)*
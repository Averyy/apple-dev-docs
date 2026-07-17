# List in-app purchases ids for an app v1

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all in-app purchases IDs for a specific app V1.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/inAppPurchases`

## Parameters

- `limit` (integer): The maximum number of in-app purchase resource identifiers to return.

## See Also

- [List all in-app purchases for an app](get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the in-app purchases for a specific app.
- [GET /v1/apps/{id}/relationships/inAppPurchasesV2](get-v1-apps-_id_-relationships-inapppurchasesv2.md)
- [List all in-app purchases for an app v1](get-v1-apps-_id_-inapppurchases.md)
  List the in-app purchases that are available for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-inapppurchases)*
# Read in-app purchase image information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the metadata for an in-app purchase image configured with the v2 API, including the asset upload state.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [Working with in-app purchase versions](working-with-in-app-purchase-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchaseImages/{id}`

## Parameters

- `fields[inAppPurchaseImages]` ([string])

## See Also

- [Create an in-app purchase image](post-v2-inapppurchaseimages.md)
  Reserve a promotion image for an in-app purchase configured with the v2 API and prepare its asset upload.
- [Modify an in-app purchase image](patch-v2-inapppurchaseimages-_id_.md)
  Commit the asset upload for an in-app purchase image configured with the v2 API.
- [Delete an in-app purchase image](delete-v2-inapppurchaseimages-_id_.md)
  Delete an in-app purchase image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchaseimages-_id_)*
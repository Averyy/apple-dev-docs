# Modify an in-app purchase image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit the asset upload for an in-app purchase image configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Working with in-app purchase versions](working-with-in-app-purchase-versions.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/inAppPurchaseImages/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create an in-app purchase image](post-v2-inapppurchaseimages.md)
  Reserve a promotion image for an in-app purchase configured with the v2 API and prepare its asset upload.
- [Read in-app purchase image information](get-v2-inapppurchaseimages-_id_.md)
  Get the metadata for an in-app purchase image configured with the v2 API, including the asset upload state.
- [Delete an in-app purchase image](delete-v2-inapppurchaseimages-_id_.md)
  Delete an in-app purchase image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-inapppurchaseimages-_id_)*
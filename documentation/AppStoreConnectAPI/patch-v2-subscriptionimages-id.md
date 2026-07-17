# Modify a subscription image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit the asset upload for a subscription image configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Working with subscription versions](working-with-subscription-versions.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/subscriptionImages/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a subscription image](post-v2-subscriptionimages.md)
  Reserve a promotion image for an auto-renewable subscription configured with the v2 API and prepare its asset upload.
- [Read subscription image information](get-v2-subscriptionimages-_id_.md)
  Get the metadata for a subscription image configured with the v2 API, including the asset upload state.
- [Delete a subscription image](delete-v2-subscriptionimages-_id_.md)
  Delete a subscription image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-subscriptionimages-_id_)*
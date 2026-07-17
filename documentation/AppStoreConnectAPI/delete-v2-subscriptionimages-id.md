# Delete a subscription image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a subscription image configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
- [Working with subscription versions](working-with-subscription-versions.md)

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v2/subscriptionImages/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a subscription image](post-v2-subscriptionimages.md)
  Reserve a promotion image for an auto-renewable subscription configured with the v2 API and prepare its asset upload.
- [Read subscription image information](get-v2-subscriptionimages-_id_.md)
  Get the metadata for a subscription image configured with the v2 API, including the asset upload state.
- [Modify a subscription image](patch-v2-subscriptionimages-_id_.md)
  Commit the asset upload for a subscription image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v2-subscriptionimages-_id_)*
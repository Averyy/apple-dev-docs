# Read subscription image information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the metadata for a subscription image configured with the v2 API, including the asset upload state.

**Availability**:
- App Store Connect API 4.4.1+

## Mentions

- [Working with subscription versions](working-with-subscription-versions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/subscriptionImages/{id}`

## Parameters

- `fields[subscriptionImages]` ([string])

## See Also

- [Create a subscription image](post-v2-subscriptionimages.md)
  Reserve a promotion image for an auto-renewable subscription configured with the v2 API and prepare its asset upload.
- [Modify a subscription image](patch-v2-subscriptionimages-_id_.md)
  Commit the asset upload for a subscription image configured with the v2 API.
- [Delete a subscription image](delete-v2-subscriptionimages-_id_.md)
  Delete a subscription image configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-subscriptionimages-_id_)*
# Modify App Store Review Details for an App Clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update App Clip metadata you provide to App Store Review.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the App Store Versions resource.

## Request Body

The request body you use to update the App Store review details of an App Clip.

## See Also

- [Read the App Store Review Details of an App Clip](get-v1-appclipappstorereviewdetails-_id_.md)
  Get App Store Review details for an App Clip.
- [Create App Store Review Details for an App Clip](post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipappstorereviewdetails-_id_)*
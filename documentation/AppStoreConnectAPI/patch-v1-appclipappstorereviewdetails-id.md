# Modify app store review details for an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update App Clip metadata you provide to App Store Review.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip App Store review detail resource ID from the [`Read the app store review detail for a default app clip experience`](get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md) response.

## Request Body

The request body you use to update the App Store review details of an App Clip.

## See Also

- [Read the app store review details of an app clip](get-v1-appclipappstorereviewdetails-_id_.md)
  Get App Store Review details for an App Clip.
- [Create app store review details for an app clip](post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipappstorereviewdetails-_id_)*
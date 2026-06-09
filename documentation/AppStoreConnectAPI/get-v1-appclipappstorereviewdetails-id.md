# Read the app store review details of an app clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get App Store Review details for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each app clip App Store review detail resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appClipDefaultExperiences]` ([string])

## See Also

- [Create app store review details for an app clip](post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.
- [Modify app store review details for an app clip](patch-v1-appclipappstorereviewdetails-_id_.md)
  Update App Clip metadata you provide to App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipappstorereviewdetails-_id_)*
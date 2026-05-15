# Read the App Store Review Details of an App Clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get App Store Review details for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAppStoreReviewDetails/{id}`

## Parameters

- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each App Clip App Store Review Details resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appClipDefaultExperiences]` ([string])

## See Also

- [Create App Store Review Details for an App Clip](post-v1-appclipappstorereviewdetails.md)
  Provide App Clip metadata required by App Store Review.
- [Modify App Store Review Details for an App Clip](patch-v1-appclipappstorereviewdetails-_id_.md)
  Update App Clip metadata you provide to App Store Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipappstorereviewdetails-_id_)*
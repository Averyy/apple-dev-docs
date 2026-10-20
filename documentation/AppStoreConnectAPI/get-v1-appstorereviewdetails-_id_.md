# Read app store review detail information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get App Review details you provided, including contact information, demo account, and notes.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreReviewDetails/{id}`

## Parameters

- `fields[appStoreReviewDetails]` ([string]): Additional fields to include for each App Store review detail resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appStoreReviewAttachments]` (integer): The maximum number of related App Store review attachments resources to return.
- `fields[appStoreReviewAttachments]` ([string]): Additional fields to include for each App Store review attachment resource returned by the response.
- `fields[appStoreVersions]` ([string])

## See Also

- [Create an app store review detail](post-v1-appstorereviewdetails.md)
  Add App Store review details to an App Store version, including contact and demo account information.
- [List App Store review attachment IDs for an App Store review detail](get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)
- [Modify an app store review detail](patch-v1-appstorereviewdetails-_id_.md)
  Update the App Store review details, including the contact information, demo account, and notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstorereviewdetails-_id_)*
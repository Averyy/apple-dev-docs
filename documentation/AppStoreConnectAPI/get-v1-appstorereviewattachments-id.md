# Read app store review attachment information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an App Store review attachment and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreReviewAttachments/{id}`

## Parameters

- `fields[appStoreReviewAttachments]` ([string]): Additional fields to include for each App Store review attachment resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appStoreReviewDetails]` ([string])

## See Also

- [List all review attachments for an app store review detail](get-v1-appstorereviewdetails-_id_-appstorereviewattachments.md)
  List all the App Store review attachments you include with a version when you submit it for App Review.
- [List App Store review attachment IDs for an App Store review detail](get-v1-appstorereviewdetails-_id_-relationships-appstorereviewattachments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstorereviewattachments-_id_)*
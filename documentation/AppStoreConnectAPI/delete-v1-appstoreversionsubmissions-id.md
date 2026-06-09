# Delete an app store version submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a version from App Store review.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 1.7 release notes](app-store-connect-api-1-7-release-notes.md)

#### Discussion

Use this endpoint to remove a version from App Review. This request fails with an appropriate error if the app can’t be removed from review. For more information, see [`Remove a submission from review`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/remove-a-submission-from-review).

##### Remove a Version From App Review

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionSubmissions/942c7a69-b184-478a-898f-a51b8be1044d
```

**Response**:

```json
HTTP/1.1 204 NO CONTENT
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionSubmissions/{id}`

## Parameters

- `id` (string) *(required)*: The unique identifier of the App Store version submission resource that you receive when you create the submission. This value is the same as the `id` property in the [`AppStoreVersionSubmission`](appstoreversionsubmission.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionsubmissions-_id_)*
# Delete an app store version submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a version from App Store review.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 1.7

> **Deprecated**: Use [`Modify a Review Submission`](./patch-v1-reviewsubmissions-_id_.md) instead.

## Mentions

- [App Store Connect API 1.7 release notes](./app-store-connect-api-1-7-release-notes.md)

#### Discussion

Use this endpoint to remove a version from App Review. This request fails with an appropriate error if the app can’t be removed from review. For more information, see [Remove a submission from review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/remove-a-submission-from-review).

##### Remove a Version from App Review

**Request**:

```
DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionSubmissions/942c7a69-b184-478a-898f-a51b8be1044d
```

**Response**:

```json
HTTP/1.1 204 NO CONTENT
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionSubmissions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier of the App Store version submission resource that you receive when you create the submission. This value is the same as the `id` property in the [`AppStoreVersionSubmission`](./appstoreversionsubmission.md) object.

## Responses

- `204` No Content: Success.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionsubmissions-_id_)*
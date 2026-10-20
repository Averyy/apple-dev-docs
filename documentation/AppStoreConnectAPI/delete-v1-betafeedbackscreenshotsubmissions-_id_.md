# Delete a Beta Feedback Screenshot Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a beta feedback screenshot submission from your app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaFeedbackScreenshotSubmissions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackScreenshotSubmissions` resource ID from the [`List All Beta Feedback Screenshot Submissions for an App`](./get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and deleting beta feedback screenshot submissions
- [List All Beta Feedback Screenshot Submissions for an App](./get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
- [List all beta feedback screenshot submission ids for an app](./get-v1-apps-_id_-relationships-betafeedbackscreenshotsubmissions.md)
  Get a list of beta feedback screenshot submissions for a specific app.
- [Read a Beta Feedback Screenshot Submission](./get-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Get information for a specific beta feedback screenshot submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betafeedbackscreenshotsubmissions-_id_)*
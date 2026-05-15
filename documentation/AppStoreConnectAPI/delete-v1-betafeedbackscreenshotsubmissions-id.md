# Delete a Beta Feedback Screenshot Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a beta feedback screenshot submission from your app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaFeedbackScreenshotSubmissions/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackScreenshotSubmissions` resource ID from the [`List All Beta Feedback Screenshot Submissions for an App`](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md) response.

## See Also

- [List All Beta Feedback Screenshot Submissions for an App](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
- [List All Beta Feedback Screenshot Submission IDs for an App](get-v1-apps-_id_-relationships-betafeedbackscreenshotsubmissions.md)
  Get a list of beta feedback screenshot submissions for a specific app.
- [Read a Beta Feedback Screenshot Submission](get-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Get information for a specific beta feedback screenshot submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betafeedbackscreenshotsubmissions-_id_)*
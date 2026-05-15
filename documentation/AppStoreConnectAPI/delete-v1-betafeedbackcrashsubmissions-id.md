# Delete a Beta Feedback Crash Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a beta feedback crash submission from your app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaFeedbackCrashSubmissions/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackCrashSubmissions` resource ID from the [`List All Beta Feedback Crash Submissions for an App`](get-v1-apps-_id_-betafeedbackcrashsubmissions.md) response.

## See Also

- [List All Beta Feedback Crash Submissions for an App](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List All Beta Feedback Crash Submission IDs for an App](get-v1-apps-_id_-relationships-betafeedbackcrashsubmissions.md)
  Get a list of beta feedback crash submissions for a specific app.
- [Read Beta Feedback Crash Submission Information](get-v1-betafeedbackcrashsubmissions-_id_.md)
  Get information for a specific beta feedback crash submission.
- [Read the Crash Log for a Beta Feedback Crash Submission](get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md)
  Get crash log information for a specific beta feedback crash submission.
- [GET /v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog](get-v1-betafeedbackcrashsubmissions-_id_-relationships-crashlog.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betafeedbackcrashsubmissions-_id_)*
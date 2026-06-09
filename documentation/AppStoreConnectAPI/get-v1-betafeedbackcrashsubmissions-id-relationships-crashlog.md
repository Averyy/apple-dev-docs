# Get the crash log ID for a beta feedback crash submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaFeedbackCrashSubmissions` resource ID from the [`List All Beta Feedback Crash Submissions for an App`](get-v1-apps-_id_-betafeedbackcrashsubmissions.md) response.

## See Also

- [List All Beta Feedback Crash Submissions for an App](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List all beta feedback crash submission ids for an app](get-v1-apps-_id_-relationships-betafeedbackcrashsubmissions.md)
  Get a list of beta feedback crash submissions for a specific app.
- [Read Beta Feedback Crash Submission Information](get-v1-betafeedbackcrashsubmissions-_id_.md)
  Get information for a specific beta feedback crash submission.
- [Read the Crash Log for a Beta Feedback Crash Submission](get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md)
  Get crash log information for a specific beta feedback crash submission.
- [Delete a Beta Feedback Crash Submission](delete-v1-betafeedbackcrashsubmissions-_id_.md)
  Delete a beta feedback crash submission from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betafeedbackcrashsubmissions-_id_-relationships-crashlog)*
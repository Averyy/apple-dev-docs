# List All Beta Feedback Crash Submission IDs for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of beta feedback crash submissions for a specific app.

**Availability**:
- App Store Connect API 4.0+

#### Overview

- id: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List Apps`](get-v1-apps.md) response.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/betaFeedbackCrashSubmissions`

## Parameters

- `limit` (integer)

## See Also

- [List All Beta Feedback Crash Submissions for an App](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [Read Beta Feedback Crash Submission Information](get-v1-betafeedbackcrashsubmissions-_id_.md)
  Get information for a specific beta feedback crash submission.
- [Read the Crash Log for a Beta Feedback Crash Submission](get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md)
  Get crash log information for a specific beta feedback crash submission.
- [GET /v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog](get-v1-betafeedbackcrashsubmissions-_id_-relationships-crashlog.md)
- [Delete a Beta Feedback Crash Submission](delete-v1-betafeedbackcrashsubmissions-_id_.md)
  Delete a beta feedback crash submission from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-betafeedbackcrashsubmissions)*
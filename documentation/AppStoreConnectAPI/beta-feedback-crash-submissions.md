# Beta feedback crash submissions

**Framework**: App Store Connect API

Get TestFlight feedback crashes from beta testers for your apps.

#### Overview

Use this API to read details about crashes submitted by testers while testing your beta app builds. There are many filters available for these endpoints to help you identify patterns and isolate issues.

You can get new beta feedback crash submissions in two ways:

- Make active `GET` request to look up new beta feedback crash submissions.
- Set up a webhook to get a notification when there is new beta feedback crash submissions. Then look up the corresponding feedback. To learn more, see [`Webhook notifications`](webhook-notifications.md).

To manage beta feedback crash submissions, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `DEVELOPER`

Both Team and Individual keys can use these endpoints with the correct role.

## Topics

### Reading and deleting beta feedback crash submissions
- [List all beta feedback crash submissions for an app](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.
- [List all beta feedback crash submission IDs for an app](get-v1-apps-_id_-relationships-betafeedbackcrashsubmissions.md)
  Get a list of beta feedback crash submissions for a specific app.
- [Read beta feedback crash submission information](get-v1-betafeedbackcrashsubmissions-_id_.md)
  Get information for a specific beta feedback crash submission.
- [Read the crash log for a beta feedback crash submission](get-v1-betafeedbackcrashsubmissions-_id_-crashlog.md)
  Get crash log information for a specific beta feedback crash submission.
- [GET /v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog](get-v1-betafeedbackcrashsubmissions-_id_-relationships-crashlog.md)
- [Delete a beta feedback crash submission](delete-v1-betafeedbackcrashsubmissions-_id_.md)
  Delete a beta feedback crash submission from your app.
### Read beta crash logs
- [Read beta crash log information](get-v1-betacrashlogs-_id_.md)
  Get crash log details for a specific beta feedback crash submission.
### Objects
- [object BetaCrashLog](betacrashlog.md)
- [object BetaCrashLogResponse](betacrashlogresponse.md)
  A response that contains a single beta crash log response resource.
- [object BetaFeedbackCrashSubmission](betafeedbackcrashsubmission.md)
  The data structure that represents a `BetaFeedbackCrashSubmission` resource.
- [object BetaFeedbackCrashSubmissionResponse](betafeedbackcrashsubmissionresponse.md)
  A response that contains a single `BetaFeedbackCrashSubmissionResponse` resource.
- [object BetaFeedbackCrashSubmissionsResponse](betafeedbackcrashsubmissionsresponse.md)
  A response that contains a list of `BetaFeedbackCrashSubmissionsResponse` resources.
- [object BetaFeedbackCrashSubmissionCrashLogLinkageResponse](betafeedbackcrashsubmissioncrashloglinkageresponse.md)
  A response that contains a single beta feedback crash submission crash log linkage response resource.

## See Also

- [Beta feedback screenshot submissions](beta-feedback-screenshot-submissions.md)
  Get Testflight feedback screenshots from beta testers for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-feedback-crash-submissions)*
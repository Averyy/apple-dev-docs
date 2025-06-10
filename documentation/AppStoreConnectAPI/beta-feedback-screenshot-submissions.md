# Beta feedback screenshot submissions

**Framework**: App Store Connect API

Get Testflight feedback screenshots from beta testers for your apps.

#### Overview

Use this API to read details about screenshots submitted by testers while testing your beta app builds. There are many filters available for these endpoints to help you identify patterns and isolate issues.

You can get new beta feedback screenshot submissions in two ways:

- Make an active `GET` request to look up new beta feedback screenshot submissions.
- Set up a webhook to get a notification when there is a new beta feedback screenshot submission. Then look up the corresponding feedback. For more information about these notifications, see [`Webhook notifications`](webhook-notifications.md).

To manage beta feedback screenshot submissions, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `DEVELOPER`

Both Team and Individual keys can use these endpoints with the correct role.

## Topics

### Reading and deleting beta feedback screenshot submissions
- [List all beta feedback screenshot submissions for an app](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
- [List all beta feedback screenshot submission IDs for an app](get-v1-apps-_id_-relationships-betafeedbackscreenshotsubmissions.md)
  Get a list of beta feedback screenshot submissions for a specific app.
- [Read a beta feedback screenshot submission](get-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Get information for a specific beta feedback screenshot submission.
- [Delete a beta feedback screenshot submission](delete-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Delete a beta feedback screenshot submission from your app.
### Objects
- [object BetaFeedbackScreenshotSubmission](betafeedbackscreenshotsubmission.md)
  The data structure that represents a `BetaFeedbackScreenshotSubmission` resource.
- [object BetaFeedbackScreenshotSubmissionResponse](betafeedbackscreenshotsubmissionresponse.md)
  A response that contains a single `BetaFeedbackScreenshotSubmission` resource.
- [object BetaFeedbackScreenshotSubmissionsResponse](betafeedbackscreenshotsubmissionsresponse.md)
- [object BetaFeedbackScreenshotImage](betafeedbackscreenshotimage.md)

## See Also

- [Beta feedback crash submissions](beta-feedback-crash-submissions.md)
  Get TestFlight feedback crashes from beta testers for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-feedback-screenshot-submissions)*
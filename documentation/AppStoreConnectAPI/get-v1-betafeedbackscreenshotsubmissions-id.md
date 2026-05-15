# Read a Beta Feedback Screenshot Submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific beta feedback screenshot submission.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaFeedbackScreenshotSubmissions/{id}`

## Parameters

- `fields[betaFeedbackScreenshotSubmissions]` ([string])
- `include` ([string])
- `fields[betaTesters]` ([string])
- `fields[builds]` ([string])

## See Also

- [List All Beta Feedback Screenshot Submissions for an App](get-v1-apps-_id_-betafeedbackscreenshotsubmissions.md)
  Get beta feedback screenshot submissions for a specific app.
- [List All Beta Feedback Screenshot Submission IDs for an App](get-v1-apps-_id_-relationships-betafeedbackscreenshotsubmissions.md)
  Get a list of beta feedback screenshot submissions for a specific app.
- [Delete a Beta Feedback Screenshot Submission](delete-v1-betafeedbackscreenshotsubmissions-_id_.md)
  Delete a beta feedback screenshot submission from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betafeedbackscreenshotsubmissions-_id_)*
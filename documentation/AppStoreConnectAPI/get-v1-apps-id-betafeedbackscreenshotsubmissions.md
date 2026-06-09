# List All Beta Feedback Screenshot Submissions for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get beta feedback screenshot submissions for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaFeedbackScreenshotSubmissions`

## Parameters

- `fields[betaFeedbackScreenshotSubmissions]` ([string]): Additional fields to include for each beta feedback screenshot submission resource returned by the response.
- `fields[betaTesters]` ([string]): Additional fields to include for each beta tester resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.
- `filter[appPlatform]` ([string]): Filter the returned beta feedback screenshot submissions by app platform.
- `filter[build.preReleaseVersion]` ([string]): Filter the returned beta feedback screenshot submissions by build pre-release version.
- `filter[build]` ([string]): Filter the returned beta feedback screenshot submissions by build.
- `filter[deviceModel]` ([string]): Filter the returned beta feedback screenshot submissions by device model.
- `filter[devicePlatform]` ([string]): Filter the returned beta feedback screenshot submissions by device platform.
- `filter[osVersion]` ([string]): Filter the returned beta feedback screenshot submissions by OS version.
- `filter[tester]` ([string]): Filter the returned beta feedback screenshot submissions by tester.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of beta feedback screenshot submission resources to return.
- `sort` ([string]): Attributes by which to sort.

## See Also

- [List All Beta Feedback Crash Submissions for an App](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betafeedbackscreenshotsubmissions)*
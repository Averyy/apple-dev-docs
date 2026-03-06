# List all beta feedback screenshot submissions for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get beta feedback screenshot submissions for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/betaFeedbackScreenshotSubmissions`

## Parameters

- `fields[betaFeedbackScreenshotSubmissions]` ([string])
- `fields[betaTesters]` ([string])
- `fields[builds]` ([string])
- `filter[appPlatform]` ([string])
- `filter[build.preReleaseVersion]` ([string])
- `filter[build]` ([string])
- `filter[deviceModel]` ([string])
- `filter[devicePlatform]` ([string])
- `filter[osVersion]` ([string])
- `filter[tester]` ([string])
- `include` ([string])
- `limit` (integer)
- `sort` ([string])

## See Also

- [List all beta feedback crash submissions for an app](get-v1-apps-_id_-betafeedbackcrashsubmissions.md)
  Get the beta feedback crash submissions for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-betafeedbackscreenshotsubmissions)*
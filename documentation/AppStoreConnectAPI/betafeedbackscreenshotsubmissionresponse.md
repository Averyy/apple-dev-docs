# BetaFeedbackScreenshotSubmissionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single screenshot and feedback note submitted by a TestFlight beta tester.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object BetaFeedbackScreenshotSubmissionResponse
```

## Properties

- `data` (BetaFeedbackScreenshotSubmission) *(required)*
- `included` ([*]): **Allowed Types**: `BetaTester`, `Build`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object BetaFeedbackScreenshotSubmission](./betafeedbackscreenshotsubmission.md)
  A screenshot and feedback note submitted by a TestFlight beta tester while testing a specific build.
- [object BetaFeedbackScreenshotSubmissionsResponse](./betafeedbackscreenshotsubmissionsresponse.md)
- [object BetaFeedbackScreenshotImage](./betafeedbackscreenshotimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betafeedbackscreenshotsubmissionresponse)*
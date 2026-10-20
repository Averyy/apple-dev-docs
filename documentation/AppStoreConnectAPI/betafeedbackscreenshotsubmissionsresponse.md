# BetaFeedbackScreenshotSubmissionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object BetaFeedbackScreenshotSubmissionsResponse
```

## Properties

- `data` ([BetaFeedbackScreenshotSubmission]) *(required)*
- `included` ([*]): **Allowed Types**: `BetaTester`, `Build`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object BetaFeedbackScreenshotSubmission](./betafeedbackscreenshotsubmission.md)
  A screenshot and feedback note submitted by a TestFlight beta tester while testing a specific build.
- [object BetaFeedbackScreenshotSubmissionResponse](./betafeedbackscreenshotsubmissionresponse.md)
  A response containing a single screenshot and feedback note submitted by a TestFlight beta tester.
- [object BetaFeedbackScreenshotImage](./betafeedbackscreenshotimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betafeedbackscreenshotsubmissionsresponse)*
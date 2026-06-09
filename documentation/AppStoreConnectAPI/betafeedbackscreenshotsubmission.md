# BetaFeedbackScreenshotSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A screenshot and feedback note submitted by a TestFlight beta tester while testing a specific build.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object BetaFeedbackScreenshotSubmission
```

## Topics

### Dictionaries
- [object BetaFeedbackScreenshotSubmission.Attributes](betafeedbackscreenshotsubmission/attributes-data.dictionary.md)
  Attributes that describe a `BetaFeedbackScreenshotSubmission` resource.
- [object BetaFeedbackScreenshotSubmission.Relationships](betafeedbackscreenshotsubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaFeedbackScreenshotSubmission.Attributes): Attributes that describe a `BetaFeedbackScreenshotSubmission` resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (BetaFeedbackScreenshotSubmission.Relationships)
- `type` (string) *(required)*: The resource type.

## See Also

- [object BetaFeedbackScreenshotSubmissionResponse](betafeedbackscreenshotsubmissionresponse.md)
  A response containing a single screenshot and feedback note submitted by a TestFlight beta tester.
- [object BetaFeedbackScreenshotSubmissionsResponse](betafeedbackscreenshotsubmissionsresponse.md)
- [object BetaFeedbackScreenshotImage](betafeedbackscreenshotimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betafeedbackscreenshotsubmission)*
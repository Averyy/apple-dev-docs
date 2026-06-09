# BetaAppReviewSubmissionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that submit a build for beta app review.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewSubmissionResponse
```

## Properties

- `data` (BetaAppReviewSubmission) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([Build])

## See Also

- [Submit an app for beta review](post-v1-betaappreviewsubmissions.md)
  Submit an app for beta app review to allow external testing.
- [object BetaAppReviewSubmission](betaappreviewsubmission.md)
  A submission of a build to Apple’s beta app review process, required before external testing.
- [object BetaAppReviewSubmissionCreateRequest](betaappreviewsubmissioncreaterequest.md)
  The request body you use to create a Beta App Review Submission.
- [object BetaAppReviewSubmissionWithoutIncludesResponse](betaappreviewsubmissionwithoutincludesresponse.md)
  A response containing a single beta app review submission, without related resources.
- [object BetaAppReviewSubmissionsResponse](betaappreviewsubmissionsresponse.md)
  The response body for endpoints that list beta app review submissions.
- [type BetaReviewState](betareviewstate.md)
  String that indicates the review state of a beta app.
- [object BetaAppReviewSubmissionBuildLinkageResponse](betaappreviewsubmissionbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewsubmissionresponse)*
# BetaAppReviewSubmissionCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Beta App Review Submission.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewSubmissionCreateRequest
```

## Topics

### Objects
- [object BetaAppReviewSubmissionCreateRequest.Data](betaappreviewsubmissioncreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (BetaAppReviewSubmissionCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object BetaAppReviewSubmission](betaappreviewsubmission.md)
  A submission of a build to Apple’s beta app review process, required before external testing.
- [object BetaAppReviewSubmissionResponse](betaappreviewsubmissionresponse.md)
  The response body for endpoints that submit a build for beta app review.
- [object BetaAppReviewSubmissionWithoutIncludesResponse](betaappreviewsubmissionwithoutincludesresponse.md)
  A response containing a single beta app review submission, without related resources.
- [object BetaAppReviewSubmissionsResponse](betaappreviewsubmissionsresponse.md)
  The response body for endpoints that list beta app review submissions.
- [type BetaReviewState](betareviewstate.md)
  String that indicates the review state of a beta app.
- [object BetaAppReviewSubmissionBuildLinkageResponse](betaappreviewsubmissionbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewsubmissioncreaterequest)*
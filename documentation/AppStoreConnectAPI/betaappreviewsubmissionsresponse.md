# BetaAppReviewSubmissionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list beta app review submissions.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewSubmissionsResponse
```

## Properties

- `data` ([BetaAppReviewSubmission]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([Build])

## See Also

- [List beta app review submissions](get-v1-betaappreviewsubmissions.md)
  Find and list beta app review submissions for all builds.
- [object BetaAppReviewSubmission](betaappreviewsubmission.md)
  A submission of a build to Apple’s beta app review process, required before external testing.
- [object BetaAppReviewSubmissionCreateRequest](betaappreviewsubmissioncreaterequest.md)
  The request body you use to create a Beta App Review Submission.
- [object BetaAppReviewSubmissionResponse](betaappreviewsubmissionresponse.md)
  The response body for endpoints that submit a build for beta app review.
- [object BetaAppReviewSubmissionWithoutIncludesResponse](betaappreviewsubmissionwithoutincludesresponse.md)
  A response containing a single beta app review submission, without related resources.
- [type BetaReviewState](betareviewstate.md)
  String that indicates the review state of a beta app.
- [object BetaAppReviewSubmissionBuildLinkageResponse](betaappreviewsubmissionbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewsubmissionsresponse)*
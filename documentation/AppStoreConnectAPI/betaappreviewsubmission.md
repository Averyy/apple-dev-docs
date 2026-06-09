# BetaAppReviewSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A submission of a build to Apple’s beta app review process, required before external testing.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewSubmission
```

## Topics

### Objects
- [object BetaAppReviewSubmission.Attributes](betaappreviewsubmission/attributes-data.dictionary.md)
  Attributes that describe a Beta App Review Submissions resource.
- [object BetaAppReviewSubmission.Relationships](betaappreviewsubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaAppReviewSubmission.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (BetaAppReviewSubmission.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BetaAppReviewSubmissionCreateRequest](betaappreviewsubmissioncreaterequest.md)
  The request body you use to create a Beta App Review Submission.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewsubmission)*
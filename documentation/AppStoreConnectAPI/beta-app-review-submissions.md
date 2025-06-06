# Beta App Review Submissions

**Framework**: App Store Connect API

The submissions of builds for beta app review, including the status of submissions.

#### Overview

A `betaAppReviewSubmissions` resource represents Apple’s review of a build before its distribution through TestFlight. Create a beta app review submission when you are ready to submit a build. App Store Connect validates the beta app review submission to ensure it includes necessary information such as `appEncryptionDeclarations`, `betaAppReviewDetails`, and so on, and submits the build to the review team.

API users can get the `betaAppReviewSubmissions` to see if the build has been accepted or rejected.

## Topics

### Submitting an App for Beta Review
- [Submit an App for Beta Review](post-v1-betaappreviewsubmissions.md)
  Submit an app for beta app review to allow external testing.
### Getting Beta App Review Submissions Info
- [List Beta App Review Submissions](get-v1-betaappreviewsubmissions.md)
  Find and list beta app review submissions for all builds.
- [Read Beta App Review Submission Information](get-v1-betaappreviewsubmissions-_id_.md)
  Get a specific beta app review submission.
### Getting Build Information
- [Read the Build Information of a Beta App Review Submission](get-v1-betaappreviewsubmissions-_id_-build.md)
  Get the build information for a specific beta app review submission.
### Objects and Data Types
- [object BetaAppReviewSubmission](betaappreviewsubmission.md)
  The data structure that represents a Beta App Review Submissions resource.
- [object BetaAppReviewSubmissionCreateRequest](betaappreviewsubmissioncreaterequest.md)
  The request body you use to create a Beta App Review Submission.
- [object BetaAppReviewSubmissionResponse](betaappreviewsubmissionresponse.md)
  A response that contains a single Beta App Review Submissions resource.
- [object BetaAppReviewSubmissionWithoutIncludesResponse](betaappreviewsubmissionwithoutincludesresponse.md)
- [object BetaAppReviewSubmissionsResponse](betaappreviewsubmissionsresponse.md)
  A response that contains a list of Beta App Review Submission resources.
- [type BetaReviewState](betareviewstate.md)
  String that indicates the review state of a beta app.

## See Also

- [Beta App Review Detail](beta-app-review-detail.md)
  Information about your app required for beta app review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-review-submissions)*
# Beta App Review Detail

**Framework**: App Store Connect API

Information about your app required for beta app review.

#### Overview

Before an app can be distributed to external testers, it must be reviewed by Apple. A `betaAppReviewDetails` resource contains the information Apple requires when you submit a build for review, including a demo account login and contact details in case the reviewer has questions.

## Topics

### Getting Beta App Review Details
- [List beta app review details](get-v1-betaappreviewdetails.md)
  Find and list beta app review details for all apps.
- [Read beta app review detail information](get-v1-betaappreviewdetails-_id_.md)
  Get beta app review details for a specific app.
- [Read the app information of a beta app review detail](get-v1-betaappreviewdetails-_id_-app.md)
  Get the app information for a specific beta app review details resource.
- [Get the app ID for a beta app review detail](get-v1-betaappreviewdetails-_id_-relationships-app.md)
### Modifying Beta App Review Details
- [Modify a beta app review detail](patch-v1-betaappreviewdetails-_id_.md)
  Update the details for a specific app’s beta app review.
### Objects
- [object BetaAppReviewDetail](betaappreviewdetail.md)
  Contact information and demo credentials provided to App Store reviewers for beta app review.
- [object BetaAppReviewDetailUpdateRequest](betaappreviewdetailupdaterequest.md)
  The request body you use to update a Beta App Review Detail.
- [object BetaAppReviewDetailResponse](betaappreviewdetailresponse.md)
  The response body for endpoints that read or modify the beta review contact and demo details for an app.
- [object BetaAppReviewDetailWithoutIncludesResponse](betaappreviewdetailwithoutincludesresponse.md)
  A response containing a single beta app review detail, without related resources.
- [object BetaAppReviewDetailsResponse](betaappreviewdetailsresponse.md)
  A response containing a list of beta app review detail records.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object BetaAppReviewDetailAppLinkageResponse](betaappreviewdetailapplinkageresponse.md)

## See Also

- [Beta App Review Submissions](beta-app-review-submissions.md)
  The submissions of builds for beta app review, including the status of submissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-review-detail)*
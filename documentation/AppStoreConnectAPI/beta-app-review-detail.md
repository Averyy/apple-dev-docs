# Beta App Review Detail

**Framework**: App Store Connect API

Information about your app required for beta app review.

#### Overview

Before an app can be distributed to external testers, it must be reviewed by Apple. A `betaAppReviewDetails` resource contains the information Apple requires when you submit a build for review, including a demo account login and contact details in case the reviewer has questions.

## Topics

### Getting Beta App Review Details
- [List Beta App Review Details](get-v1-betaappreviewdetails.md)
  Find and list beta app review details for all apps.
- [Read Beta App Review Detail Information](get-v1-betaappreviewdetails-_id_.md)
  Get beta app review details for a specific app.
- [Read the App Information of a Beta App Review Detail](get-v1-betaappreviewdetails-_id_-app.md)
  Get the app information for a specific beta app review details resource.
- [GET /v1/betaAppReviewDetails/{id}/relationships/app](get-v1-betaappreviewdetails-_id_-relationships-app.md)
### Modifying Beta App Review Details
- [Modify a Beta App Review Detail](patch-v1-betaappreviewdetails-_id_.md)
  Update the details for a specific app’s beta app review.
### Objects
- [object BetaAppReviewDetail](betaappreviewdetail.md)
  The data structure that represents a Beta App Review Details resource.
- [object BetaAppReviewDetailUpdateRequest](betaappreviewdetailupdaterequest.md)
  The request body you use to update a Beta App Review Detail.
- [object BetaAppReviewDetailResponse](betaappreviewdetailresponse.md)
  A response that contains a single Beta App Review Details resource.
- [object BetaAppReviewDetailWithoutIncludesResponse](betaappreviewdetailwithoutincludesresponse.md)
- [object BetaAppReviewDetailsResponse](betaappreviewdetailsresponse.md)
  A response that contains a list of Beta App Review Detail resources.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object BetaAppReviewDetailAppLinkageResponse](betaappreviewdetailapplinkageresponse.md)

## See Also

- [Beta App Review Submissions](beta-app-review-submissions.md)
  The submissions of builds for beta app review, including the status of submissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-review-detail)*
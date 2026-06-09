# BetaAppReviewDetailResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify the beta review contact and demo details for an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewDetailResponse
```

## Properties

- `data` (BetaAppReviewDetail) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([App])

## See Also

- [Read the beta app review details resource of an app](get-v1-apps-_id_-betaappreviewdetail.md)
  Get the beta app review details for a specific app.
- [object BetaAppReviewDetail](betaappreviewdetail.md)
  Contact information and demo credentials provided to App Store reviewers for beta app review.
- [object BetaAppReviewDetailUpdateRequest](betaappreviewdetailupdaterequest.md)
  The request body you use to update a Beta App Review Detail.
- [object BetaAppReviewDetailWithoutIncludesResponse](betaappreviewdetailwithoutincludesresponse.md)
  A response containing a single beta app review detail, without related resources.
- [object BetaAppReviewDetailsResponse](betaappreviewdetailsresponse.md)
  A response containing a list of beta app review detail records.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object BetaAppReviewDetailAppLinkageResponse](betaappreviewdetailapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewdetailresponse)*
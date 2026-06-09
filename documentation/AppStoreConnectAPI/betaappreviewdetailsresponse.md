# BetaAppReviewDetailsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of beta app review detail records.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewDetailsResponse
```

## Properties

- `data` ([BetaAppReviewDetail]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([App])

## See Also

- [List beta app review details](get-v1-betaappreviewdetails.md)
  Find and list beta app review details for all apps.
- [object BetaAppReviewDetail](betaappreviewdetail.md)
  Contact information and demo credentials provided to App Store reviewers for beta app review.
- [object BetaAppReviewDetailUpdateRequest](betaappreviewdetailupdaterequest.md)
  The request body you use to update a Beta App Review Detail.
- [object BetaAppReviewDetailResponse](betaappreviewdetailresponse.md)
  The response body for endpoints that read or modify the beta review contact and demo details for an app.
- [object BetaAppReviewDetailWithoutIncludesResponse](betaappreviewdetailwithoutincludesresponse.md)
  A response containing a single beta app review detail, without related resources.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object BetaAppReviewDetailAppLinkageResponse](betaappreviewdetailapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewdetailsresponse)*
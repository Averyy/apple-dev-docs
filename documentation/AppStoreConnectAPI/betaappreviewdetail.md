# BetaAppReviewDetail

**Framework**: App Store Connect API  
**Kind**: dictionary

Contact information and demo credentials provided to App Store reviewers for beta app review.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppReviewDetail
```

## Topics

### Objects
- [object BetaAppReviewDetail.Attributes](betaappreviewdetail/attributes-data.dictionary.md)
  Attributes that describe a Beta App Review Details resource.
- [object BetaAppReviewDetail.Relationships](betaappreviewdetail/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaAppReviewDetail.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (BetaAppReviewDetail.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappreviewdetail)*
# BetaGroupsWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response body that contains a list of beta groups without any includes.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BetaGroupsWithoutIncludesResponse
```

## Properties

- `data` ([BetaGroup]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BetaGroup](betagroup.md)
  A group of beta testers and builds that you use to manage TestFlight distribution for an app.
- [object BetaGroupResponse](betagroupresponse.md)
  The response body for endpoints that create, read, or modify a TestFlight beta group.
- [object BetaGroupCreateRequest](betagroupcreaterequest.md)
  The request body you use to create a Beta Group.
- [object BetaGroupUpdateRequest](betagroupupdaterequest.md)
  The request body you use to update a Beta Group.
- [object BetaGroupBuildsLinkagesRequest](betagroupbuildslinkagesrequest.md)
  A request body you use to add or remove builds from a beta group.
- [object BetaGroupBetaTestersLinkagesRequest](betagroupbetatesterslinkagesrequest.md)
  A request body you use to add or remove beta testers from a beta group.
- [object BetaGroupBetaTestersLinkagesResponse](betagroupbetatesterslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaGroupBuildsLinkagesResponse](betagroupbuildslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaPublicLinkUsagesV1MetricResponse](betapubliclinkusagesv1metricresponse.md)
  A metrics response containing usage data for a TestFlight public invite link, showing tester enrollment trends.
- [object BetaGroupsResponse](betagroupsresponse.md)
  The response body for endpoints that list TestFlight beta groups.
- [object BetaGroupAppLinkageResponse](betagroupapplinkageresponse.md)
- [object BetaGroupBetaRecruitmentCriteriaLinkageResponse](betagroupbetarecruitmentcriterialinkageresponse.md)
- [object BetaGroupBetaRecruitmentCriterionCompatibleBuildCheckLinkageResponse](betagroupbetarecruitmentcriterioncompatiblebuildchecklinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betagroupswithoutincludesresponse)*
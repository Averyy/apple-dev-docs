# BetaGroup

**Framework**: App Store Connect API  
**Kind**: dictionary

A group of beta testers and builds that you use to manage TestFlight distribution for an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaGroup
```

## Topics

### Objects
- [object BetaGroup.Attributes](betagroup/attributes-data.dictionary.md)
  Attributes with values that describe a beta group update request.
- [object BetaGroup.Relationships](betagroup/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaGroup.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BetaGroup.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object BetaGroupResponse](betagroupresponse.md)
  The response body for endpoints that create, read, or modify a TestFlight beta group.
- [object BetaGroupsWithoutIncludesResponse](betagroupswithoutincludesresponse.md)
  A response body that contains a list of beta groups without any includes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betagroup)*
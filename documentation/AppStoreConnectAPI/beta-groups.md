# Beta Groups

**Framework**: App Store Connect API

Groups of beta testers that have access to one or more builds.

#### Overview

A `betaGroups` resource represents the group of testers that have access to builds for testing. Each beta group is associated with a single app and contains one or more builds. Every tester has access to every build in the group.

There are two types of beta tester groups:

- Internal beta tester — Contains members of your App Store Connect team whom you’ve designated as beta testers. For more information about internal testers, see[`Add internal testers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/add-internal-testers).
- External beta tester — You create and manage these groups. They may contain individuals from your company who don’t qualify as internal testers, or people outside of your organization that you’ve invited to test your app. For more information about external testers, see [`Invite external testers`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers).

Add beta testers to a group through App Store Connect or with this API.

## Topics

### Creating, Modifying, and Deleting Beta Groups
- [Create a beta group](post-v1-betagroups.md)
  Create a beta group associated with an app, optionally enabling TestFlight public links.
- [Modify a beta group](patch-v1-betagroups-_id_.md)
  Modify a beta group’s metadata, including changing its TestFlight public link status.
- [Delete a beta group](delete-v1-betagroups-_id_.md)
  Delete a beta group and remove beta tester access to associated builds.
### Getting Beta Group Information
- [List beta groups](get-v1-betagroups.md)
  Find and list beta groups for all apps.
- [Read beta group information](get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the app information of a beta group](get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [Get the app ID for a beta group](get-v1-betagroups-_id_-relationships-app.md)
- [Read Metrics for Beta Testers in a Beta Group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read Recruitment Criteria for a Beta Group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [List beta recruitment criterion IDs for a beta group](get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Read build compatibility for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibility information for a specific beta group.
- [Get the compatible build check ID for a beta group recruitment criterion](get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)
### Adding and Removing Builds and Testers
- [Add beta testers to a beta group](post-v1-betagroups-_id_-relationships-betatesters.md)
  Add a specific beta tester to one or more beta groups for beta testing.
- [Remove beta testers from a beta group](delete-v1-betagroups-_id_-relationships-betatesters.md)
  Remove a specific beta tester from a one or more beta groups, revoking their access to test builds associated with those groups.
- [Add builds to a beta group](post-v1-betagroups-_id_-relationships-builds.md)
  Associate builds with a beta group to enable the group to test the builds.
- [Remove builds from a beta group](delete-v1-betagroups-_id_-relationships-builds.md)
  Remove access to test one or more builds from beta testers in a specific beta group.
### Reading Build and Beta Tester Information
- [List all builds for a beta group](get-v1-betagroups-_id_-builds.md)
  Get a list of builds associated with a specific beta group.
- [Get all build ids in a beta group](get-v1-betagroups-_id_-relationships-builds.md)
  Get a list of build resource IDs in a specific beta group.
- [List all beta testers in a beta group](get-v1-betagroups-_id_-betatesters.md)
  Get a list of beta testers contained in a specific beta group.
- [Get all beta tester ids in a beta group](get-v1-betagroups-_id_-relationships-betatesters.md)
  Get a list of the beta tester resource IDs in a specific beta group.
### Measuring public link usage
- [Read Public Link Usage Metrics for a Beta Group](get-v1-betagroups-_id_-metrics-publiclinkusages.md)
  Get public link usage metrics for a specific beta group.
### Objects
- [object BetaGroup](betagroup.md)
  A group of beta testers and builds that you use to manage TestFlight distribution for an app.
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

## See Also

- [Beta Testers](beta-testers.md)
  People who can install and test prerelease builds.
- [Beta Tester Invitations](beta-tester-invitations.md)
  Requests to send or resend an email inviting a beta tester to test an app.
- [Beta recruitment criteria](beta-recruitment-criteria.md)
  Create public links that accept testers with specific device and OS combinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-groups)*
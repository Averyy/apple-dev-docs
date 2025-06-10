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
- [Create a Beta Group](post-v1-betagroups.md)
  Create a beta group associated with an app, optionally enabling TestFlight public links.
- [Modify a Beta Group](patch-v1-betagroups-_id_.md)
  Modify a beta group’s metadata, including changing its TestFlight public link status.
- [Delete a Beta Group](delete-v1-betagroups-_id_.md)
  Delete a beta group and remove beta tester access to associated builds.
### Getting Beta Group Information
- [List Beta Groups](get-v1-betagroups.md)
  Find and list beta groups for all apps.
- [Read Beta Group Information](get-v1-betagroups-_id_.md)
  Get a specific beta group.
- [Read the App Information of a Beta Group](get-v1-betagroups-_id_-app.md)
  Get the app information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/app](get-v1-betagroups-_id_-relationships-app.md)
- [Read metrics for beta testers in a beta group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read recruitment criteria for a beta group](get-v1-betagroups-_id_-betarecruitmentcriteria.md)
  Get the recruitment criteria information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/betaRecruitmentCriteria](get-v1-betagroups-_id_-relationships-betarecruitmentcriteria.md)
- [Read build compatibilty for a beta group](get-v1-betagroups-_id_-betarecruitmentcriterioncompatiblebuildcheck.md)
  Get the build compatibilty information for a specific beta group.
- [GET /v1/betaGroups/{id}/relationships/betaRecruitmentCriterionCompatibleBuildCheck](get-v1-betagroups-_id_-relationships-betarecruitmentcriterioncompatiblebuildcheck.md)
### Adding and Removing Builds and Testers
- [Add Beta Testers to a Beta Group](post-v1-betagroups-_id_-relationships-betatesters.md)
  Add a specific beta tester to one or more beta groups for beta testing.
- [Remove Beta Testers from a Beta Group](delete-v1-betagroups-_id_-relationships-betatesters.md)
  Remove a specific beta tester from a one or more beta groups, revoking their access to test builds associated with those groups.
- [Add Builds to a Beta Group](post-v1-betagroups-_id_-relationships-builds.md)
  Associate builds with a beta group to enable the group to test the builds.
- [Remove Builds from a Beta Group](delete-v1-betagroups-_id_-relationships-builds.md)
  Remove access to test one or more builds from beta testers in a specific beta group.
### Reading Build and Beta Tester Information
- [List All Builds for a Beta Group](get-v1-betagroups-_id_-builds.md)
  Get a list of builds associated with a specific beta group.
- [Get All Build IDs in a Beta Group](get-v1-betagroups-_id_-relationships-builds.md)
  Get a list of build resource IDs in a specific beta group.
- [List All Beta Testers in a Beta Group](get-v1-betagroups-_id_-betatesters.md)
  Get a list of beta testers contained in a specific beta group.
- [Get All Beta Tester IDs in a Beta Group](get-v1-betagroups-_id_-relationships-betatesters.md)
  Get a list of the beta tester resource IDs in a specific beta group.
### Measuring public link usage
- [Read public link usage metrics for a beta group](get-v1-betagroups-_id_-metrics-publiclinkusages.md)
  Get public link usage metrics for a specific beta group.
### Objects
- [object BetaGroup](betagroup.md)
  The data structure that represents a Beta Groups resource.
- [object BetaGroupResponse](betagroupresponse.md)
  A response that contains a single Beta Groups resource.
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
- [object BetaGroupsResponse](betagroupsresponse.md)
  A response that contains a list of Beta Group resources.
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
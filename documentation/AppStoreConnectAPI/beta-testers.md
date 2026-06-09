# Beta Testers

**Framework**: App Store Connect API

People who can install and test prerelease builds.

#### Overview

The `betaTesters` resource represents the people who can install and test prerelease builds. You can create and delete beta testers, add and remove them from beta groups, and assign them to an app or a build.

When you create a beta tester, they must have an email address and must be assigned to an app, a build, or a beta group. Anonymous testers added via a TestFlight public link may not have an email address.

## Topics

### Creating and Deleting Beta Testers
- [Create a beta tester](post-v1-betatesters.md)
  Create a beta tester assigned to a group, a build, or an app.
- [Delete a beta tester](delete-v1-betatesters-_id_.md)
  Remove a beta tester’s ability to test all apps.
### Getting Beta Tester Information
- [List beta testers](get-v1-betatesters.md)
  Find and list beta testers for all apps, builds, and beta groups.
- [Read beta tester information](get-v1-betatesters-_id_.md)
  Get a specific beta tester.
### Assigning Groups and Access
- [Add a beta tester to beta groups](post-v1-betatesters-_id_-relationships-betagroups.md)
  Add one or more beta testers to a specific beta group.
- [Remove a beta tester from beta groups](delete-v1-betatesters-_id_-relationships-betagroups.md)
  Remove a specific beta tester from one or more beta groups, revoking their access to test builds associated with those groups.
- [Individually assign a beta tester to builds](post-v1-betatesters-_id_-relationships-builds.md)
  Individually assign a beta tester to a build.
- [Individually unassign a beta tester from builds](delete-v1-betatesters-_id_-relationships-builds.md)
  Remove an individually assigned beta tester’s ability to test a build.
- [Remove a beta tester’s access to apps](delete-v1-betatesters-_id_-relationships-apps.md)
  Remove a specific beta tester’s access to test any builds of one or more apps.
### Reading Beta Tester Details
- [List all apps for a beta tester](get-v1-betatesters-_id_-apps.md)
  Get a list of apps that a beta tester can test.
- [Get all app resource ids for a beta tester](get-v1-betatesters-_id_-relationships-apps.md)
  Get a list of app resource IDs associated with a beta tester.
- [List all builds individually assigned to a beta tester](get-v1-betatesters-_id_-builds.md)
  Get a list of builds individually assigned to a specific beta tester.
- [Get all ids of builds individually assigned to a beta tester](get-v1-betatesters-_id_-relationships-builds.md)
  Get a list of build resource IDs individually assigned to a specific beta tester.
- [List all beta groups to which a beta tester belongs](get-v1-betatesters-_id_-betagroups.md)
  Get a list of beta groups that contain a specific beta tester.
- [Get all beta group ids of a beta tester's groups](get-v1-betatesters-_id_-relationships-betagroups.md)
  Get a list of group resource IDs associated with a beta tester.
### Beta Tester Metrics
- [Read Beta Tester Metrics for an App](get-v1-apps-_id_-metrics-betatesterusages.md)
  Get usage metrics for beta testers of a specific app.
- [Read Metrics for Beta Testers in a Beta Group](get-v1-betagroups-_id_-metrics-betatesterusages.md)
  Get beta tester usage metrics for a beta group.
- [Read Beta Tester Usage Metrics](get-v1-betatesters-_id_-metrics-betatesterusages.md)
  Get usage metrics for a specific beta tester.
### Objects
- [object BetaTester](betatester.md)
  An individual enrolled as a beta tester in TestFlight, identified by their email address and associated with one or more apps or groups.
- [object BetaTestersWithoutIncludesResponse](betatesterswithoutincludesresponse.md)
  A response containing a list of TestFlight beta testers, without related resources.
- [object BetaTesterAppsLinkagesRequest](betatesterappslinkagesrequest.md)
  A request body you use to remove an app from a beta tester.
- [object BetaTesterAppsLinkagesResponse](betatesterappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterBetaGroupsLinkagesRequest](betatesterbetagroupslinkagesrequest.md)
  A request body you use to add or remove beta groups from a beta tester.
- [object BetaTesterBetaGroupsLinkagesResponse](betatesterbetagroupslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterBuildsLinkagesRequest](betatesterbuildslinkagesrequest.md)
  A request body you use to add or remove builds from a beta tester.
- [object BetaTesterBuildsLinkagesResponse](betatesterbuildslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterCreateRequest](betatestercreaterequest.md)
  The request body you use to create a BetaTester.
- [object BetaTesterResponse](betatesterresponse.md)
  The response body for endpoints that create, read, or modify a TestFlight beta tester.
- [object BetaTestersResponse](betatestersresponse.md)
  The response body for endpoints that list TestFlight beta testers.
- [object AppsBetaTesterUsagesV1MetricResponse](appsbetatesterusagesv1metricresponse.md)
  A response that contains one or more beta app tester metric resources.
- [object BetaTesterUsagesV1MetricResponse](betatesterusagesv1metricresponse.md)
  A response that contains one or more beta tester usage metric resources.

## See Also

- [Beta Tester Invitations](beta-tester-invitations.md)
  Requests to send or resend an email inviting a beta tester to test an app.
- [Beta recruitment criteria](beta-recruitment-criteria.md)
  Create public links that accept testers with specific device and OS combinations.
- [Beta Groups](beta-groups.md)
  Groups of beta testers that have access to one or more builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-testers)*
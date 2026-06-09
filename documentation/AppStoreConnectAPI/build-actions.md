# Build Actions

**Framework**: App Store Connect API

Read information about actions you configured for an Xcode Cloud workflow and their related data such as artifacts, issues, or test results.

#### Overview

The `ciBuildActions` resource represents the actions Xcode Cloud performed when it built your project or workspace. Use it to read information about the actions Xcode Cloud performed during a build; for example:

- Type, name, and date information of the action
- Status information for an ongoing and completed action
- Artifacts created by the action
- Issues that occurred
- Detailed information about test results

To update a workflow’s actions, use the [`Workflows`](workflows.md) resource.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Build Actions
- [Read build action information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List all artifacts for a build action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the xcode cloud build information for a build action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List all issues for a build action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [List all test results for an xcode cloud test action](get-v1-cibuildactions-_id_-testresults.md)
  List all test results for a specific test action Xcode Cloud performed as part of a build.
- [List artifact IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [Get the build run ID for a CI build action](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [List issue IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-issues.md)
- [List test result IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-testresults.md)
### Objects
- [object CiBuildAction](cibuildaction.md)
  The execution result of a specific action step within an Xcode Cloud build run, including its status and issues.
- [object CiArtifactsResponse](ciartifactsresponse.md)
  The response body for endpoints that list artifacts produced by an Xcode Cloud build action.
- [object CiBuildActionResponse](cibuildactionresponse.md)
  The response body for endpoints that read a single Xcode Cloud build action.
- [object CiIssuesResponse](ciissuesresponse.md)
  The response body for endpoints that list issues from an Xcode Cloud build action.
- [object CiTestResultsResponse](citestresultsresponse.md)
  The response body for endpoints that list test results from an Xcode Cloud build action.
- [object CiBuildActionArtifactsLinkagesResponse](cibuildactionartifactslinkagesresponse.md)
- [object CiBuildActionBuildRunLinkageResponse](cibuildactionbuildrunlinkageresponse.md)
- [object CiBuildActionIssuesLinkagesResponse](cibuildactionissueslinkagesresponse.md)
- [object CiBuildActionTestResultsLinkagesResponse](cibuildactiontestresultslinkagesresponse.md)

## See Also

- [Build Runs](build-runs.md)
  Read detailed build information and start new builds.
- [Artifacts](artifacts.md)
  Read information about artifacts Xcode Cloud creates when it performs a build.
- [Issues](issues.md)
  Read information about issues that occurred when Xcode Cloud performs a build.
- [Test Results](test-results.md)
  Read test results for test actions Xcode Cloud performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-actions)*
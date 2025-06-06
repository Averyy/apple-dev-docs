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

 This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Build Actions
- [Read Build Action Information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List All Artifacts for a Build Action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the Xcode Cloud Build Information for a Build Action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List All Issues for a Build Action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [List All Test Results for an Xcode Cloud Test Action](get-v1-cibuildactions-_id_-testresults.md)
  List all test results for a specific test action Xcode Cloud performed as part of a build.
### Objects
- [object CiBuildAction](cibuildaction.md)
  The data structure that represents a Build Actions resource.
- [object CiArtifactsResponse](ciartifactsresponse.md)
  A response that contains a list of Artifacts resources.
- [object CiBuildActionResponse](cibuildactionresponse.md)
  A response that contains a single Build Actions resource.
- [object CiIssuesResponse](ciissuesresponse.md)
  A response that contains a list of Issues resources.
- [object CiTestResultsResponse](citestresultsresponse.md)
  A response that contains a list of Test Results resources.

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
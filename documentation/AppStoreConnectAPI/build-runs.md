# Build Runs

**Framework**: App Store Connect API

Read detailed build information and start new builds.

#### Overview

The `ciBuildRuns` resource represents an Xcode Cloud build. Use it to get a list of builds Xcode Cloud performed and access detailed information for a specific build; for example:

- The status of ongoing and completed builds
- The number of issues Xcode Cloud encountered during the build
- The build number
- Start and completion dates
- Actions Xcode Cloud performed

Additionally, use the `ciBuildRuns` resource to tell Xcode Cloud to start a new build.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Build Information
- [Read xcode cloud build information](get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List all actions for an xcode cloud build](get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [List all builds xcode cloud created in app store connect](get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [List action IDs for a CI build run](get-v1-cibuildruns-_id_-relationships-actions.md)
- [List build IDs for a CI build run](get-v1-cibuildruns-_id_-relationships-builds.md)
### Starting a New Build
- [Start a build](post-v1-cibuildruns.md)
  Start a new Xcode Cloud build for a workflow.
### Objects
- [object CiBuildRun](cibuildrun.md)
  A single execution of an Xcode Cloud workflow, capturing the trigger, commit, status, and artifacts produced.
- [object CiBuildRunCreateRequest](cibuildruncreaterequest.md)
  The request body you use to start a new Xcode Cloud build.
- [object CiBuildRunResponse](cibuildrunresponse.md)
  The response body for endpoints that start or read a single Xcode Cloud build run.
- [object CiBuildActionsResponse](cibuildactionsresponse.md)
  The response body for endpoints that list actions for an Xcode Cloud build run.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)

## See Also

- [Build Actions](build-actions.md)
  Read information about actions you configured for an Xcode Cloud workflow and their related data such as artifacts, issues, or test results.
- [Artifacts](artifacts.md)
  Read information about artifacts Xcode Cloud creates when it performs a build.
- [Issues](issues.md)
  Read information about issues that occurred when Xcode Cloud performs a build.
- [Test Results](test-results.md)
  Read test results for test actions Xcode Cloud performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-runs)*
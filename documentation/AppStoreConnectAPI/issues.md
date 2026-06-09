# Issues

**Framework**: App Store Connect API

Read information about issues that occurred when Xcode Cloud performs a build.

#### Overview

The `ciIssues` resource represents issues that occur when Xcode Cloud performs a build. Use it to access a list of issues that occurred and read detailed issue information; for example:

- The type of issue that occurred
- The location in your code where the issue occurred
- A message describing the issue

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Xcode Cloud Build Issues
- [Read xcode cloud issue information](get-v1-ciissues-_id_.md)
  Get information about a specific issue that occurred when Xcode Cloud performed a build.
### Objects
- [object CiIssue](ciissue.md)
  A warning or error produced during an Xcode Cloud build action, associated with a source file location.
- [object FileLocation](filelocation.md)
  A source code location reference indicating the file path, line number, and column of an issue in an Xcode Cloud build.
- [object CiIssueResponse](ciissueresponse.md)
  The response body for endpoints that read a single issue from an Xcode Cloud build action.

## See Also

- [Build Runs](build-runs.md)
  Read detailed build information and start new builds.
- [Build Actions](build-actions.md)
  Read information about actions you configured for an Xcode Cloud workflow and their related data such as artifacts, issues, or test results.
- [Artifacts](artifacts.md)
  Read information about artifacts Xcode Cloud creates when it performs a build.
- [Test Results](test-results.md)
  Read test results for test actions Xcode Cloud performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/issues)*
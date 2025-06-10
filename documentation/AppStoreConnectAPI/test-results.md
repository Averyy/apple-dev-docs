# Test Results

**Framework**: App Store Connect API

Read test results for test actions Xcode Cloud performs.

#### Overview

The `ciTestResult` resource represents the test results that Xcode Cloud makes available if you configure a workflow to include a test action. Use this resource to access:

- The name of the test class
- Test file information
- The name and operating system version of the simulated device that Xcode Cloud used to perform the tests
- The time it took to run the tests
- Test status information
- A unique identifier for the tests Xcode Cloud ran

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Test Results
- [Read Test Result Information](get-v1-citestresults-_id_.md)
  Get a specific test result Xcode Cloud created when it performed a build with a test action.
### Objects and Types
- [object CiTestResult](citestresult.md)
  The data structure that represents a Test Results resource.
- [object CiTestResultResponse](citestresultresponse.md)
  A response that contains a single Test Results resource.

## See Also

- [Build Runs](build-runs.md)
  Read detailed build information and start new builds.
- [Build Actions](build-actions.md)
  Read information about actions you configured for an Xcode Cloud workflow and their related data such as artifacts, issues, or test results.
- [Artifacts](artifacts.md)
  Read information about artifacts Xcode Cloud creates when it performs a build.
- [Issues](issues.md)
  Read information about issues that occurred when Xcode Cloud performs a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/test-results)*
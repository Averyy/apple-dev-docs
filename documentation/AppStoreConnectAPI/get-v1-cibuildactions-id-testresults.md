# List All Test Results for an Xcode Cloud Test Action

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all test results for a specific test action Xcode Cloud performed as part of a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists the test results for an Xcode Cloud build that performed a test action. Use the information provided in the response to display test results on a dashboard, create a new task for a failing test in your issue tracker, and so on.

##### Example Request and Response

## See Also

- [Read Build Action Information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List All Artifacts for a Build Action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the Xcode Cloud Build Information for a Build Action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List All Issues for a Build Action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [GET /v1/ciBuildActions/{id}/relationships/artifacts](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [GET /v1/ciBuildActions/{id}/relationships/buildRun](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [GET /v1/ciBuildActions/{id}/relationships/issues](get-v1-cibuildactions-_id_-relationships-issues.md)
- [GET /v1/ciBuildActions/{id}/relationships/testResults](get-v1-cibuildactions-_id_-relationships-testresults.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_-testresults)*
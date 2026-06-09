# List all artifacts for a build action

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all artifacts Xcode Cloud created when it performed an action.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/{id}/artifacts`

## Parameters

- `fields[ciArtifacts]` ([string]): Additional fields to include for each Artifacts resource returned by the response.
- `limit` (integer): The number of Artifacts resources to return.

## See Also

- [Read build action information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_-artifacts)*
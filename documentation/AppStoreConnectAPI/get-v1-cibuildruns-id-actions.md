# List All Actions for an Xcode Cloud Build

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all actions Xcode Cloud performed during a specific build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists actions Xcode Cloud performed during a specific build. Use the information provided in the response to display detailed action information on a dashboard or to read additional data; for example, test results.

##### Example Request and Response

## See Also

- [Read Xcode Cloud Build Information](get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List All Builds Xcode Cloud Created in App Store Connect](get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [GET /v1/ciBuildRuns/{id}/relationships/actions](get-v1-cibuildruns-_id_-relationships-actions.md)
- [GET /v1/ciBuildRuns/{id}/relationships/builds](get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-actions)*
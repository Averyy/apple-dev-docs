# List action IDs for a CI build run

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}/relationships/actions`

## Parameters

- `limit` (integer)

## See Also

- [Read xcode cloud build information](get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List all actions for an xcode cloud build](get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [List all builds xcode cloud created in app store connect](get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [List build IDs for a CI build run](get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-relationships-actions)*
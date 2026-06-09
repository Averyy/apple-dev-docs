# Read build information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}`

## Parameters

- `fields[appEncryptionDeclarations]` ([string]): Fields to return for included related types.
- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaTesters]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.
- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.
- `fields[betaBuildLocalizations]` ([string]): Fields to return for included related types.
- `limit[individualTesters]` (integer): Number of included related resources to return.
- `limit[betaBuildLocalizations]` (integer): Number of included related resources to return.
- `limit[icons]` (integer)
- `fields[appStoreVersions]` ([string])
- `fields[buildIcons]` ([string])
- `limit[buildBundles]` (integer)
- `limit[betaGroups]` (integer)
- `fields[betaGroups]` ([string])
- `fields[buildBundles]` ([string])
- `fields[buildUploads]` ([string])

## See Also

- [List builds](get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read the app information of a build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app id of a build](get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Read the app store version information of a build](get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [Get the App Store version ID for a build](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the prerelease version of a build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [Get the prerelease version ID for a build](get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read Usage Metrics for a Beta Build](get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_)*
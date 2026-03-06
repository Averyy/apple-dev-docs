# List Builds

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list builds for all apps in App Store Connect.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds`

## Parameters

- `fields[appEncryptionDeclarations]` ([string]): Fields to return for included related types.
- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaTesters]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[expired]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[id]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[preReleaseVersion]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[processingState]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `limit[individualTesters]` (integer): Number of included related resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[usesNonExemptEncryption]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[preReleaseVersion.version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.
- `filter[betaGroups]` ([string]): Attributes, relationships, and IDs by which to filter.
- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.
- `filter[betaAppReviewSubmission.betaReviewState]` ([string]): Attributes, relationships, and IDs by which to filter.
- `fields[betaBuildLocalizations]` ([string]): Fields to return for included related types.
- `limit[betaBuildLocalizations]` (integer): Number of included related resources to return.
- `limit[icons]` (integer)
- `fields[appStoreVersions]` ([string])
- `fields[buildIcons]` ([string])
- `filter[appStoreVersion]` ([string])
- `filter[preReleaseVersion.platform]` ([string])
- `filter[buildAudienceType]` ([string])
- `limit[buildBundles]` (integer)
- `limit[betaGroups]` (integer)
- `exists[usesNonExemptEncryption]` (boolean)

## See Also

- [Read Build Information](get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the App Information of a Build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app ID of a build](get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Read the App Store Version Information of a Build](get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [GET /v1/builds/{id}/relationships/appStoreVersion](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the Prerelease Version of a Build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [GET /v1/builds/{id}/relationships/preReleaseVersion](get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read usage metrics for a beta build](get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds)*
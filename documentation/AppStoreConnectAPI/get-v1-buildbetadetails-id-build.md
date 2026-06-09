# Read the build information of a build beta detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the build information for a specific build beta details resource.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBetaDetails/{id}/build`

## Parameters

- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[appEncryptionDeclarations]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])
- `fields[betaAppReviewSubmissions]` ([string])
- `fields[betaBuildLocalizations]` ([string])
- `fields[betaGroups]` ([string])
- `fields[betaTesters]` ([string])
- `fields[buildBetaDetails]` ([string])
- `fields[buildBundles]` ([string])
- `fields[buildIcons]` ([string])
- `fields[buildUploads]` ([string])
- `fields[preReleaseVersions]` ([string])
- `include` ([string])
- `limit[betaBuildLocalizations]` (integer)
- `limit[betaGroups]` (integer)
- `limit[buildBundles]` (integer)
- `limit[icons]` (integer)
- `limit[individualTesters]` (integer)

## See Also

- [List build beta details](get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [Read build beta detail information](get-v1-buildbetadetails-_id_.md)
  Get a specific build beta details resource.
- [Get the build ID for a build beta detail](get-v1-buildbetadetails-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbetadetails-_id_-build)*
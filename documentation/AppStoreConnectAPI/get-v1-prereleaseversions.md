# List prerelease versions

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of prerelease versions for all apps.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/preReleaseVersions`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds.expired]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds.processingState]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[platform]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `limit[builds]` (integer): Number of included related resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[builds.version]` ([string])
- `filter[builds.buildAudienceType]` ([string])

## See Also

- [Read prerelease version information](get-v1-prereleaseversions-_id_.md)
  Get information about a specific prerelease version.
- [Read the app information of a prerelease version](get-v1-prereleaseversions-_id_-app.md)
  Get the app information for a specific prerelease version.
- [Get the app ID for a prerelease version](get-v1-prereleaseversions-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-prereleaseversions)*
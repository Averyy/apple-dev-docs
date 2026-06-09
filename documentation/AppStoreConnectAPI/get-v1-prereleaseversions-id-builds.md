# List all builds of a prerelease version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of builds of a specific prerelease version.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/preReleaseVersions/{id}/builds`

## Parameters

- `limit` (integer): Number of resources to return.
- `fields[builds]` ([string]): Fields to return for included related types.

## See Also

- [List build IDs for a prerelease version](get-v1-prereleaseversions-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-prereleaseversions-_id_-builds)*
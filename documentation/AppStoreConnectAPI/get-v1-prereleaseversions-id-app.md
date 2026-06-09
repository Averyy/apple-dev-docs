# Read the app information of a prerelease version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the app information for a specific prerelease version.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/preReleaseVersions/{id}/app`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

## See Also

- [List prerelease versions](get-v1-prereleaseversions.md)
  Get a list of prerelease versions for all apps.
- [Read prerelease version information](get-v1-prereleaseversions-_id_.md)
  Get information about a specific prerelease version.
- [Get the app ID for a prerelease version](get-v1-prereleaseversions-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-prereleaseversions-_id_-app)*
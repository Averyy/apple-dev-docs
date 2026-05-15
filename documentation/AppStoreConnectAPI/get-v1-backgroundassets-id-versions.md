# Read Version Details for a Background Asset

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a specific background asset version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssets/{id}/versions`

## Parameters

- `fields[backgroundAssetVersionAppStoreReleases]` ([string])
- `fields[backgroundAssetVersionExternalBetaReleases]` ([string])
- `fields[backgroundAssetVersionInternalBetaReleases]` ([string])
- `fields[backgroundAssetVersions]` ([string])
- `filter[appStoreRelease.state]` ([string])
- `filter[externalBetaRelease.state]` ([string])
- `filter[internalBetaRelease.state]` ([string])
- `filter[state]` ([string])
- `filter[version]` ([string])
- `include` ([string])
- `limit` (integer)
- `sort` ([string])
- `fields[backgroundAssetUploadFiles]` ([string])
- `fields[backgroundAssets]` ([string])
- `filter[platforms]` ([string])

## See Also

- [List All Assets Packs for an App](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the Assets Packs IDs for an App](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Read Background Assets Information](get-v1-backgroundassets-_id_.md)
  Get details about a specific background asset.
- [Read Version IDs for a Background Asset](get-v1-backgroundassets-_id_-relationships-versions.md)
  Get version IDs about a specific background asset version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassets-_id_-versions)*
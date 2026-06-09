# Read Background Assets Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a specific background asset.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssets/{id}`

## Parameters

- `fields[backgroundAssets]` ([string])
- `include` ([string])
- `fields[apps]` ([string])
- `fields[backgroundAssetVersions]` ([string])

## See Also

- [List all background assets for an app](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the assets packs ids for an app](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Read Version Details for a Background Asset](get-v1-backgroundassets-_id_-versions.md)
  Get details about a specific background asset version.
- [Read version ids for a background asset](get-v1-backgroundassets-_id_-relationships-versions.md)
  Get version IDs about a specific background asset version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassets-_id_)*
# List all background assets for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the Apple-hosted background assets for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.4 release notes](app-store-connect-api-4-4-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/backgroundAssets`

## Parameters

- `fields[backgroundAssetVersions]` ([string]): Additional fields to include for each background asset version resource that the response returns.
- `fields[backgroundAssets]` ([string]): Additional fields to include for each background asset resource that the response returns.
- `filter[assetPackIdentifier]` ([string]): Filter the returned background assets by asset pack identifier.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of background asset resources to return.
- `fields[apps]` ([string])
- `filter[archived]` ([string])
- `filter[versions.locale]` ([string])
- `filter[versions.platforms]` ([string])
- `sort` ([string])

## See Also

- [List the assets packs ids for an app](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Modify a Background Asset](patch-v1-backgroundassets-_id_.md)
  Update a specific background asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-backgroundassets)*
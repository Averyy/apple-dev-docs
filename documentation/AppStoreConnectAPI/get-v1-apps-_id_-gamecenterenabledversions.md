# List all game center enabled versions for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of Game Center enabled versions for a specific app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/gameCenterEnabledVersions`

## Parameters

- `fields[gameCenterEnabledVersions]` ([string]): Additional fields to include for each Game Center enabled version resource returned by the response.
- `filter[id]` ([string]): Filter the returned Game Center enabled versions by ID.
- `filter[platform]` ([string]): Filter the returned Game Center enabled versions by platform.
- `filter[versionString]` ([string]): Filter the returned Game Center enabled versions by version string.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of Game Center enabled version resources to return.
- `sort` ([string]): Attributes by which to sort.
- `limit[compatibleVersions]` (integer): The maximum number of related compatible versions resources to return.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

## See Also

- [List all compatible versions for a game center enabled version](get-v1-gamecenterenabledversions-_id_-compatibleversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-gamecenterenabledversions)*
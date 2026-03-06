# List territory age ratings for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all territory age ratings for a specific app info.

**Availability**:
- App Store Connect API 4.1+

## Mentions

- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/territoryAgeRatings`

## Parameters

- `fields[territories]` ([string])
- `fields[territoryAgeRatings]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [List territory age rating Ids for an app info](get-v1-appinfos-_id_-relationships-territoryageratings.md)
  List all territory age rating IDs for a specific app info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-territoryageratings)*
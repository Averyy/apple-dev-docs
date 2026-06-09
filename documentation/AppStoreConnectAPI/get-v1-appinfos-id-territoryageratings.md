# List Territory Age Ratings for an App Info

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

- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `fields[territoryAgeRatings]` ([string]): Additional fields to include for each territory age rating resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of territory age rating resources to return.

## See Also

- [List territory age rating IDs for an app info](get-v1-appinfos-_id_-relationships-territoryageratings.md)
  List all territory age rating IDs for a specific app info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-territoryageratings)*
# Read Details for a Nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific featuring nomination.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/nominations/{id}`

## Parameters

- `fields[nominations]` ([string])
- `include` ([string])
- `limit[inAppEvents]` (integer)
- `limit[relatedApps]` (integer)
- `limit[supportedTerritories]` (integer)
- `fields[actors]` ([string])
- `fields[appEvents]` ([string])
- `fields[apps]` ([string])
- `fields[territories]` ([string])

## See Also

- [Create a Featuring Nomination](post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List Nominations](get-v1-nominations.md)
  Get all featuring nominations.
- [Modify a Nomination](patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a Featuring Nomination](delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-nominations-_id_)*
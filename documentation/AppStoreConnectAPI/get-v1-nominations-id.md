# Read details for a nomination

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

## See Also

- [Create a featuring nomination](post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List nominations](get-v1-nominations.md)
  Get all featuring nominations.
- [Modify a nomination](patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a featuring nomination](delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-nominations-_id_)*
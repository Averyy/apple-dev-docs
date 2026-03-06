# List nominations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all featuring nominations.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/nominations`

## Parameters

- `fields[nominations]` ([string])
- `filter[relatedApps]` ([string])
- `filter[state]` ([string]) *(required)*
- `filter[type]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[inAppEvents]` (integer)
- `limit[relatedApps]` (integer)
- `limit[supportedTerritories]` (integer)
- `sort` ([string])

## See Also

- [Create a featuring nomination](post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [Read details for a nomination](get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Modify a nomination](patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a featuring nomination](delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-nominations)*
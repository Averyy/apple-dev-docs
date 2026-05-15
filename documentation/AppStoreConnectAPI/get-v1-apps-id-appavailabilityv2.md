# List Availability for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of availabilities for a specific app.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appAvailabilityV2`

## Parameters

- `fields[appAvailabilities]` ([string])
- `include` ([string])
- `fields[territoryAvailabilities]` ([string])
- `limit[territoryAvailabilities]` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/appAvailabilityV2](get-v1-apps-_id_-relationships-appavailabilityv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appavailabilityv2)*
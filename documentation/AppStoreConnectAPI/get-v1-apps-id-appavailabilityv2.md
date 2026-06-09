# List Availability for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

The data structure that represents a get-v1-apps-{id}-app availability v2 resource.

**Availability**:
- App Store Connect API 3.6+

#### Overview

Get a list of availabilities for a specific app.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appAvailabilityV2`

## Parameters

- `fields[appAvailabilities]` ([string])
- `include` ([string])
- `fields[territoryAvailabilities]` ([string])
- `limit[territoryAvailabilities]` (integer)

## See Also

- [Get the app availability ID for an app](get-v1-apps-_id_-relationships-appavailabilityv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appavailabilityv2)*
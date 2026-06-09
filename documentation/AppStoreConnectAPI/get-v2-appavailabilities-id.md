# Read app availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about your app’s availalbility.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 3.1 release notes](app-store-connect-api-3-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/appAvailabilities/{id}`

## Parameters

- `fields[appAvailabilities]` ([string])
- `fields[territoryAvailabilities]` ([string])
- `include` ([string])
- `limit[territoryAvailabilities]` (integer)

## See Also

- [Read app availablity territories](get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [List territory availability IDs for an app availability](get-v2-appavailabilities-_id_-relationships-territoryavailabilities.md)
  Get a list of territory availability IDs for a specific app availability.
- [Create an app pre-order](post-v2-appavailabilities.md)
  Create an app pre-order and set the expected app release date.
- [Modify the territory availability for an app pre-order](patch-v1-territoryavailabilities-_id_.md)
  Update the release territories for your app pre-order.
- [End an app pre-order](post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-appavailabilities-_id_)*
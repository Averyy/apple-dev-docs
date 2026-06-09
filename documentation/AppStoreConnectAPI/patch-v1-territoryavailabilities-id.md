# Modify the territory availability for an app pre-order

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the release territories for your app pre-order.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/territoryAvailabilities/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read app availability](get-v2-appavailabilities-_id_.md)
  Get information about your app’s availalbility.
- [Read app availablity territories](get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [List territory availability IDs for an app availability](get-v2-appavailabilities-_id_-relationships-territoryavailabilities.md)
  Get a list of territory availability IDs for a specific app availability.
- [Create an app pre-order](post-v2-appavailabilities.md)
  Create an app pre-order and set the expected app release date.
- [End an app pre-order](post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-territoryavailabilities-_id_)*
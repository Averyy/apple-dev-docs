# List territory availability IDs for an app availability

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of territory availability IDs for a specific app availability.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/appAvailabilities/{id}/relationships/territoryAvailabilities`

## Parameters

- `limit` (integer)

## See Also

- [Read app availability](get-v2-appavailabilities-_id_.md)
  Get information about your app’s availalbility.
- [Read app availablity territories](get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [Create an app pre-order](post-v2-appavailabilities.md)
  Create an app pre-order and set the expected app release date.
- [Modify the territory availability for an app pre-order](patch-v1-territoryavailabilities-_id_.md)
  Update the release territories for your app pre-order.
- [End an app pre-order](post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-appavailabilities-_id_-relationships-territoryavailabilities)*
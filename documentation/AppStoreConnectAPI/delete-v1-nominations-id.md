# Delete a Featuring Nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a specific featuring nomination.

**Availability**:
- App Store Connect API 3.8+

#### Overview

- id: An opaque resource ID that uniquely identifies the resource. Obtain the nomination resource ID from the [`List Nominations`](get-v1-nominations.md) response.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/nominations/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a Featuring Nomination](post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List Nominations](get-v1-nominations.md)
  Get all featuring nominations.
- [Read Details for a Nomination](get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Modify a Nomination](patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-nominations-_id_)*
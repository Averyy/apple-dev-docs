# Modify a nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a specific featuring nomination.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/nominations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the nomination resource ID from the [`List nominations`](get-v1-nominations.md) response.

## See Also

- [Create a featuring nomination](post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List nominations](get-v1-nominations.md)
  Get all featuring nominations.
- [Read details for a nomination](get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Delete a featuring nomination](delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-nominations-_id_)*
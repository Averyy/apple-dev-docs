# Read Bundle ID Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific bundle ID.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/bundleIds/{id}`

## Parameters

- `fields[bundleIds]` ([string])
- `fields[profiles]` ([string])
- `include` ([string])
- `limit[profiles]` (integer)
- `fields[bundleIdCapabilities]` ([string])
- `limit[bundleIdCapabilities]` (integer)
- `fields[apps]` ([string])

## See Also

- [List Bundle IDs](get-v1-bundleids.md)
  Find and list bundle IDs that are registered to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-bundleids-_id_)*
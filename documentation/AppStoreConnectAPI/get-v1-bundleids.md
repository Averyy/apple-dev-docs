# List bundle ids

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list bundle IDs that are registered to your team.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/bundleIds`

## Parameters

- `fields[bundleIds]` ([string])
- `fields[profiles]` ([string])
- `filter[id]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string])
- `filter[seedId]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[profiles]` (integer)
- `sort` ([string])
- `fields[bundleIdCapabilities]` ([string])
- `limit[bundleIdCapabilities]` (integer)
- `fields[apps]` ([string])

## See Also

- [Read bundle id information](get-v1-bundleids-_id_.md)
  Get information about a specific bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-bundleids)*